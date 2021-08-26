# Copyright (c) 2021, MITRE Engenuity. Approved for public release.
# See LICENSE for complete terms.

import argparse
import json
import pathlib

import numpy
import requests

from src.create_mappings import get_sheets, get_sheet_by_name


def get_argparse():
    desc = "ATT&CK to VERIS Mappings Validator"
    argparser = argparse.ArgumentParser(description=desc)

    argparser.add_argument(
        "-config-location",
        dest="config_location",
        type=lambda path: pathlib.Path(path),
        default=pathlib.Path("..", "frameworks", "veris", "input", "config.json"),
        help="The path to the config metadata location.",
    )

    argparser.add_argument(
        "-spreadsheet-location",
        dest="spreadsheet_location",
        type=lambda path: pathlib.Path(path),
        default=pathlib.Path("..", "frameworks", "veris", "veris-mappings.xlsx"),
        help="The path to the spreadsheet mappings location.",
    )

    argparser.add_argument(
        "-json-location",
        dest="json_location",
        type=lambda path: pathlib.Path(path),
        default=pathlib.Path("..", "frameworks", "veris", "veris-mappings.json"),
        help="The path to the JSON mappings location.",
    )

    argparser.add_argument(
        "-attack-version",
        dest="attack_version",
        type=str,
        default="9.0",
        help="The ATT&CK release version to use.",
    )

    argparser.add_argument(
        "-veris-version",
        dest="veris_version",
        type=str,
        default="1.3.5",
        help="The VERIS release version to use.",
    )

    argparser.add_argument(
        "-metadata-version",
        dest="metadata_version",
        type=str,
        default="1.9",
        help="The Metadata version to check against.",
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


def validate_json_mappings_metadata(mappings_location, attack_version, veris_version, metadata_version):
    """Checks for presence and correct metadata information in the mappings JSON file."""
    mappings_dict = get_mappings_file(mappings_location)

    # Checks presence of metadata key
    assert mappings_dict, "[-] No Metadata Found..."

    if "metadata" in mappings_dict:
        mappings_dict = mappings_dict["metadata"]

    # Checks metadata info matches the validator options
    assert attack_version == mappings_dict["attack_version"], "[-] ATT&CK Version does not match JSON contents"
    assert veris_version == mappings_dict["veris_version"], "[-] VERIS Version does not match JSON contents"
    assert metadata_version == mappings_dict["mappings_version"], "[-] Metadata Version does not match JSON contents"


def validate_spreadsheet_mappings_metadata(spreadsheet_location, attack_version, veris_version, metadata_version):
    """Checks for presence and correct metadata information in the mappings spreadsheet."""
    sheet_data = get_sheet_by_name(spreadsheet_location, "Metadata")

    # Checks presence of metadata key
    assert sheet_data.empty is False, "[-] No Metadata Found..."

    for idx, row in sheet_data.iterrows():
        # Checks metadata info matches the validator options
        # Need to track specific rows/cells to make the chec
        if idx == 6:
            test_attack_version, test_attack_version_value = row[3], row[5]
            assert "ATT&CK version" == test_attack_version,\
                "[-] Spreadsheet contents does not match ATT&CK version cell"
            assert attack_version == str(test_attack_version_value),\
                "[-] ATT&CK Version does not match Spreadsheet contents"
        if idx == 7:
            test_veris_version, test_veris_version_value = row[3], row[5]
            assert "VERIS version" == test_veris_version,\
                "[-] Spreadsheet contents does not match VERIS version cell"
            assert veris_version == str(test_veris_version_value),\
                "[-] VERIS Version does not match Spreadsheet contents"
        if idx == 8:
            test_mappings_version, test_mappings_version_value = row[3], row[5]
            assert "Mapping version" == test_mappings_version,\
                "[-] Spreadsheet contents does not match Mappings version cell"
            assert metadata_version == str(test_mappings_version_value),\
                "[-] Mappings version does not match Spreadsheet contents"
        if idx == 9:
            text_spreadsheet_version, test_spreadsheet_version_value = row[3], row[5]
            assert "Spreadsheet version" == text_spreadsheet_version,\
                "[-] Spreadsheet contents does not match Spreadsheet version cell"
            assert metadata_version == str(test_spreadsheet_version_value),\
                "[-] Spreadsheet version does not match Spreadsheet contents "


def validate_mapping_entries(spreadsheet_location, attack_version):
    """Walks over forward and reverse mappings checking the ATT&CK entry is valid.
    1) The ATT&CK ID is correct 2) The ATT&CK name is correct 3) The VERIS path is correct"""
    attack_source = get_stix2_source(attack_version)
    veris_enum = get_veris_enum()
    sheets = get_sheets(spreadsheet_location)

    print("\t\t[+] VERIS to ATT&CK mappings check...")
    fail_test = False

    for sheet, name in sheets:
        name = name.lower()
        print(f"\t\t\t[+] checking sheet: {name}")
        veris_path = None
        unique_per_veris_entry = {}

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
            elif attack_technique not in attack_source:
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
                print(f"[-] In Sheet '{name}', under '{veris_path}', "
                      f"the technique ID '{attack_technique}' is duplicated")
                fail_test = True

            try:
                axes, category, sub_category, veris_name = veris_path.split(".")
                extracted_value = veris_enum[axes][category][sub_category][veris_name]
                assert extracted_value
            except (KeyError, ValueError):
                print(f"[-] In Sheet '{name}', the VERIS path '{veris_path}' is invalid")
                fail_test = True

    assert fail_test is False


if __name__ == "__main__":
    parser = get_argparse()
    args = parser.parse_args()

    print("[+] Starting Execution")
    print(f"[+] Mappings Location: {args.spreadsheet_location}\t"
          f"ATT&CK Version: {args.attack_version}\t"
          f"VERIS Version: {args.veris_version}")
    validate_json_mappings_metadata(
        args.config_location, args.attack_version, args.veris_version, args.metadata_version
    )
    validate_json_mappings_metadata(
        args.json_location, args.attack_version, args.veris_version, args.metadata_version
    )
    validate_spreadsheet_mappings_metadata(
        args.spreadsheet_location, args.attack_version, args.veris_version, args.metadata_version
    )
    print("\t[+] Metadata Validation passed")
    validate_mapping_entries(args.spreadsheet_location, args.attack_version)
    print("\t[+] Mappings Validation passed")
    print("[+] Finished Execution")
