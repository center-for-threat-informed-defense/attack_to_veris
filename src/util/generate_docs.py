import argparse
import csv
import json
import re
import os
import pathlib
from datetime import datetime


def insert_docs(old_doc, doc_lines, tag):
    start_tag = re.compile(r"\.\. " + tag)
    end_tag = re.compile(r"\.\. /" + tag)
    output = list()

    for line in old_doc:
        if start_tag.search(line):
            break
        output.append(line.rstrip("\n"))
    else:
        raise RuntimeError("Did not find start tag")

    now = datetime.now().isoformat()
    output.append(f".. {tag} Generated at: {now}Z")
    output.append("")
    output.extend(doc_lines)
    output.append(f".. /{tag}")

    for line in old_doc:
        if end_tag.search(line):
            break
    else:
        raise RuntimeError("Did not find end tag")

    for line in old_doc:
        output.append(line.rstrip("\n"))
    output.append("")

    return "\n".join(output)


def generate_mappings_enumerations(file_path):
    objs = {}

    with open(file_path, "r") as file:
        csvreader = csv.reader(file)

        headers = next(csvreader)
        objs["headers"] = headers

        for row in csvreader:
            path = row[1].split(".")[0:3]
            key = ""
            for x in path:
                key += f"{x}."
            key = key[:-1]
            data = (
                row[0],
                row[1].split(".")[-1],
                row[2],
                row[3],
            )

            if key in objs.keys():
                objs[key].append(data)
            else:
                objs[key] = list()
                objs[key].append(data)
    return objs



def generate_attack_types_tables(attack_types, mappings_dir):
    obj_lines = []

    for attack_type in attack_types:
        csv_path = pathlib.Path(mappings_dir, attack_type, "csv", f"veris1_3_7-mappings-{attack_type}.csv")
        json_path = pathlib.Path(mappings_dir, attack_type, "json", f"veris-1_3_7-mappings-{attack_type}.json")
        if csv_path.is_file():
            mappings_table = generate_mappings_enumerations(csv_path)
            with open(json_path) as file:
                attack_names = json.loads(file.read())["attack_to_veris"]
        else:
            break

        if attack_type == "ics":
            obj_lines.append("ICS")
        else:
            obj_lines.append(attack_type.title())
        obj_lines.append("".join("-" for x in range(len(attack_type))))

        start_table = list()

        
        start_table.append("  :widths: 30 20 50")
        start_table.append("  :header-rows: 1")
        start_table.append("")
        start_table.append(f"  * - {mappings_table['headers'][1]}")
        start_table.append(f"    - {mappings_table['headers'][3]}")
        start_table.append(f"    - ATT&CK TECHNIQUE")

        del mappings_table["headers"]

        for key, values in mappings_table.items():
            title = key.split(".")[1]
            obj_lines.append(key.title())
            obj_lines.append("".join("~" for x in range(len(key))))
            obj_lines.append("")

            obj_lines.append(f".. list-table::")
            obj_lines.extend(start_table)
            obj_lines.append("")

            veris_id = ""
            for value in values:
                date, veris_path, relationship, tid = value
                if veris_path != veris_id:
                    obj_lines.append(f"  * - {veris_path}")
                    veris_id = veris_path
                else:
                    obj_lines.append(f"  * - ")
                obj_lines.append(f"    - {tid}")
                obj_lines.append(f"    - {attack_names[tid]['name']}")
                obj_lines.append("")

            
    return obj_lines


def main(args):
    attack_types = [i for i in os.listdir(args.mappings_dir) if 
                    not pathlib.Path(args.mappings_dir, i).is_file()]

    obj_lines = generate_attack_types_tables(attack_types, args.mappings_dir)
    
    with open(args.old_doc) as file:
        new_doc = insert_docs(file, obj_lines, "MAPPINGS_TABLE")

    with open(args.old_doc, "w") as out:
        out.write(new_doc)
    


    
if __name__ == "__main__":
    top_level = pathlib.Path(__file__).resolve().parent.parent.parent
    parser = argparse.ArgumentParser(description="Generate docs for mappings")
    parser.add_argument("-doc-file",
                        dest="old_doc",
                        help="Documentation file to edit",
                        type=pathlib.Path,
                        default=pathlib.Path(top_level / "docs" / "mappings.rst"),
                        )
    parser.add_argument("-mappings-dir",
                        dest="mappings_dir",
                        help="Location of the top level mappings directory",
                        type=pathlib.Path,
                        default=pathlib.Path(top_level,  "mappings",  "veris-1.3.7",  "input"),
                        )
    args = parser.parse_args()

    main(args)