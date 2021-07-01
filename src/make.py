import json
import os
import pathlib
import subprocess
import sys


def find_file_with_suffix(suffix, folder):
    """find a file with the given suffix in the folder"""
    for f in os.listdir(folder):
        if f.endswith(suffix):
            return f
    return None


def main():
    """rebuild veris framework from the input data"""
    for framework in ["veris"]:
        # move to the framework folder
        framework_folder = pathlib.Path("frameworks", framework)
        os.chdir(framework_folder)

        # read the framework config
        config_path = pathlib.Path("input", "config.json")
        if not config_path.exists():
            print("WARNING: framework has no config file, skipping")
            os.chdir(os.path.join("..", ".."))
            continue
        with config_path.open("r", encoding="utf-8") as f:
            config = json.load(f)

        # build the veris objects and mappings STIX
        subprocess.run([sys.executable, "parse.py"])
        os.chdir(os.path.join("..", ".."))

        # find the mapping and object files that were generated
        veris_file = find_file_with_suffix("-enumerations.json", pathlib.Path(framework_folder, "stix"))
        mappings_file = find_file_with_suffix("-mappings.json", pathlib.Path(framework_folder, "stix"))

        # run the utility scripts
        os.chdir("util")
        subprocess.run([
            sys.executable, "mappings_to_heatmaps.py",
            "-veris-objects", pathlib.Path("..", framework_folder, "stix", veris_file),
            "-mappings", pathlib.Path("..", framework_folder, "stix", mappings_file),
            "-output", pathlib.Path("..", framework_folder, "layers"),
            "-domain", config["attack_domain"],
            "-version", config["attack_version"],
            "-framework", framework,
            "--clear",
            "--build-directory",
        ])
        subprocess.run([
            sys.executable, "append_mappings.py",
            "-veris-objects", pathlib.Path("..", framework_folder, "stix", veris_file),
            "-mappings", pathlib.Path("..", framework_folder, "stix", mappings_file),
            "-output", pathlib.Path("..", framework_folder, "stix", f"{framework}135-enterprise-attack.json"),
            "-domain", config["attack_domain"],
            "-version", config["attack_version"],
        ])
        subprocess.run([
            sys.executable, "list_mappings.py",
            "-veris-objects", pathlib.Path("..", framework_folder, "stix", veris_file),
            "-mappings", pathlib.Path("..", framework_folder, "stix", mappings_file),
            "-output", pathlib.Path("..", framework_folder, f"{framework}-list-mappings.xlsx"),
            "-domain", config["attack_domain"],
            "-version", config["attack_version"],
        ])
        # reset
        os.chdir("..")


if __name__ == "__main__":
    main()
