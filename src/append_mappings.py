import argparse
import json
import pathlib

import requests
from stix2.v20 import Bundle


def save_bundle(bundle, path):
    """helper function to write a STIX bundle to file"""
    print(f"{'overwriting' if path.exists() else 'writing'} {path}... ", end="", flush=True)
    with path.open("w", encoding="utf-8") as outfile:
        outfile.write(bundle.serialize(pretty=False, ensure_ascii=False, indent=4, sort_keys=True))
    print("done!")


def append_mappings(attack_bundle, veris_bundle, mappings_bundle, allow_unmapped=False):
    """append the veris objects and mappings to the provided ATT&CK STIX Bundle. By default
    only the veris objects that are mapped to ATT&CK will appear in the output from this function
    enclosed in a STIX Bundle.
    """
    out_objects = attack_bundle.objects

    if allow_unmapped:
        # add all veris objects
        out_objects += veris_bundle.objects
    else:
        # add only veris objects which have associated mappings
        used_ids = set()
        for mapping in mappings_bundle.objects:
            used_ids.add(mapping["source_ref"])

        out_objects += list(filter(lambda sdo: sdo["id"] in used_ids, veris_bundle.objects))

    # add mappings
    out_objects += mappings_bundle.objects

    return Bundle(*out_objects, allow_custom=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="append veris framework objects and mappings with ATT&CK")
    parser.add_argument("-veris-objects",
                        dest="veris_objects",
                        help="filepath to the stix bundle representing the veris framework",
                        type=lambda path: pathlib.Path(path),
                        default=pathlib.Path("..", "frameworks", "veris", "stix", "veris135-enumerations.json"))
    parser.add_argument("-mappings",
                        dest="mappings",
                        help="filepath to the stix bundle mapping veris to ATT&CK",
                        type=lambda path: pathlib.Path(path),
                        default=pathlib.Path("..", "frameworks", "veris", "stix", "veris135-mappings.json"))
    parser.add_argument("-domain",
                        choices=["enterprise-attack", "mobile-attack", "pre-attack"],
                        help="the ATT&CK domain to append the veris work to",
                        default="enterprise-attack")
    parser.add_argument("-version",
                        dest="version",
                        help="which ATT&CK version to use",
                        default="9.0")
    parser.add_argument("--allow-unmapped",
                        dest="allow_unmapped",
                        action="store_true",
                        help="if flag is present, output bundle will include veris objects that don't map to "
                             "techniques. By default only veris objects that have technique mappings will be included",
                        default=False)
    parser.add_argument("-output",
                        help="filepath to write the output stix bundle to",
                        type=lambda path: pathlib.Path(path),
                        default=pathlib.Path("..", "frameworks", "veris", "stix", "veris135-enterprise-attack.json"))

    args = parser.parse_args()

    print("downloading ATT&CK data... ", end="", flush=True)
    attack_url = f"https://raw.githubusercontent.com/mitre/cti/ATT%26CK-v{args.version}/{args.domain}/{args.domain}.json"
    attack_data = Bundle(requests.get(attack_url).json()["objects"], allow_custom=True)
    print("done")

    print("loading veris framework... ", end="", flush=True)
    with args.veris_objects.open("r", encoding="utf-8") as f:
        veris_objects = Bundle(json.load(f)["objects"], allow_custom=True)
    print("done")

    print("loading mappings... ", end="", flush=True)
    with args.mappings.open("r", encoding="utf-8") as f:
        mappings = Bundle(json.load(f)["objects"])
    print("done")

    print("appending veris data... ", end="", flush=True)
    out_bundle = append_mappings(attack_data, veris_objects, mappings, args.allow_unmapped)
    print("done")

    save_bundle(out_bundle, args.output)
