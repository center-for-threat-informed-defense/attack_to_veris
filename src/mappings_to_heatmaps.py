import argparse
import json
import pathlib
import re
import shutil

import requests
import urllib.parse
from stix2 import Filter, MemoryStore


def technique(attack_id, mapped_veris):
    """create a technique for a layer"""
    return {
        "techniqueID": attack_id,
        "score": len(mapped_veris),  # count of mapped veris entries
        "comment": f"Related to {', '.join(sorted(mapped_veris))}",  # list of mapped veris entries
    }


def layer(name, description, domain, techniques, version):
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
            "navigator": "4.3",
            "layer": "4.2",
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


def parse_family_data(veris_objects):
    """ingest veris data to return family_id_to_veris_entries mapping and family_id_to_name mapping"""
    id_to_family = re.compile(r"(\w+).*")

    family_id_to_veris_entries = {}  # family ID to veris object
    family_id_to_name = {}
    for veris_object in veris_objects.query([Filter("type", "=", "attack-pattern")]):
        # parse family ID from veris external ID
        family_id = id_to_family.search(veris_object["external_references"][0]["external_id"]).groups()[0]
        if family_id not in family_id_to_veris_entries:
            family_id_to_veris_entries[family_id] = [veris_object]
        else:
            family_id_to_veris_entries[family_id].append(veris_object)
        # parse family name if possible, or just use family ID if not
        if "x_mitre_family" in veris_object:
            family_id_to_name[family_id] = veris_object["x_mitre_family"]
        else:
            family_id_to_name[family_id] = family_id

    return family_id_to_veris_entries, family_id_to_name, id_to_family


def to_technique_list(veris_objects, mappings, attack_data, family_id_to_veris_entries, family_id_to_name,
                      id_to_family):
    """take a veris ms, a mappings ms, and attack_data ms
    return a list of Techniques where the score is the number of veris that map to the technique"""

    technique_to_mapped_veris_entry = {}
    for mapping in mappings.query():
        # source_ref is the veris object in veris_objects
        if not veris_objects.get(mapping["source_ref"]):
            continue  # mapping not relevant to this list of veris objects

        veris_id = veris_objects.get(mapping["source_ref"])["external_references"][0]["external_id"]
        # target_ref is the technique in attack_data
        attack_id = attack_data.get(mapping["target_ref"])["external_references"][0]["external_id"]
        # build the mapping
        if attack_id in technique_to_mapped_veris_entry:
            technique_to_mapped_veris_entry[attack_id].append(veris_id)
        else:
            technique_to_mapped_veris_entry[attack_id] = [veris_id]

    # collapse families where all veris objects are mapped; list just the family identifier
    for id in technique_to_mapped_veris_entry:
        veris_ids = technique_to_mapped_veris_entry[id]

        # Group mappings for this technique according to the family
        families = {}
        for veris_id in veris_ids:
            family_id = id_to_family.search(veris_id).groups()[0]
            if family_id not in families:
                families[family_id] = {veris_id}  # new set
            else:
                families[family_id].add(veris_id)  # add to set

        collapsed_veris_objects = []
        for family_id in families:
            family_set = families[family_id]
            entries_in_family = set(
                map(lambda c: c["external_references"][0]["external_id"], family_id_to_veris_entries[family_id]))
            if family_set == entries_in_family:
                collapsed_veris_objects.append(f"all '{family_id_to_name[family_id]}' veris entries")
            else:
                collapsed_veris_objects += veris_ids
        technique_to_mapped_veris_entry[id] = collapsed_veris_objects

    # remove duplicate mappings
    for id in technique_to_mapped_veris_entry:
        technique_to_mapped_veris_entry[id] = list(set(technique_to_mapped_veris_entry[id]))

    # transform to techniques
    return [technique(id, technique_to_mapped_veris_entry[id]) for id in technique_to_mapped_veris_entry]


