# Utility Scripts

This folder contains additional resources that may be utilized in conjunction with the [ATT&CK to VERIS repository](/README.md).

| Script | Purpose |
|:---|:---|
| append_mappings.py | Creates a single STIX Bundle that encapsulates the VERIS objects, mappings and ATT&CK domain data. The default behavior is to only include objects that have been mapped from VERIS to ATT&CK. |
| create_mappings.py | From the master excel spreadsheet, generates the CSV for the VERIS enumerations and mappings. It also creates the JSON mappings that sit at the same level as the XLSX file. |
| list_mappings.py | Creates a human readable list of mappings from the STIX mapping data. This script is capable of generating outputs in xlsx, csv, html, and markdown formats. |
| make.py | To rebuild all the data in the repository based on the most up-to-date input spreadsheet mappings changes. |
| mappings_to_heatmaps.py | Enables visualization of the veris mappings in the ATT&CK Matrix. Builds ATT&CK Navigator heatmap layers. These layers can also be found in the `layers` folder of the framework. |
| mappings_validator.py | CLI validation tool for the master spreadsheet contents. Checks ATT&CK IDs are valid per the specified version, and VERIS paths are valid. |
