import argparse
import json
import pathlib

from parse_mappings import parse_mappings
from parse_veris import parse_veris


def save_bundle(bundle, path):
    """Helper function to write a STIX bundle to a file"""
    print(f"{'overwriting' if path.exists() else 'writing'} {path}... ", end="", flush=True)
    with path.open("w", encoding="utf-8") as outfile:
        bundle.fp_serialize(outfile, pretty=False, ensure_ascii=False, sort_keys=True, indent=4)
    print("done!")


def main(in_enumerations=pathlib.Path("input", "veris135-enumerations.csv"),
         in_mappings=pathlib.Path("input", "veris135-mappings.csv"),
         out_enumerations=pathlib.Path("stix", "veris135-enumerations.json"),
         out_mappings=pathlib.Path("stix", "veris135-mappings.json"),
         config_location=pathlib.Path("input", "config.json")):
    """
    Parses the VERIS vocabulary entries and ATT&CK mappings and creates STIX2 Bundles.

    :param in_enumerations - csv file of VERIS enumeration entries
    :param in_mappings - csv file with mappings between VERIS and ATT&CK
    :param out_enumerations - output STIX bundle file for the controls.
    :param out_mappings - output STIX bundle file for the mappings.
    :return tuple with (out_enumerations, out_mappings)
    """

    # build control ID helper lookups so that STIX IDs don't get replaced on each rebuild
    veris_ids = {}

    if out_enumerations.exists():
        print("Found existing VERIS entries file...")
        # parse idMappings from existing output so that IDs don't change when regenerated
        with out_enumerations.open("r", encoding="utf-8") as f:
            bundle = json.load(f)

        for sdo in bundle["objects"]:
            from_id = sdo["external_references"][0]["external_id"]
            to_id = sdo["id"]
            veris_ids[from_id] = to_id

    else:
        print("Generating VERIS entries from scratch...")

    # build veris entries in STIX
    enumerations = parse_veris(
        in_enumerations,
        veris_ids,
        config_location,
    )

    # build mapping ID helper lookup so that STIX IDs don't get replaced on each rebuild
    mapping_relationship_ids = {}

    if out_mappings.exists():
        with out_mappings.open("r", encoding="utf-8") as f:
            bundle = json.load(f)

        for sdo in bundle["objects"]:
            from_id = f"{sdo['source_ref']}---{sdo['target_ref']}"
            to_id = sdo["id"]
            mapping_relationship_ids[from_id] = to_id

    # build veris mappings in STIX
    mappings = parse_mappings(
        in_mappings,
        enumerations,
        mapping_relationship_ids,
        config_location,
    )

    save_bundle(enumerations, out_enumerations)
    save_bundle(mappings, out_mappings)

    return out_enumerations, out_mappings


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parses VERIS, ATT&CK and produces mappings in STIX 2.0")
    parser.add_argument("-input-enumerations",
                        dest="in_enumerations",
                        help="csv file with VERIS entries",
                        type=lambda path: pathlib.Path(path),
                        default=pathlib.Path("input", "veris135-enumerations.csv"))
    parser.add_argument("-input-mappings",
                        dest="in_mappings",
                        help="csv file with mappings between VERIS and ATT&CK",
                        type=lambda path: pathlib.Path(path),
                        default=pathlib.Path("input", "veris135-mappings.csv"))
    parser.add_argument("-output-enumerations",
                        dest="out_enumerations",
                        help="output STIX bundle file for the veris entries.",
                        type=lambda path: pathlib.Path(path),
                        default=pathlib.Path("stix", "veris135-enumerations.json"))
    parser.add_argument("-output-mappings",
                        dest="out_mappings",
                        help="output STIX bundle file for the mappings.",
                        type=lambda path: pathlib.Path(path),
                        default=pathlib.Path("stix", "veris135-mappings.json"))
    parser.add_argument("-config-location",
                        dest="config_location",
                        help="filepath to the configuration for the framework",
                        type=lambda path: pathlib.Path(path),
                        default=pathlib.Path("input", "config.json"))

    args = parser.parse_args()

    main(**vars(args))