def get_framework_overview_layers(veris_objects, mappings, attack_data, domain, framework_name, version):
    """ingest mappings, veris objects and attack_data, and return an array of json layers according to the veris axes"""
    # build list of veris axes
    family_id_to_veris_entries, family_id_to_name, id_to_family = parse_family_data(veris_objects)

    out_layers = [
        {
            "outfile": pathlib.Path(f"{framework_name}-overview.json"),
            "layer": layer(
                f"{framework_name} overview",
                f"{framework_name} heatmap overview of veris mappings, scores are the number of associated entries",
                domain,
                to_technique_list(veris_objects, mappings, attack_data, family_id_to_veris_entries, family_id_to_name,
                                  id_to_family),
                version,
            )
        }
    ]

    for family_id in family_id_to_veris_entries:
        veris_family = MemoryStore(stix_data=family_id_to_veris_entries[family_id])
        techniques_in_family = to_technique_list(veris_family, mappings, attack_data, family_id_to_veris_entries,
                                                 family_id_to_name, id_to_family)
        if len(techniques_in_family) > 0:  # don't build heatmaps with no mappings
            # build family overview mapping
            out_layers.append({
                "outfile": pathlib.Path("by_axes", family_id_to_name[family_id].replace(" ", "_").replace("/", "_"),
                                        f"{family_id}-overview.json"),
                "layer": layer(
                    f"{family_id_to_name[family_id]} overview",
                    f"{framework_name} heatmap for entries in the {family_id_to_name[family_id]} axes, scores are the number of associated entries",
                    domain,
                    techniques_in_family,
                    version
                )
            })

            # build layer for each veris object
            for veris_object in family_id_to_veris_entries[family_id]:
                veris_ms = MemoryStore(stix_data=veris_object)
                veris_id = veris_object["external_references"][0]["external_id"]
                techniques_mapped_to_veris = to_technique_list(veris_ms, mappings, attack_data,
                                                               family_id_to_veris_entries, family_id_to_name,
                                                               id_to_family)

                # don't build heatmaps with no mappings
                if len(techniques_mapped_to_veris) > 0:
                    out_layers.append({
                        "outfile": pathlib.Path("by_axes", family_id_to_name[family_id].replace(" ", "_"),
                                                f"{'_'.join(veris_id.split(' ')).replace('/', '_')}.json"),
                        "layer": layer(
                            f"{veris_id} mappings",
                            f"{framework_name} {veris_id} mappings",
                            domain,
                            techniques_mapped_to_veris,
                            version
                        )
                    })

    return out_layers


def get_layers_by_property(veris_objects, mappings, attack_data, domain, framework_name, x_mitre, version):
    """get layers grouping the mappings according to values of the given property"""
    property_name = x_mitre.split("x_mitre_")[1]  # remove prefix

    family_id_to_veris_entries, family_id_to_name, id_to_family = parse_family_data(veris_objects)

    # group veris objects by the property
    property_value_to_veris = {}

    def add_to_dict(value, veris_object):
        if value in property_value_to_veris:
            property_value_to_veris[value].append(veris_object)
        else:
            property_value_to_veris[value] = [veris_object]

    # iterate through veris objects, grouping by property
    is_list_type = False
    for veris_object in veris_objects.query([Filter("type", "=", "attack-pattern")]):
        value = veris_object.get(x_mitre)
        if not value:
            continue
        if isinstance(value, list):
            is_list_type = True
            for v in value:
                add_to_dict(v, veris_object)
        else:
            add_to_dict(value, veris_object)

    out_layers = []
    for value in property_value_to_veris:
        # map veris for the corresponding values
        veris_values = MemoryStore(stix_data=property_value_to_veris[value])
        techniques = to_technique_list(veris_values, mappings, attack_data, family_id_to_veris_entries,
                                       family_id_to_name, id_to_family)
        if len(techniques) > 0:
            # build layer for this technique set
            out_layers.append({
                "outfile": pathlib.Path(f"by_{property_name}", f"{value}.json"),
                "layer": layer(
                    f"{property_name}={value} mappings",
                    f"techniques where the {property_name} of associated veris entries {'includes' if is_list_type else 'is'} {value}",
                    domain,
                    techniques,
                    version
                )
            })

    return out_layers


def get_x_mitre(ms, type="attack-pattern"):
    """return a list of all x_mitre_ properties defined on the given type"""
    keys = set()
    for obj in ms.query([Filter("type", "=", type)]):
        for key in obj:
            if key.startswith("x_mitre_"):
                keys.add(key)
    return keys


