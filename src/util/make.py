import argparse
import subprocess
import pathlib

ROOT_DIR = pathlib.Path(pathlib.Path(__file__).parent.parent)

def create_mappings(attack_types):
    for attack_type in attack_types:
        
        subprocess.run([
            "python", "-m", "util.create_mappings",
            "-spreadsheet-location", pathlib.Path(ROOT_DIR, "mappings", attack_type, 
                f"xlsx", f"veris-2-mappings-{attack_type}.xlsx"),
            "-json-location", pathlib.Path(ROOT_DIR, "mappings", attack_type, "json", 
                f"veris-2-mappings-{attack_type}.json"),
            "-mappings-location", pathlib.Path(ROOT_DIR, "mappings", attack_type, "csv", 
                f"veris137-mappings-{attack_type}.csv"),
            "-veris-location", pathlib.Path(ROOT_DIR, "mappings", attack_type, "csv", 
                f"veris137-enumerations-{attack_type}.csv"),
            "-config-location", pathlib.Path(ROOT_DIR, "stix", "input", "config.json"),
            "-veris-version", "1.3.7",
        ])
        
        
        
        
        subprocess.run([
            "python", "-m",  "stix.parse",
            "-input-enumerations", pathlib.Path(ROOT_DIR, "mappings", attack_type, "csv", 
                f"veris137-enumerations-{attack_type}.csv"), 
            "-input-mappings", pathlib.Path(ROOT_DIR, "mappings", attack_type, "csv", 
                f"veris137-mappings-{attack_type}.csv"), 
            "-output-enumerations", pathlib.Path(ROOT_DIR, "stix", "output", attack_type, 
                f"veris137-enumerations-{attack_type}.json"), 
            "-output-mappings", pathlib.Path(ROOT_DIR, "stix", "output", attack_type, 
                f"veris137-mappings-{attack_type}.json"),
            "-config-location", pathlib.Path(ROOT_DIR, "stix", "input", "config.json"),
            "-attack-domain", f"{attack_type}-attack",
        ])
        

def create_layers(attack_types):
    for attack_type in attack_types:
        subprocess.run([
            "python", "-m", "util.mappings_to_heatmaps.py",
            "-veris-objects", pathlib.Path(ROOT_DIR, "stix", "output", attack_type, 
                f"veris137-enumerations-{attack_type}.json"),
            "-mappings", pathlib.Path(ROOT_DIR, "stix", "output", attack_type, 
                f"veris137-mappings-{attack_type}.json"),
            "-domain", f"{attack_type}-attack",
            "-version", "12.1",
            "-output", pathlib.Path(ROOT_DIR, "stix", "output", attack_type, "layers"),
            "-clear", 
            "-build-directory"
        ])


def main(args):
    if args.task == "mappings":
        if args.attack_type == "all":
            create_mappings(["enterprise", "ics", "mobile"])
        else:
            create_mappings([args.attack_type])
    elif args.task == "layers":
        if args.attack_type == "all":
            create_layers(["enterprise", "ics", "mobile"])
        else:
            create_layers([args.attack_type])



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create the mappings and stix data")
    parser.add_argument("-attack-type",
                        dest="attack_type",
                        choices=["all", "enterprise", "ics", "mobile"],
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
    args = parser.parse_args()

    main(args)
    