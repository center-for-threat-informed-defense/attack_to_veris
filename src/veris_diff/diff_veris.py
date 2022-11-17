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

def printChanges(changes):
    with open("output\\result.json", "w") as file:
        file.write(json.dumps(changes, indent=4))


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
    depricatedKeys = oldKeys - keys

    for key in keys:
        if key in addedKeys:
            changes[key] = {"New field": new[key]}
            print("1")
        elif key in depricatedKeys:
            changes[key] = "Depricated"
            print("2")
        elif old[key] != new[key]:
            if type(new[key]) != dict:
                tmp = {
                    "old": old[key],
                    "new": new[key]
                }
                changes[key] = tmp
            else:
                changes[key] = findChanges(old[key], new[key])
        

    return changes
        



def compareSchema(old, new):
    changes = {
        "OldProperties": [],
        "NewProperties": [],
        "DepricatedProperties": [],
        "AddedProperties": [],
        "Changes": [],
    }
    changes["OldProperties"] = list(old["properties"].keys())
    changes["NewProperties"] = list(new["properties"].keys())


    for field in changes["OldProperties"]:
        if field not in changes["NewProperties"]:
            changes["DepricatedProperties"].append(field)
    
    for field in changes["NewProperties"]:
        if field not in changes["OldProperties"]:
            changes["AddedProperties"].append(field)

    print("depricated")
    print(changes["DepricatedProperties"])
    print("added")
    print(changes["AddedProperties"])

    for key in changes["NewProperties"]:
        if key not in changes["DepricatedProperties"] and key not in changes["AddedProperties"]:
            changeDict = findChanges(old["properties"][key], new["properties"][key])
            changes["Changes"].append({key: changeDict})

    return changes

    

def main():
    logger.info("Loading old schema")
    old = loadData("./old/verisc1_3_5.json")

    logger.info("Loading new schema")
    new = loadData("./new/verisc1_3_6.json")

    printChanges(compareSchema(old, new))




if __name__ == "__main__":
    main()