def get_argparse():
    parser = argparse.ArgumentParser(description="Create ATT&CK Navigator layers from VERIS mappings")
    parser.add_argument("-framework",
                        help="the name of the framework",
                        default="veris")
    parser.add_argument("-veris-objects",
                        dest="veris_objects",
                        help="filepath to the STIX Bundle representing the VERIS framework",
                        type=lambda path: pathlib.Path(path),
                        default=pathlib.Path("..", "frameworks", "veris", "stix", "veris135-enumerations.json"))
    parser.add_argument("-mappings",
                        dest="mappings",
                        help="filepath to the STIX Bundle mappings from VERIS to ATT&CK",
                        type=lambda path: pathlib.Path(path),
                        default=pathlib.Path("..", "frameworks", "veris", "stix", "veris135-mappings.json"))
    parser.add_argument("-domain",
                        choices=["enterprise-attack"],
                        help="the domain of ATT&CK to visualize",
                        default="enterprise-attack")
    parser.add_argument("-version",
                        dest="version",
                        help="which ATT&CK version to use",
                        default="9.0")
    parser.add_argument("-output",
                        help="folder to write output layers to",
                        type=lambda path: pathlib.Path(path),
                        default=pathlib.Path("..", "frameworks", "veris", "layers"))
    parser.add_argument("--clear",
                        action="store_true",
                        help="if flag specified, will remove the contents the output folder before writing layers")
    parser.add_argument("--build-directory",
                        dest="build_dir",
                        action="store_true",
                        help="if flag specified, will build a markdown file listing the output files "
                             "for easy access in the Navigator")
    return parser


if __name__ == "__main__":
    parser = get_argparse()
    args = parser.parse_args()

    print("downloading ATT&CK data... ", end="", flush=True)
    attack_url = f"https://raw.githubusercontent.com/mitre/cti/ATT%26CK-v{args.version}/{args.domain}/{args.domain}.json"
    attack_data = MemoryStore(stix_data=requests.get(attack_url).json()["objects"])
    print("done")

    print("loading veris framework... ", end="", flush=True)
    with open(args.veris_objects, "r") as f:
        veris_objects = MemoryStore(stix_data=json.load(f)["objects"], allow_custom=True)
    print("done")

    print("loading mappings... ", end="", flush=True)
    with open(args.mappings, "r") as f:
        mappings = MemoryStore(stix_data=json.load(f)["objects"])
    print("done")

    print("generating layers... ", end="", flush=True)
    layers = get_framework_overview_layers(veris_objects, mappings, attack_data, args.domain, args.framework,
                                           args.version)
    for p in get_x_mitre(veris_objects):  # iterate over all custom properties as potential layer-generation material
        if p == "x_mitre_family":
            continue
        layers += get_layers_by_property(veris_objects, mappings, attack_data, args.domain, args.framework, p,
                                         args.version)
    print("done")

    if args.clear:
        print("clearing layers directory...", end="", flush=True)
        shutil.rmtree(args.output)
        print("done")

    print("writing layers... ", end="", flush=True)
    for layer in layers:
        # make path if it doesn't exist
        layer_dir = pathlib.Path(args.output, layer["outfile"]).parent
        if not layer_dir.exists():
            layer_dir.mkdir(parents=True)
        # write layer
        with pathlib.Path(args.output, layer["outfile"]).open("w", encoding="utf-8") as f:
            json.dump(layer["layer"], f)
    print("done")
    if args.build_dir:
        print("writing layer directory markdown... ", end="", flush=True)

        md_file_lines = [
            "# ATT&CK Navigator Layers",
            "",
            f"The following [ATT&CK Navigator](https://github.com/mitre-attack/attack-navigator/) layers represent the mappings from ATT&CK to {args.framework.upper()}:",
            ""
        ]  # "" is an empty line
        prefix = f"https://raw.githubusercontent.com/center-for-threat-informed-defense/attack_to_veris/main/frameworks"
        nav_prefix = f"https://mitre-attack.github.io/attack-navigator/#layerURL="
        for layer in layers:

            path_parts = layer["outfile"].parts
            depth = len(path_parts) - 1  # how many subdirectories deep is it?
            layer_name = layer['layer']['name']
            if layer_name.endswith("overview"):
                depth = max(0, depth - 1)  # overviews get un-indented
            path = [prefix] + [args.framework, "layers"] + list(path_parts)
            path = "/".join(path)
            encodedPath = urllib.parse.quote(path, safe='~()*!.\'')  # encode the url for the query string
            md_file_lines.append(
                f"{'    ' * depth}- {layer_name} ( [download]({path}) | [view]({nav_prefix}{encodedPath}) )")
        with pathlib.Path(args.output, "README.md").open("w", encoding="utf-8") as f:
            f.write("\n".join(md_file_lines))

        print("done")
