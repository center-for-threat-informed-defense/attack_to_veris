import argparse
import json
import pathlib

import pandas
import requests
from colorama import Fore
from stix2.v20 import Bundle


def mappings_to_dataframe(attack_bundle, veris_bundle, mappings_bundle):
    """Return a pandas dataframe listing the mappings in mappings_bundle"""
    rows = []
    for mapping in mappings_bundle.objects:
        veris_object = veris_bundle.get(mapping.source_ref)
        if not veris_object:
            print(Fore.RED + f"ERROR: cannot find object with ID {mapping.source_ref} in controls bundle" + Fore.RESET)
            exit()
        else:
            veris_object = veris_object[0]

        technique = attack_bundle.get(mapping.target_ref)
        if not technique:
            print(Fore.RED + f"ERROR: cannot find object with ID {mapping.target_ref} in ATT&CK bundle" + Fore.RESET)
            exit()
        else:
            technique = technique[0]

        rows.append(
            {
                "veris path": veris_object["external_references"][0]["external_id"],
                "veris name": veris_object["name"],
                "mapping type": mapping["relationship_type"],
                "technique ID": technique["external_references"][0]["external_id"],
                "technique name": technique["name"],
                "mapping description": mapping["description"] if "description" in mapping else "",
            }
        )

    return pandas.DataFrame(rows)


def get_argparse():
    parser = argparse.ArgumentParser(description="List mappings in human readable formats")
    parser.add_argument("-veris-objects",
                        dest="veris_objects",
                        help="filepath to the STIX Bundle representing the veris framework",
                        type=lambda path: pathlib.Path(path),
                        default=pathlib.Path("..", "frameworks", "veris", "stix", "veris135-enumerations.json"))
    parser.add_argument("-mappings",
                        dest="mappings",
                        help="filepath to the STIX Bundle that contains mappings from VERIS to ATT&CK",
                        type=lambda path: pathlib.Path(path),
                        default=pathlib.Path("..", "frameworks", "veris", "stix", "veris135-mappings.json"))
    parser.add_argument("-domain",
                        dest="domain",
                        help="which ATT&CK domain to use",
                        default="enterprise-attack")
    parser.add_argument("-version",
                        dest="version",
                        help="which ATT&CK version to use",
                        default="9.0")
    parser.add_argument("-output",
                        help=f"filepath to write the output mappings to. Output format will be inferred "
                             f"from the extension. Allowed extensions: {allowed_extension_list}",
                        type=lambda path: pathlib.Path(path),
                        default=pathlib.Path("..", "frameworks", "veris", "veris-mappings.md"))
    return parser


if __name__ == "__main__":
    # extension to df export function name
    extension_to_pd_export = {
        "xlsx": "to_excel",
        "csv": "to_csv",
        "html": "to_html",
        "md": "to_markdown"
    }
    allowed_extension_list = ", ".join(extension_to_pd_export.keys())
    parser = get_argparse()
    args = parser.parse_args()

    extension = args.output.name.split(".")[-1]
    if extension not in extension_to_pd_export:
        print(Fore.RED + f"ERROR: Unknown output extension \"{extension}\", "
                         f"please make sure your output extension is one of: {allowed_extension_list}", Fore.RESET)
        exit()

    print("downloading ATT&CK data... ", end="", flush=True)
    url = f"https://raw.githubusercontent.com/mitre/cti/ATT%26CK-v{args.version}/{args.domain}/{args.domain}.json"
    attack_data = Bundle(requests.get(url, verify=True).json()["objects"], allow_custom=True)
    print("done")

    print("loading veris framework... ", end="", flush=True)
    with open(args.veris_objects, "r") as f:
        veris_objects = Bundle(json.load(f)["objects"], allow_custom=True)
    print("done")

    print("loading mappings... ", end="", flush=True)
    with open(args.mappings, "r") as f:
        mappings = Bundle(json.load(f)["objects"])
    df = mappings_to_dataframe(attack_data, veris_objects, mappings)
    print("done")

    print(f"writing {args.output}...", end="", flush=True)
    if extension in ["md"]:
        # md doesn't support index=False and requires a stream and not a path
        with open(args.output, "w") as f:
            getattr(df, extension_to_pd_export[extension])(f)
    else:
        getattr(df, extension_to_pd_export[extension])(args.output, index=False)
    print("done")
