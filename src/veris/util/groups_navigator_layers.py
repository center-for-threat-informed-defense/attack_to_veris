import argparse
import requests
import tempfile
import json
import pathlib
import os
from mitreattack.stix20 import MitreAttackData


def get_technique(attack_id, mapped_veris):
    """create a technique for a layer"""
    return {
        "techniqueID": attack_id,
        "score": len(mapped_veris),  # count of mapped veris entries
        "comment": f"Related to {', '.join(sorted(mapped_veris))}",  # list of mapped veris entries
    }


def create_layer(name, description, domain, techniques, version):
    """create a Layer"""
    min_mappings = min(map(lambda t: t["score"], techniques)) if len(techniques) > 0 else 0
    max_mappings = max(map(lambda t: t["score"], techniques)) if len(techniques) > 0 else 100
    gradient = ["#ffe766", "#ffaf66"]
    # check if all the same count of mappings
    if max_mappings - min_mappings == 0:
        min_mappings = 0  # set low end of gradient to 0
        gradient = ["#ffffff", "#ffaf66"]


    # convert version to just major version
    if version.startswith("v"):
        version = version[1:]
    version = version.split(".")[0]

    return {
        "name": name,
        "versions": {
            "navigator": "4.8.0",
            "layer": "4.4",
            "attack": version
        },
        "sorting": 3,  # descending order of score
        "description": description,
        "domain": domain,
        "techniques": techniques,
        "gradient": {
            "colors": gradient,
            "minValue": min_mappings,
            "maxValue": max_mappings
        },
    }


def get_technique_list(techniques, mappings_data):
    technique_list = []
    for t in techniques:
        technique = t["object"]
        for reference in technique.external_references:
            if reference["source_name"] == "mitre-attack":
                tid = reference.external_id
        if tid in mappings_data.keys():
            technique_list.append(get_technique(tid, mappings_data[tid]["veris"]))

    return technique_list


def load_mitre_data(version, domain):
    enterprise_url = f"https://raw.githubusercontent.com/mitre/cti/ATT%26CK-v{version}/{domain}-attack/{domain}-attack.json"

    temp_file = tempfile.NamedTemporaryFile(mode="w+")

    print("Downloading Enterprise ATT&CK Data")
    json.dump(requests.get(enterprise_url, verify=True).json(), temp_file)
    temp_file.flush()
    print("Done")


    print("Loading ATT&CK Data...")
    result = MitreAttackData(temp_file.name)
    temp_file.close()

    return result


def generate_group_id_mappings(attack_data):
    mappings = {}
    groups = attack_data.get_groups(remove_revoked_deprecated=True)
    for group in groups:
        for reference in group["external_references"]:
            if reference["source_name"] == "mitre-attack":
                mappings[group.id] = reference["external_id"]

    return mappings


def parse_mappings(mappings_dir, attack_type):
    file_path = mappings_dir / attack_type / "json" / f"veris-1_3_7-mappings-{attack_type}.json"

    with open(file_path, "r") as file:
        data = json.loads(file.read())["attack_to_veris"]

    return data


def write_layers(output_dir, attack_type, layers_data):
    output_dir_path = output_dir / attack_type

    for name, l in layers_data.items():
        for veris_type in l["types"]:
            if not os.path.exists(output_dir_path / veris_type):
                os.makedirs(f"{output_dir_path}/{veris_type}")

            with open(output_dir_path / veris_type / f"{name}.json", "w") as outfile:
                json.dump(l["layers"], outfile)



def main():
    args = _parse_args()
    attack_types = []

    if args.attack_type == "all":
        attack_types = ["enterprise", "ics", "mobile"]
    else:
        attack_types.append(args.attack_type)

    group_mapped_data = parse_mappings(args.mappings_dir, "groups")

    for attack_type in attack_types:
        layers_data = {}
        attack_data = load_mitre_data(args.version, attack_type)

        group_id_mappings = generate_group_id_mappings(attack_data)
        attack_mapped_data = parse_mappings(args.mappings_dir, "enterprise")

        for id, name in group_id_mappings.items():
            if name not in group_mapped_data.keys():
                continue

            group_techniques = get_technique_list(attack_data.get_techniques_used_by_group(id), attack_mapped_data)

            veris_types = [x.split(".")[-1] for x in group_mapped_data[name]["veris"]]

            layers = create_layer(
                                    f"{name} overview",
                                    f"Veris entries for group {name}",
                                    f"{attack_type}-attack",
                                    group_techniques,
                                    args.version
                                )
            layers_data[name] = {
                                    "layers": layers,
                                    "types": veris_types
                                }
            
        write_layers(args.output_dir, attack_type, layers_data)


def _parse_args():
    ROOT_DIR = pathlib.Path(__file__).parent.parent.parent.parent

    parser = argparse.ArgumentParser(description="Create ATT&CK Navigator layers from VERIS mappings for group data")

    parser.add_argument("-mappings",
                        dest="mappings_dir",
                        help="Path to the groups mappings directory",
                        type=pathlib.Path,
                        default=pathlib.Path(ROOT_DIR, "mappings", "veris-1.3.7", "input")
                        )
    parser.add_argument("-attack-type",
                        dest="attack_type",
                        choices=["all", "enterprise", "ics", "mobile"],
                        help="What attack type do you want to generate.",
                        type=str,
                        default="all",
                        )
    parser.add_argument("-output",
                        dest="output_dir",
                        help="folder to write output layers to",
                        type=pathlib.Path,
                        default=pathlib.Path(ROOT_DIR, "mappings", "veris-1.3.7", "layers", "groups"),
                        )
    parser.add_argument("-version",
                        dest="version",
                        help="The version fo attack to get group data from",
                        default="12.1",
                        )
    
    return parser.parse_args()


if __name__ == "__main__":
    main()