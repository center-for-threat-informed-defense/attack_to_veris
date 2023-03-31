import os
import pathlib
import subprocess
import sys
import tempfile
import csv
import filecmp

import pytest

from src.util.create_mappings import get_sheets, generate_csv_spreadsheet, generate_json_mappings


@pytest.fixture()
def dir_location():
    cwd = os.getcwd()
    if "tests" in cwd:
        return os.path.dirname(cwd)
    else:
        return pathlib.Path(cwd, "tests")


def test_get_sheets(dir_location):
    sheets = get_sheets(pathlib.Path(dir_location, "fixtures", "test_spreadsheet_1.xlsx"))
    sheet_names = [
        'Action.Hacking.Variety',
        'Action.Hacking.Vector',
        'Action.Malware.Variety',
        'Action.Malware.Vector',
        'Action.Social.Variety',
        'Action.Social.Vector',
        'Attribute.Integrity.Variety',
        'Attribute.Confidentiality.""',
        'Attribute.Availability.Variety',
        'Value_chain',
    ]

    for sheet in sheets:
        assert sheet[1] in sheet_names

def test_create_mappings_csv(dir_location):
    sheets = get_sheets(pathlib.Path(dir_location, "fixtures", "test_spreadsheet_1.xlsx"))

    with tempfile.NamedTemporaryFile() as csvfile:
        generate_csv_spreadsheet(sheets, pathlib.Path(csvfile.name))

        assert filecmp.cmp(csvfile.name, pathlib.Path(dir_location, "fixtures", "create_mappings_output.csv"))

def test_create_mappings_json(dir_location):
    sheets = get_sheets(pathlib.Path(dir_location, "fixtures", "test_spreadsheet_1.xlsx"))

    with tempfile.NamedTemporaryFile() as jsonfile:
        config = pathlib.Path(dir_location, "fixtures", "config.json")
        generate_json_mappings(sheets, config, pathlib.Path(jsonfile.name))

        assert filecmp.cmp(jsonfile.name, pathlib.Path(dir_location, "fixtures", "create_mappings_output.json"))

def test_parse_veris(dir_location):
    veris_enumerations_file = pathlib.Path(dir_location, "fixtures", "veris_enumerations.json")
    mappings_file = pathlib.Path(dir_location, "fixtures", "veris-mappings.json")

    mappings_location = pathlib.Path(dir_location, "fixtures", "create_mappings_output.csv")
    veris_location = pathlib.Path(dir_location, "fixtures", "veris137-enumerations.csv")
    veris_objects = pathlib.Path(veris_enumerations_file)
    mappings = pathlib.Path(mappings_file)
    config_location = pathlib.Path(dir_location, "fixtures", "config.json")
    child_process = subprocess.Popen([
        "python", "-m", "src.parse.parse",
        "-input-enumerations", veris_location,
        "-input-mappings", mappings_location,
        "-output-enumerations", veris_objects,
        "-output-mappings", mappings,
        "-config-location", config_location,
        "-attack-domain", "ics-attack",
    ])
    child_process.wait(timeout=60)
    assert child_process.returncode == 0

    if veris_enumerations_file.is_file():
        veris_enumerations_file.unlink()
    if mappings_file.is_file():
        mappings_file.unlink()

    