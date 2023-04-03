import argparse
import subprocess
import os
import pathlib


ROOT_DIR = pathlib.Path(__file__).parent.parent.parent.parent

def create_mappings(attack_types):
    for attack_type in attack_types:

        mappings_command = [
            "python", "-m", "veris.util.create_mappings",
            "-spreadsheet-location", pathlib.Path(ROOT_DIR, "mappings", "veris-1.3.7", "input", 
                attack_type, f"xlsx", f"veris-1_3_7-mappings-{attack_type}_v12.xlsx"),
            "-json-location", pathlib.Path(ROOT_DIR, "mappings", "veris-1.3.7", "input",
                attack_type, "json", f"veris-1_3_7-mappings-{attack_type}.json"),
            "-mappings-location", pathlib.Path(ROOT_DIR, "mappings", "veris-1.3.7", "input",
                attack_type, "csv", f"veris1_3_7-mappings-{attack_type}.csv"),
            "-veris-location", pathlib.Path(ROOT_DIR, "mappings", "veris-1.3.7", "input",
                attack_type, "csv", f"veris1_3_7-enumerations-{attack_type}.csv"),
            "-config-location", pathlib.Path(ROOT_DIR, "mappings", "veris-1.3.7", "input", "config.json"),
            "-veris-version", "1.3.7",
        ]

        subprocess_command = [
            "python", "-m",  "veris.parse.parse",
            "-input-enumerations", pathlib.Path(ROOT_DIR, "mappings", "veris-1.3.7", "input",
                attack_type, "csv", f"veris1_3_7-enumerations-{attack_type}.csv"), 
            "-input-mappings", pathlib.Path(ROOT_DIR, "mappings", "veris-1.3.7", "input",
                attack_type, "csv", f"veris1_3_7-mappings-{attack_type}.csv"), 
            "-output-enumerations", pathlib.Path(ROOT_DIR, "mappings", "veris-1.3.7", "stix", attack_type, 
                f"veris1_3_7-enumerations-{attack_type}.json"), 
            "-output-mappings", pathlib.Path(ROOT_DIR, "mappings", "veris-1.3.7", "stix", attack_type, 
                f"veris1_3_7-mappings-{attack_type}.json"),
            "-config-location", pathlib.Path(ROOT_DIR, "mappings", "veris-1.3.7", "input", "config.json"),
            "-attack-domain", f"{attack_type}-attack",
        ]

        if attack_type == "groups":
            mappings_command.append("-groups")
            subprocess_command.append("-groups")
        else:
            subprocess_command.append("-attack-domain")
            subprocess_command.append(f"{attack_type}-attack")
        
        subprocess.run(mappings_command)
        subprocess.run(subprocess_command)

def create_layers(attack_types):
    for attack_type in attack_types:
        if attack_type == "groups":
            subprocess.run([
                "python", "-m", "veris.util.groups_navigator_layers"
            ])
        else:
            subprocess.run([
                "python", "-m", "veris.util.mappings_to_heatmaps",
                "-veris-objects", pathlib.Path(ROOT_DIR, "mappings", "veris-1.3.7", "stix", attack_type, 
                    f"veris1_3_7-enumerations-{attack_type}.json"),
                "-mappings", pathlib.Path(ROOT_DIR, "mappings", "veris-1.3.7", "stix", attack_type, 
                    f"veris1_3_7-mappings-{attack_type}.json"),
                "-domain", f"{attack_type}-attack",
                "-version", "12.1",
                "-output", pathlib.Path(ROOT_DIR, "mappings", "veris-1.3.7", "layers", attack_type),
                "-clear", 
                "-build-directory"
            ])


def main():
    args = _parse_args()

    if args.task == "mappings":
        if args.attack_type == "all":
            create_mappings(["enterprise", "ics", "mobile", "groups"])
        else:
            create_mappings([args.attack_type])
    elif args.task == "layers":
        if args.attack_type == "all":
            create_layers(["enterprise", "ics", "mobile", "groups"])
        else:
            create_layers([args.attack_type])



def _parse_args():
    parser = argparse.ArgumentParser(description="Create the mappings and stix data")
    parser.add_argument("-attack-type",
                        dest="attack_type",
                        choices=["all", "enterprise", "ics", "mobile", "groups"],
                        help="What attack type do you want to generate.",
                        type=str,
                        default="all",
                        )
    parser.add_argument("-task",
                        dest="task",
                        choices=["mappings", "layers"],
                        help="Create new mappings, or generate navigator layers based on existing mappings data",
                        type=str,
                        default="mappings")
    return parser.parse_args()

if __name__ == "__main__":
    main()