import argparse
import csv
import datetime
import json
import pathlib

import numpy
import pandas
import requests


def generate_veris_enumerations(veris_location, veris_version):
    """Reads the enumeration defined in VERIS and creates a spreadsheet only for the axes
    and categories described below."""
    veris_url = f"https://raw.githubusercontent.com/vz-risk/VCDB/{veris_version}/vcdb-labels.json"
    json_enum = requests.get(veris_url).json()
    axes = {"action": ["hacking", "malware", "misuse", "social"],
            "attribute": ["integrity"],
            "value_chain": ["development", "non-distribution services", "targeting", "distribution"],
            }

    with veris_location.open('w', newline='\n', encoding='utf-8') as csvfile:
        fieldnames = ['AXES', 'CATEGORY', 'SUB CATEGORY', 'VALUE', 'DESCRIPTION']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for axes_name, axes_values in axes.items():
            for axes_value in axes_values:
                sub_categories = json_enum[axes_name][axes_value]
                for sub_category, category_value in sub_categories.items():
                    for category_name, category_description in category_value.items():
                        writer.writerow({
                            'AXES': axes_name,
                            'CATEGORY': axes_value,
                            'SUB CATEGORY': sub_category,
                            'VALUE': category_name,
                            'DESCRIPTION': category_description.strip()
                        })


def get_sheets(spreadsheet_location):
    """Helper method to retrieve Excel sheets"""
    sheet1 = 'Action.Hacking.Variety'
    sheet2 = 'Action.Hacking.Vector'
    sheet3 = 'Action.Malware.Variety'
    sheet4 = 'Action.Malware.Vector'
    sheet5 = 'Action.Social.Variety'
    sheet6 = 'Action.Social.Vector'
    sheet7 = 'Attribute.Integrity.Variety'
    sheet8 = 'Value_chain'

    xls = pandas.ExcelFile(spreadsheet_location)
    df1 = pandas.read_excel(xls, sheet1)
    df2 = pandas.read_excel(xls, sheet2)
    df3 = pandas.read_excel(xls, sheet3)
    df4 = pandas.read_excel(xls, sheet4)
    df5 = pandas.read_excel(xls, sheet5)
    df6 = pandas.read_excel(xls, sheet6)
    df7 = pandas.read_excel(xls, sheet7)
    df8 = pandas.read_excel(xls, sheet8)

    sheets = [
        (df1, sheet1),
        (df2, sheet2),
        (df3, sheet3),
        (df4, sheet4),
        (df5, sheet5),
        (df6, sheet6),
        (df7, sheet7),
        (df8, sheet8),
    ]
    return sheets


def generate_csv_spreadsheet(spreadsheet_location, mappings_location):
    """Reads the main XSLX mappings file and creates a spreadsheet for the
    mappings in CSV"""
    sheets = get_sheets(spreadsheet_location)
    now = datetime.datetime.utcnow()
    strf_time = now.strftime("%y/%m/%d")
    relationship_type = "related-to"

    with mappings_location.open('w', newline='\n', encoding='utf-8') as csvfile:
        fieldnames = ['DATE DELIVERED', 'VERIS PATH', 'RELATIONSHIP TYPE', 'TECHNIQUE ID']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for sheet, name in sheets:
            name = name.lower()
            veris_path = None
            for idx, row in sheet.iterrows():
                if row[0] is not numpy.nan:
                    veris_path = f'{name}.{row[0]}'

                if row[1] is not numpy.nan:
                    writer.writerow({
                        'DATE DELIVERED': strf_time,
                        'VERIS PATH': veris_path,
                        'RELATIONSHIP TYPE': relationship_type,
                        'TECHNIQUE ID': row[1]  # .strip()
                    })


def generate_json_mappings(spreadsheet_location, config_location, json_mappings_location):
    """Reads the XLSX mappings and creates the normal JSON file used to
    describe the bi-directional mappings for this project."""
    sheets = get_sheets(spreadsheet_location)
    json_mappings = {
        "metadata": {},
        "attack_to_veris": {},
        "veris_to_attack": {},
    }

    with config_location.open("r", encoding="utf-8") as json_conf:
        json_mappings["metadata"] = json.load(json_conf)

    for sheet, name in sheets:
        name = name.lower()
        veris_path = None
        for idx, row in sheet.iterrows():
            if row[0] is not numpy.nan:
                veris_path = f'{name}.{row[0]}'
            axes, category, sub_category, veris_name = veris_path.split(".")
            attack_id, technique_name = row[1], row[2]

            veris_to_attack = json_mappings["veris_to_attack"]

            if axes not in veris_to_attack:
                veris_to_attack[axes] = {}
            if category not in veris_to_attack[axes]:
                veris_to_attack[axes][category] = {}
            if sub_category not in veris_to_attack[axes][category]:
                veris_to_attack[axes][category][sub_category] = {}
            if veris_name not in veris_to_attack[axes][category][sub_category]:
                veris_to_attack[axes][category][sub_category][veris_name] = {}
            if attack_id not in veris_to_attack[axes][category][sub_category][veris_name]:
                map_entry = {"name": technique_name}
                veris_to_attack[axes][category][sub_category][veris_name][attack_id] = map_entry

            attack_to_veris = json_mappings["attack_to_veris"]

            if attack_id not in attack_to_veris:
                map_entry = {"name": technique_name, "veris": [veris_path]}
                attack_to_veris[attack_id] = map_entry
            elif veris_path not in attack_to_veris[attack_id]["veris"]:
                attack_to_veris[attack_id]["veris"].append(veris_path)
                attack_to_veris[attack_id]["veris"].sort()

    with json_mappings_location.open("w", encoding="utf-8") as f:
        json.dump(json_mappings, f, indent=4, sort_keys=False, ensure_ascii=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create ATT&CK Navigator layers from VERIS mappings")
    parser.add_argument("-config-location",
                        dest="config_location",
                        help="filepath to the configuration for the framework",
                        type=lambda path: pathlib.Path(path),
                        default=pathlib.Path("..", "frameworks", "veris", "input", "config.json"))
    parser.add_argument("-spreadsheet-location",
                        dest="spreadsheet_location",
                        help="filepath to the Excel spreadsheet for the mappings",
                        type=lambda path: pathlib.Path(path),
                        default=pathlib.Path("..", "frameworks", "veris", "veris-mappings.xlsx"))
    parser.add_argument("-json-location",
                        dest="json_location",
                        help="filepath to the JSON version of the spreadsheet mappings",
                        type=lambda path: pathlib.Path(path),
                        default=pathlib.Path("..", "frameworks", "veris", "veris-mappings.json"))
    parser.add_argument("-mappings-location",
                        dest="mappings_location",
                        help="filepath to the CSV spreadsheet to write the mappings",
                        type=lambda path: pathlib.Path(path),
                        default=pathlib.Path("..", "frameworks", "veris", "input", "veris135-mappings.csv"))
    parser.add_argument("-veris-location",
                        dest="veris_location",
                        help="filepath to the CSV spreadsheet to write the enumeration",
                        type=lambda path: pathlib.Path(path),
                        default=pathlib.Path("..", "frameworks", "veris", "input", "veris135-enumerations.csv"))
    parser.add_argument("-veris-version",
                        dest="veris_version",
                        help="the veris version to use",
                        type=str,
                        default="1.3.5")

    args = parser.parse_args()

    generate_veris_enumerations(args.veris_location, args.veris_version)
    generate_csv_spreadsheet(args.spreadsheet_location, args.mappings_location)
    generate_json_mappings(args.spreadsheet_location, args.config_location, args.json_location)
