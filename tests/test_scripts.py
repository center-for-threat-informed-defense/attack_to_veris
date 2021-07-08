import os
import pathlib
import subprocess
import sys

import pytest


@pytest.fixture()
def dir_location():
    cwd = os.getcwd()
    if "tests" in cwd:
        return os.path.dirname(cwd)
    else:
        return cwd


def test_append_mappings(dir_location):
    veris_objects = pathlib.Path(dir_location, "frameworks", "veris", "stix", "veris135-enumerations.json")
    output_location = pathlib.Path(dir_location, "frameworks", "veris", "stix", "veris135-enterprise-attack.json")
    mappings = pathlib.Path(dir_location, "frameworks", "veris", "stix", "veris135-mappings.json")
    script_location = f"{dir_location}/src/append_mappings.py"
    child_process = subprocess.Popen([
        sys.executable, script_location,
        "-veris-objects", veris_objects,
        "-mappings", mappings,
        "-output", output_location,
    ])
    child_process.wait(timeout=60)
    assert child_process.returncode == 0


def test_create_mappings(dir_location):
    config_location = pathlib.Path(dir_location, "frameworks", "veris", "input", "config.json")
    spreadsheet_location = pathlib.Path(dir_location, "frameworks", "veris", "veris-mappings.xlsx")
    json_location = pathlib.Path(dir_location, "frameworks", "veris", "veris-mappings.json")
    mappings_location = pathlib.Path(dir_location, "frameworks", "veris", "input", "veris135-mappings.csv")
    veris_location = pathlib.Path(dir_location, "frameworks", "veris", "input", "veris135-enumerations.csv")
    script_location = f"{dir_location}/src/create_mappings.py"
    child_process = subprocess.Popen([
        sys.executable, script_location,
        "-config-location", config_location,
        "-spreadsheet-location", spreadsheet_location,
        "-json-location", json_location,
        "-mappings-location", mappings_location,
        "-veris-location", veris_location,
    ])
    child_process.wait(timeout=60)
    assert child_process.returncode == 0


def test_list_mappings(dir_location):
    veris_objects = pathlib.Path(dir_location, "frameworks", "veris", "stix", "veris135-enumerations.json")
    mappings = pathlib.Path(dir_location, "frameworks", "veris", "stix", "veris135-mappings.json")
    output_location = pathlib.Path(dir_location, "frameworks", "veris", "veris-mappings.md")
    script_location = f"{dir_location}/src/list_mappings.py"
    child_process = subprocess.Popen([
        sys.executable, script_location,
        "-veris-objects", veris_objects,
        "-mappings", mappings,
        "-output", output_location,
    ])
    child_process.wait(timeout=60)
    assert child_process.returncode == 0


def test_mappings_to_heatmaps(dir_location):
    veris_objects = pathlib.Path(dir_location, "frameworks", "veris", "stix", "veris135-enumerations.json")
    mappings = pathlib.Path(dir_location, "frameworks", "veris", "stix", "veris135-mappings.json")
    output_location = pathlib.Path(dir_location, "frameworks", "veris", "layers")
    script_location = f"{dir_location}/src/mappings_to_heatmaps.py"
    child_process = subprocess.Popen([
        sys.executable, script_location,
        "-veris-objects", veris_objects,
        "-mappings", mappings,
        "-output", output_location,
        "--clear",
        "--build-directory",
    ])
    child_process.wait(timeout=60)
    assert child_process.returncode == 0


def test_mappings_validator(dir_location):
    config_location = pathlib.Path(dir_location, "frameworks", "veris", "input", "config.json")
    spreadsheet_location = pathlib.Path(dir_location, "frameworks", "veris", "veris-mappings.xlsx")
    json_location = pathlib.Path(dir_location, "frameworks", "veris", "veris-mappings.json")
    script_location = f"{dir_location}/src/mappings_validator.py"
    need_pop = False
    if 'PYTHONPATH' not in os.environ:
        os.environ['PYTHONPATH'] = dir_location
        need_pop = True
    child_process = subprocess.Popen([
        sys.executable, script_location,
        "-config-location", config_location,
        "-spreadsheet-location", spreadsheet_location,
        "-json-location", json_location,
    ], env=os.environ)
    child_process.wait(timeout=60)
    if need_pop:
        # cleanup purposes
        os.environ.pop('PYTHONPATH', None)
    assert child_process.returncode == 0


def test_make(dir_location):
    script_location = f"{dir_location}/src/make.py"
    child_process = subprocess.Popen([
        sys.executable, script_location,
    ])
    child_process.wait(timeout=90)
    assert child_process.returncode == 0
