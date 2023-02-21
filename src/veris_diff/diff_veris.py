#from msilib.schema import Error
import os
import json
import logging

#logging.basicConfig(filename="diff_veris.log", filemode="w")
logger = logging.getLogger(name="veris_logger")
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler("diff_veris.log")
fh.setLevel(logging.DEBUG)

logger.addHandler(fh)

def printChangesJson(changes):
    with open("output\\result.json", "w") as file:
        file.write(json.dumps(changes, indent=4))
        

def printChangesMD(changes):
    with open("output\\result.md", "w") as file:
        file.write("# Deprecated Properties\n")
        for i in range(len(changes["DeprecatedProperties"])):
            file.write(f"{i + 1}. {changes['DeprecatedProperties'][i]}\n")

        file.write("# Added Properties\n")
        for i in range(len(changes["AddedProperties"])):
            file.write(f"{i + 1}. {changes['AddedProperties'][i]}\n")

        file.write("# Property changes\n")
        for value in changes["Changes"]:
            for change in getChangeString(value):
                if change["type"] == "New":
                    file.write("## New field:\n")
                    file.write(f"### {change['path']}\n")
                    file.write(f"* ```{change['value']}```\n")

                elif change["type"] == "Update":
                    file.write("## Updated field:\n")
                    file.write(f"### {change['path']}\n")
                    file.write(f"* Old: ```{change['value']['old']}```\n")
                    file.write(f"* New: ```{change['value']['new']}```\n")


def getChangeString(change, path=""):
    for key in change.keys():
        if key == "New field":
            yield   {"path": path, "type": "New", "value": change[key]}
        elif key == "Update":
            yield {"path": path, "type": "Update", "value": change[key]}
        elif change[key] == "No Changes":
            yield {"path": path, "type": "No Change", "value": change[key]}
        else:
            path += f".{key}"
            yield from getChangeString(change[key], path)
             
    
def loadData(filepath):
    if os.path.isfile(filepath):
        file = open(filepath, "r", encoding="utf-8")
        return json.load(file)
    else:
        print(f"Could not find file: {filepath}")


def findChanges(old, new):
    if old == new:
        logger.info(f"No changes for {new}")
        return "No Changes"

    changes = {}
    keys = new.keys()
    oldKeys = old.keys()
    addedKeys = keys - oldKeys
    deprecatedKeys = oldKeys - keys

    for key in keys:
        if key in addedKeys:
            changes[key] = {"New field": new[key]}
            print("1")
        elif key in deprecatedKeys:
            changes[key] = "Deprecated"
            print("2")
        elif old[key] != new[key]:
            if type(new[key]) != dict:
                tmp = {
                    "Update": {
                        "old": old[key],
                        "new": new[key]
                    }
                }
                changes[key] = tmp
            else:
                changes[key] = findChanges(old[key], new[key])
        

    return changes
        

def compareSchema(old, new):
    changes = {
        "OldProperties": [],
        "NewProperties": [],
        "DeprecatedProperties": [],
        "AddedProperties": [],
        "Changes": [],
    }
    changes["OldProperties"] = list(old["properties"].keys())
    changes["NewProperties"] = list(new["properties"].keys())


    for field in changes["OldProperties"]:
        if field not in changes["NewProperties"]:
            changes["DeprecatedProperties"].append(field)
    
    for field in changes["NewProperties"]:
        if field not in changes["OldProperties"]:
            changes["AddedProperties"].append(field)

    print("deprecated")
    print(changes["DeprecatedProperties"])
    print("added")
    print(changes["AddedProperties"])

    for key in changes["NewProperties"]:
        if key not in changes["DeprecatedProperties"] and key not in changes["AddedProperties"]:
            changeDict = findChanges(old["properties"][key], new["properties"][key])
            changes["Changes"].append({key: changeDict})

    return changes

    
def main():
    logger.info("Loading old schema")
    old = loadData("./old/verisc.json")

    logger.info("Loading new schema")
    new = loadData("./new/verisc.json")

    changes = compareSchema(old, new)

    printChangesJson(changes)

    printChangesMD(changes)


if __name__ == "__main__":
    main()
