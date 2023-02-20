import json
import uuid

from stix2.v20 import AttackPattern, Bundle
from tqdm import tqdm
import pandas


class VERISEntry(object):
    """helper class defining a VERIS Entry"""

    def __init__(self, row, veris_ids):
        self.name = row["VALUE"]
        self.axes = row["AXES"]
        self.category = row["CATEGORY"]
        self.sub_category = row["SUB CATEGORY"]
        self.description = row["DESCRIPTION"]
        if self.sub_category == "":
            self.external_id = ".".join([self.axes, self.category, self.name])
        else:
            self.external_id = ".".join([self.axes, self.category, self.sub_category, self.name])

        # if the external_id is present in our veris_ids lookup reuse-it, otherwise calculate a new identifier
        if self.external_id in veris_ids:
            self.stix_id = veris_ids[self.external_id]
        else:
            self.stix_id = f"attack-pattern--{uuid.uuid4()}"

        

    def to_stix(self, framework_id):
        """Convert to a STIX AttackPattern"""
        base_url = "https://veriscommunity.net/enums.html"

        if self.axes == "action":
            base_url = base_url + "#section-actions"
        elif self.axes == "attribute":
            base_url = base_url + "#section-attributes"

        return AttackPattern(
            id=self.stix_id,
            name=self.name,
            description=self.description,
            labels=[
                f"veris-path:{self.external_id}"
            ],
            external_references=[
                {
                    "source_name": framework_id.lower(),
                    "external_id": self.external_id,
                    "url": base_url,
                }
            ]
        )


def parse_veris(veris_path, veris_ids, config_location):
    """Parse the VERIS entries, generate STIX from it and return a STIX Bundle
    :param veris_path: the filepath to the enumerations CSV file
    :param veris_ids: is a dict of format {veris_path -> stix ID} which maps a
        VERIS entry (e.g action.hacking.variety.DoS) to desired STIX IDs
    :param config_location: the filepath to the JSON configuration file.
    """
    print("reading framework config...", end="", flush=True)

    # load the mapping config
    with config_location.open("r", encoding="utf-8") as f:
        config = json.load(f)
        framework_id = config["framework_id"]
        veris_version = config["veris_version"]
    print("done")

    veris_df = pandas.read_csv(veris_path, sep=",", keep_default_na=False, header=0)

    veris_entries = []
    tqdm_format = "{desc}: {percentage:3.0f}% |{bar}| {elapsed}<{remaining}{postfix}"
    tqdm_desc = f"parsing {framework_id.lower()} version {veris_version}"
    for index, row in tqdm(list(veris_df.iterrows()), desc=tqdm_desc, bar_format=tqdm_format):
        entry = VERISEntry(row, veris_ids)
        veris_entries.append(entry)

        # update lookup so that subsequent objects can reference the same object identifier
        veris_ids[entry.external_id] = entry.stix_id

    # parse veris entries into stix
    stix_veris_entries = []
    tqdm_desc = "creating veris STIX objects"
    for veris_entry in tqdm(veris_entries, desc=tqdm_desc, bar_format=tqdm_format):
        stix_veris_entries.append(veris_entry.to_stix(framework_id))

    return Bundle(stix_veris_entries)
