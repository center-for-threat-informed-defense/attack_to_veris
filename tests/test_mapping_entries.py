import pathlib
import os

import pytest

from src.mappings_validator import (validate_json_mappings_metadata, validate_spreadsheet_mappings_metadata,
                                    validate_mapping_entries)


@pytest.fixture()
def project_meta():
    attack_version = "9.0"
    veris_version = "1.3.5"
    metadata_version = "1.9"
    return attack_version, veris_version, metadata_version


@pytest.fixture()
def dir_location():
    cwd = os.getcwd()
    if "tests" in cwd:
        return os.path.dirname(cwd)
    else:
        return cwd


def test_spreadsheet_mappings_metadata(project_meta, dir_location):
    """Tests metadata contents from the spreadsheet file"""
    spreadsheet_location = pathlib.Path(dir_location, "frameworks", "veris", "veris-mappings.xlsx")
    attack_version, veris_version, metadata_version = project_meta

    try:
        validate_spreadsheet_mappings_metadata(spreadsheet_location, attack_version, veris_version, metadata_version)
    except AssertionError:
        pytest.fail("Unexpected error for test_json_mappings_metadata")


def test_json_mappings_metadata(project_meta, dir_location):
    """Tests metadata contents from the json mappings file"""
    mappings_location = pathlib.Path(dir_location, "frameworks", "veris", "veris-mappings.json")
    attack_version, veris_version, metadata_version = project_meta

    try:
        validate_json_mappings_metadata(mappings_location, attack_version, veris_version, metadata_version)
    except AssertionError:
        pytest.fail("Unexpected error for test_json_mappings_metadata")


def test_mappings_entries(project_meta, dir_location):
    """Tests the spreadsheet entries for incorrect ATT&CK IDs or VERIS Paths"""
    spreadsheet_location = pathlib.Path(dir_location, "frameworks", "veris", "veris-mappings.xlsx")
    attack_version, _, _ = project_meta

    try:
        validate_mapping_entries(spreadsheet_location, attack_version)
    except AssertionError:
        pytest.fail("Unexpected error for test_mappings_entries")
