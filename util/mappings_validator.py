# Copyright (c) 2021, MITRE Engenuity. Approved for public release.
# See LICENSE for complete terms

# pip install requests stix2

import argparse
import collections
import json
import pathlib

import requests
import stix2


def get_argparse():
    desc = "ATT&CK to VERIS Mappings Validator"
    argparser = argparse.ArgumentParser(description=desc)

    argparser.add_argument(
        "-mappings_location",
        type=str,
        default="../attack_veris_mappings.json",
        help="The ATT&CK release version to use.",
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
        "https://raw.githubusercontent.com/vz-risk/VCDB/master/vcdb-enum.json",
        verify=True,
    ).json()
    return veris_enum_dict

def get_stix2_data_source(attack_version):
    """Downloads ATT&CK knowledge base using the provided version"""
    stix_bundle = requests.get(
        f"https://raw.githubusercontent.com/mitre/cti/ATT%26CK-v{attack_version}/enterprise-attack/enterprise-attack.json",
        verify=True,
    ).json()
    ms_source = stix2.MemorySource(stix_data=stix_bundle["objects"])
    return ms_source


def get_technique_by_id(src, technique_id):
    """Get ATT&CK Technique by ID"""
    results = remove_revoked_deprecated(
        src.query([
            stix2.Filter("type", "=", "attack-pattern"),
            stix2.Filter("external_references.external_id", "=", technique_id),
        ])
    )

    # assert len(results) == 1, f"[-] Check entry with ID: {technique_id}, not found on knowledge base"
    if len(results) <= 0:
        # TODO: temporary section to be replaced by assert
        print(f"[-] Check entry with ID: {technique_id}, not found on knowledge base or it is deprecated/revoked")
        return None
    stix2_technique = results[0]

    return stix2_technique


def remove_revoked_deprecated(stix_objects):
    """Remove any revoked or deprecated objects from queries made to the data source"""
    # Note we use .get() because the property may not be present in the JSON data. The default is False
    # if the property is not set.
    return list(
        filter(
            lambda x: x.get("x_mitre_deprecated", False) is False and x.get("revoked", False) is False,
            stix_objects,
        )
    )


def get_parent_technique(technique_id):
    """Separates parent technique from sub technique TXXXX.YYY"""
    return technique_id.split(".")[0]


def flatten_dictionary(d, parent_key='', sep='$$'):
    """Given a highly nested dict structure, flatten it and compress keys"""
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten_dictionary(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def validate_mappings_metadata(mappings_location, attack_version, veris_version):
    """Checks for presence and correct metadata information in the mappings JSON file."""
    mappings_dict = get_mappings_file(mappings_location)

    # Checks presence of metadata key
    assert "metadata" in mappings_dict, "[-] No Metadata Found..."

    mappings_meta = mappings_dict["metadata"]

    # Checks metadata info matches the validator options
    assert attack_version == mappings_meta["attack_version"], f"[-] ATT&CK Version does not match JSON contents"
    assert veris_version == mappings_meta["veris_version"], f"[-] VERIS Version does not match JSON contents"


def validate_mapping_entries(mappings_location, attack_version):
    """Walks over forward and reverse mappings checking the ATT&CK entry is valid.
    1) The ATT&CK ID is correct 2) The ATT&CK name is correct 3) The VERIS path is correct"""
    mem_source = get_stix2_data_source(attack_version)
    mappings_dict = get_mappings_file(mappings_location)
    veris_enum = get_veris_enum()

    print("\t\t[+] VERIS to ATT&CK mappings check...")
    for key_full_path, property_value in flatten_dictionary(mappings_dict["veris_to_attack"]).items():
        veris_path = key_full_path.split("$$")[0:4]
        technique_id = key_full_path.split("$$")[4]
        property_name = key_full_path.split("$$")[5]

        if technique_id == "T0000" and property_name == "name":
            assert property_value == "INACTIVE"
            continue

        parent_technique = None
        stix2_technique = get_technique_by_id(mem_source, technique_id)
        if not stix2_technique:
            continue
        if stix2_technique.get("x_mitre_is_subtechnique", False) is True:
            parent_technique = get_technique_by_id(mem_source, get_parent_technique(technique_id))

        if parent_technique:
            technique_name = f"{parent_technique.name}: {stix2_technique.name}"
        else:
            technique_name = f"{stix2_technique.name}"

        if property_name == "name" and technique_name != property_value:
            # TODO: temporary section to be replaced by assert
            veris_full_key = ".".join(key_full_path.split("$$")[0:4])
            print(f"[-] Check entry with VERIS path: '{veris_full_key}', {technique_id} 'name' property does not match. '{technique_name}' != '{property_value}'")

        test_enum = veris_enum
        for veris_section in veris_path[0:3]:
            if veris_section in test_enum:
                test_enum = test_enum[veris_section]

        if veris_path[-1] not in test_enum:
            veris_full_key = ".".join(key_full_path.split("$$")[0:4])
            print(f"[-] Check entry with VERIS path: '{veris_full_key}', not a valid path")

    print("\t\t[+] ATT&CK to VERIS mappings check...")
    for technique_id, mapping in mappings_dict["attack_to_veris"].items():
        if technique_id == "T0000":
            assert mapping["name"] == "INACTIVE"
            continue

        parent_technique = None
        stix2_technique = get_technique_by_id(mem_source, technique_id)
        if not stix2_technique:
            continue
        if stix2_technique.get("x_mitre_is_subtechnique", False) is True:
            parent_technique = get_technique_by_id(mem_source, get_parent_technique(technique_id))

        if parent_technique:
            technique_name = f"{parent_technique.name}: {stix2_technique.name}"
        else:
            technique_name = f"{stix2_technique.name}"

        assert "name" in mapping, f"[-] Check entry with ID: {technique_id}, missing 'name' property"
        if technique_name != mapping["name"]:
            # TODO: temporary section to be replaced by assert
            print(f"[-] Check entry with ID: {technique_id}, 'name' property does not match. '{technique_name}' != '{mapping['name']}'")

        for veris_path in mapping["veris"]:
            veris_parts = veris_path.split(".")

            test_enum = veris_enum
            for veris_section in veris_parts[0:3]:
                if veris_section in test_enum:
                    test_enum = test_enum[veris_section]

            if veris_parts[-1] not in test_enum:
                print(f"[-] Check entry with VERIS path: '{veris_path}', not a valid path")


# TODO: Check that for each forward entry in the mappings a reverse mapping also exists.

if __name__ == "__main__":
    parser = get_argparse()
    args = parser.parse_args()

    print("[+] Starting Execution")
    print(f"[+] Mappings Location: {args.mappings_location}\tATT&CK Version: {args.attack_version}\tVERIS Version: {args.veris_version}")
    validate_mappings_metadata(args.mappings_location, args.attack_version, args.veris_version)
    print("\t[+] Metadata Validation passed")
    validate_mapping_entries(args.mappings_location, args.attack_version)
    print("\t[+] Mappings Validation passed")
    print("[+] Finished Execution")
