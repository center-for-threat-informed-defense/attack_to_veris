import json
import requests
import pathlib
import os
import numpy
import pytest

from src.util.create_mappings import get_sheets, get_sheet_by_name

@pytest.fixture()
def mappings_dir():
    return pathlib.Path(pathlib.Path(__file__).parent.parent / "src" / "mappings")


@pytest.fixture()
def veris_schema():
    veris_url = f"https://raw.githubusercontent.com/vz-risk/veris/master/verisc-labels.json"
    print(veris_url)
    return requests.get(veris_url, verify=True).json()

@pytest.fixture()
def spreadsheets(mappings_dir):
    attack_types = ["enterprise", "ics", "mobile", "groups"]
    result = {}

    for attack_type in attack_types:
        dir_path = pathlib.Path(mappings_dir, attack_type, "xlsx")

        files = os.listdir(dir_path)
        for file in files:
            if file.endswith(".xlsx"):
                result[attack_type] = pathlib.Path(dir_path / file)
    return result


def merge_lists(l1, l2):
    for item in l2:
        if item not in l1:
            l1.append(item)
    return l1


def get_attack_objects(attack_type, version, groups=False):
    attackid_to_stixid = {}
    if groups:
        enterprise_url = f"https://raw.githubusercontent.com/mitre/cti/ATT%26CK-v{version}/enterprise-attack/enterprise-attack.json"
        ics_url = f"https://raw.githubusercontent.com/mitre/cti/ATT%26CK-v{version}/ics-attack/ics-attack.json"
        mobile_url = f"https://raw.githubusercontent.com/mitre/cti/ATT%26CK-v{version}/mobile-attack/mobile-attack.json"
        stix_objects = requests.get(enterprise_url, verify=True).json()["objects"]
        stix_objects = merge_lists(stix_objects, requests.get(ics_url, verify=True).json()["objects"])
        stix_objects = merge_lists(stix_objects, requests.get(mobile_url, verify=True).json()["objects"])
    else:
        url = f"https://raw.githubusercontent.com/mitre/cti/ATT%26CK-v{version}/{attack_type}-attack/{attack_type}-attack.json"
        stix_objects = requests.get(url, verify=True).json()["objects"]

    if groups:
        type_match = "intrusion-set"
    else:
        type_match = "attack-pattern"
    for stix_object in stix_objects:
        if stix_object["type"] == type_match:
            if "external_references" not in stix_object:
                continue  # skip objects without IDs
            if stix_object.get("revoked", False):
                continue  # skip revoked objects
            if stix_object.get("x_mitre_deprecated", False):
                continue  # skip deprecated objects

            # map attack ID to stix ID
            for reference in stix_object["external_references"]:
                if reference["source_name"] == "mitre-attack":
                    attackid_to_stixid[reference["external_id"]] = stix_object["id"]
    return attackid_to_stixid


def test_spreadsheet_names(spreadsheets):
    for attack_type in spreadsheets.keys():
        name = spreadsheets[attack_type].name
        assert name == f"veris-2-mappings-{attack_type}.xlsx"


def test_spreadsheet_contents(spreadsheets, veris_schema):
    groups_flag = "groups" in spreadsheets.keys()

    for attack_type in spreadsheets.keys():
        groups = False
        print(f"\t\t\t[+] checking document: {spreadsheets[attack_type].name}")
        attack_src = get_attack_objects(attack_type, "12.1", groups_flag)
        if attack_type == "groups":
            groups = True
            sheets = [get_sheet_by_name(spreadsheets[attack_type], "Actor.External.Motive")]
        else:
            sheets = get_sheets(spreadsheets[attack_type])
        
        for sheet, name in sheets:
            name = name.lower()
            print(f"\t\t\t[+] checking sheet: {name}")
            veris_path = None
        unique_per_veris_entry = {}
        fail_test = False

        for idx, row in sheet.iterrows():
            if row[0] is not numpy.nan:
                veris_path = f'{name}.{row[0]}'
                check_unique = True
            else:
                check_unique = False
            attack_technique = row[1]

            if attack_technique is numpy.nan:
                # Don't validate the attack_technique if the cell is blank (aka is numpy.nan)
                pass
            elif attack_technique not in attack_src:
                if groups:
                    print(f"[-] In Sheet '{name}', under '{veris_path}', "
                      f"the group ID '{attack_technique}' is invalid (revoked or deprecated)")
                else:
                    print(f"[-] In Sheet '{name}', under '{veris_path}', "
                        f"the technique ID '{attack_technique}' is invalid (revoked or deprecated)")
                fail_test = True

            if check_unique and veris_path in unique_per_veris_entry:
                print(f"[-] In Sheet '{name}', under '{veris_path}', "
                      f"the veris path is duplicated")
                fail_test = True

            if veris_path not in unique_per_veris_entry:
                unique_per_veris_entry[veris_path] = set()

            if attack_technique is numpy.nan:
                # Don't validate the attack_technique if the cell is blank (aka is numpy.nan)
                pass
            elif attack_technique not in unique_per_veris_entry[veris_path]:
                unique_per_veris_entry[veris_path].add(attack_technique)
            else:
                if groups:
                    print(f"[-] In Sheet '{name}', under '{veris_path}', "
                      f"the group ID '{attack_technique}' is duplicated")
                else:
                    print(f"[-] In Sheet '{name}', under '{veris_path}', "
                        f"the technique ID '{attack_technique}' is duplicated")
                fail_test = True

        print(f"\t\t\t[+] finished checking document: {spreadsheets[attack_type].name}\n")
        assert fail_test == False, f"Problems found in: {spreadsheets[attack_type].name}"
            




