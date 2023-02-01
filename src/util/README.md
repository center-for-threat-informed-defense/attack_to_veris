# Utility Scripts
Contains scripts used to create auxiliary data for mappings

| Script | Purpose |
|:---|:---|
| [create_mappings.py](#create_mappingspy) | From the master excel spreadsheet, generates the CSV for the VERIS enumerations and mappings. It also creates the JSON mappings that sit at the same level as the XLSX file. |
| [mappings_to_heatmaps.py](#mappings_to_heatmapspy) | Enables visualization of the veris mappings in the ATT&CK Matrix. Builds ATT&CK Navigator heatmap layers. These layers can also be found in the `layers` folder of the attack type in the stix output folder. |
| [make.py](#makepy) | Utility script used to generate the data in the format this repository is set up for |

## create_mappings.py
### Description
From the master excel spreadsheet, generates the CSV for the VERIS enumerations and mappings. It also creates the JSON mappings that sit at the same level as the XLSX file.
### Use
| Argument | Description | Default Value |
|:--|:--|:--|
| config-location | filepath to the configuration for the framework | [../stix/input/config.json](../stix/input/config.json) |
| spreadsheet-location | filepath to the Excel spreadsheet for the mappings | [../mappings/enterprise/xlsx/veris-2-mappings-enterprise.xlsx](../mappings/enterprise/xlsx) |
| json-location | filepath to the JSON version of the spreadsheet mappings | [../mappings/enterprise/json/veris-2-mappings-enterprise.json](../mappings/enterprise/json/) |
| mappings-location | filepath to the CSV spreadsheet to write the mappings | [../mappings/enterprise/csv/veris137-mappings-enterprise.csv](../mappings/enterprise/csv/) |
| veris-location | filepath to the CSV spreadsheet to write the enumeration | [../mappings/enterprise/csv/veris137-enumerations-enterprise.csv](./mappings/enterprise/csv/) |
| veris-version | the veris version to use | 1.3.7 |
## mappings_to_heatmaps.py
### Description
### Use
## make.py
### Description
### Use
