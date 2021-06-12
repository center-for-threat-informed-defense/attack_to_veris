import json
import pathlib
import uuid

import pandas
import requests
from colorama import Fore
from stix2.v20 import Bundle, Relationship
from tqdm import tqdm


def dict_lookup(lookup_dict, term):
    """:return item from dictionary if present. Exits otherwise"""
    if term not in lookup_dict:
        print(Fore.RED + f"ERROR: cannot find '{term}' in lookup dictionary...",  Fore.RESET)
        exit()
    return lookup_dict[term]


def parse_mappings(mappings_path, veris_entries, relationship_ids):
    """Parses the VERIS mappings and returns a STIX Bundle
    with relationship objects conveying the mappings in STIX format.

    :param mappings_path the filepath to the mappings TSV file
    :param veris_entries a stix2.Bundle representing veris framework STIX objects
    :param relationship_ids is a dict of format
        {relationship-source-id---relationship-target-id -> relationship-id} which
        maps relationships to desired STIX IDs
    :return stix2 Bundle
    """

    print("reading framework config...", end="", flush=True)
    # load the mapping config
    with pathlib.Path("input", "config.json").open("r", encoding="utf-8") as f:
        config = json.load(f)
        version = config["attack_version"]
        domain = config["attack_domain"]
    print("done")

    tqdm_format = "{desc}: {percentage:3.0f}% |{bar}| {elapsed}<{remaining}{postfix}"

    # load ATT&CK STIX data
    print("downloading ATT&CK data... ", end="", flush=True)
    attack_url = f"https://raw.githubusercontent.com/mitre/cti/ATT%26CK-v{version}/{domain}/{domain}.json"
    attack_data = requests.get(attack_url).json()["objects"]
    print("done")

    # build mapping of attack ID to stix ID
    attackid_to_stixid = {}
    for attack_object in tqdm(attack_data, desc=f"parsing v{version} {domain} data", bar_format=tqdm_format):
        if attack_object["type"] == "attack-pattern":
            if "external_references" not in attack_object:
                continue  # skip objects without IDs
            if attack_object.get("revoked", False):
                continue  # skip revoked objects
            if attack_object.get("x_mitre_deprecated", False):
                continue  # skip deprecated objects

            # map attack ID to stix ID
            attackid_to_stixid[attack_object["external_references"][0]["external_id"]] = attack_object["id"]

    # build mapping from a veris path to stix ID
    veris_path_to_stix_id = {}
    for sdo in tqdm(veris_entries.objects, desc="parsing veris", bar_format=tqdm_format):
        veris_path_to_stix_id[sdo["external_references"][0]["external_id"]] = sdo["id"]

    # build mapping relationships
    stix_relationships = {}
    mappings_df = pandas.read_csv(mappings_path, sep=",", keep_default_na=False, header=0)

    for index, row in tqdm(list(mappings_df.iterrows()), desc="parsing mappings", bar_format=tqdm_format):
        from_id = dict_lookup(veris_path_to_stix_id, row["VERIS PATH"])
        to_id = dict_lookup(attackid_to_stixid, row["TECHNIQUE ID"])
        joined_id = f"{from_id}---{to_id}"

        if joined_id in relationship_ids:
            relationship_id = relationship_ids[joined_id]
        else:
            relationship_id = f"relationship--{uuid.uuid4()}"

        # build the mapping relationship
        relationship = Relationship(
            id=relationship_id,
            source_ref=from_id,
            target_ref=to_id,
            relationship_type="related-to",
        )
        if joined_id not in stix_relationships:
            stix_relationships[joined_id] = relationship

    # construct and return the bundle with relationships
    return Bundle(*stix_relationships.values())
