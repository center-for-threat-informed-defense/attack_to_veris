# Copyright (c) 2021, MITRE Engenuity. Approved for public release.
# See LICENSE for complete terms.

import argparse
import json
import pathlib

import numpy
import pandas
import requests


def get_argparse():
    desc = "ATT&CK to VERIS Mappings Validator"
    argparser = argparse.ArgumentParser(description=desc)

    argparser.add_argument(
        "-config_location",
        type=lambda path: pathlib.Path(path),
        default=pathlib.Path("..", "frameworks", "veris", "input", "config.json"),
        help="The path to the config metadata location.",
    )

    argparser.add_argument(
        "-spreadsheet_location",
        type=lambda path: pathlib.Path(path),
        default=pathlib.Path("..", "frameworks", "veris", "veris-mappings.xlsx"),
        help="The path to the spreadsheet location.",
    )

    argparser.add_argument(
        "-attack_version",
        type=str,
        default="9.0",
        help="The ATT&CK release version to use.",
    )

    argparser.add_argument(
        "-veris_version",
        type=str,
        default="1.3.5",
        help="The VERIS release version to use.",
    )

    return argparser


def get_mappings_file(mappings_location):
    """Returns the ATT&CK VERIS mappings JSON file"""
    path_obj = pathlib.Path(mappings_location).resolve()
    with path_obj.open(encoding="utf-8") as f:
        return json.load(f)


def get_veris_enum():
    """Downloads the latest VERIS enum"""
    veris_enum_dict = requests.get(
        "https://raw.githubusercontent.com/vz-risk/VCDB/1.3.5/vcdb-labels.json",
        verify=True,
    ).json()
    return veris_enum_dict


def get_stix2_source(attack_version):
    """Downloads ATT&CK knowledge base using the provided version"""
    attackid_to_stixid = {}
    stix_bundle = requests.get(
        f"https://raw.githubusercontent.com/mitre/cti/ATT%26CK-v{attack_version}/"
        f"enterprise-attack/enterprise-attack.json",
        verify=True,
    ).json()

    for attack_object in stix_bundle["objects"]:
        if attack_object["type"] == "attack-pattern":
            if "external_references" not in attack_object:
                continue  # skip objects without IDs
            if attack_object.get("revoked", False):
                continue  # skip revoked objects
            if attack_object.get("x_mitre_deprecated", False):
                continue  # skip deprecated objects

            # map attack ID to stix ID
            attackid_to_stixid[attack_object["external_references"][0]["external_id"]] = attack_object["id"]

    return attackid_to_stixid


def validate_mappings_metadata(mappings_location, attack_version, veris_version):
    """Checks for presence and correct metadata information in the mappings JSON file."""
    mappings_dict = get_mappings_file(mappings_location)

    # Checks presence of metadata key
    assert mappings_dict, "[-] No Metadata Found..."

    # Checks metadata info matches the validator options
    assert attack_version == mappings_dict["attack_version"], f"[-] ATT&CK Version does not match JSON contents"
    assert veris_version == mappings_dict["veris_version"], f"[-] VERIS Version does not match JSON contents"


def validate_mapping_entries(spreadsheet_location, attack_version):
    """Walks over forward and reverse mappings checking the ATT&CK entry is valid.
    1) The ATT&CK ID is correct 2) The ATT&CK name is correct 3) The VERIS path is correct"""
    attack_source = get_stix2_source(attack_version)
    veris_enum = get_veris_enum()

    sheet1 = 'Action.Hacking.Variety'
    sheet2 = 'Action.Hacking.Vector'
    sheet3 = 'Action.Malware.Variety'
    sheet4 = 'Action.Malware.Vector'
    sheet5 = 'Action.Social.Variety'
    sheet6 = 'Attribute.Integrity.Variety'

    xls = pandas.ExcelFile(spreadsheet_location)
    df1 = pandas.read_excel(xls, sheet1)
    df2 = pandas.read_excel(xls, sheet2)
    df3 = pandas.read_excel(xls, sheet3)
    df4 = pandas.read_excel(xls, sheet4)
    df5 = pandas.read_excel(xls, sheet5)
    df6 = pandas.read_excel(xls, sheet6)

    sheets = [
        (df1, sheet1),
        (df2, sheet2),
        (df3, sheet3),
        (df4, sheet4),
        (df5, sheet5),
        (df6, sheet6),
    ]

    print("\t\t[+] VERIS to ATT&CK mappings check...")
    fail_test = False

    for sheet, name in sheets:
        name = name.lower()
        veris_path = None

        for idx, row in sheet.iterrows():
            if row[0] is not numpy.nan:
                veris_path = f'{name}.{row[0]}'
            attack_technique = row[1]

            if attack_technique not in attack_source:
                print(f"[-] In Sheet '{name}', under '{veris_path}', the technique ID '{attack_technique}' is invalid (revoked or deprecated)")
                fail_test = True

            try:
                axes, category, sub_category, veris_name = veris_path.split(".")
                veris_enum[axes][category][sub_category][veris_name]
            except (KeyError, ValueError):
                print(f"[-] In Sheet '{name}', the VERIS path '{veris_path}' is invalid")
                fail_test = True

    assert fail_test is False


if __name__ == "__main__":
    parser = get_argparse()
    args = parser.parse_args()

    print("[+] Starting Execution")
    print(f"[+] Mappings Location: {args.spreadsheet_location}\tATT&CK Version: {args.attack_version}\tVERIS Version: {args.veris_version}")
    validate_mappings_metadata(args.config_location, args.attack_version, args.veris_version)
    print("\t[+] Metadata Validation passed")
    validate_mapping_entries(args.spreadsheet_location, args.attack_version)
    print("\t[+] Mappings Validation passed")
    print("[+] Finished Execution")
