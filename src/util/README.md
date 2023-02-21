# Utility Scripts
Contains scripts used to create auxiliary data for mappings

| Script | Purpose |
|:---|:---|
| [create_mappings.py](#create_mappingspy) | From the master excel spreadsheet, generates the CSV for the VERIS enumerations and mappings. It also creates the JSON mappings that sit at the same level as the XLSX file. |
| [mappings_to_heatmaps.py](#mappings_to_heatmapspy) | Enables visualization of the veris mappings in the ATT&CK Matrix. Builds ATT&CK Navigator heatmap layers. These layers can also be found in the `layers` folder of the attack type in the stix output folder. |
| [make.py](#makepy) | Utility script used to generate the data in this repository. |

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
| veris-location | filepath to the CSV spreadsheet to write the enumeration | [../mappings/enterprise/csv/veris137-enumerations-enterprise.csv](../mappings/enterprise/csv/) |
| veris-version | the veris version to use | 1.3.7 |

Use with default arguments
```
python create_mappings.py
```
## mappings_to_heatmaps.py
### Description
Enables visualization of the veris mappings in the ATT&CK Matrix. Builds ATT&CK Navigator heatmap layers. These layers can also be found in the `layers` folder of the attack type in the stix output folder.
### Use
| Argument | Description | Default Value |
|:--|:--|:--|
| veris-objects | filepath to the STIX Bundle representing the VERIS framework | [../stix/output/enterprise/veris137-enumerations-enterprise.json](../stix/output/enterprise/) |
| mappings | filepath to the STIX Bundle mappings from VERIS to ATT&CK | [../stix/output/enterprise/veris137-mappings-enterprise.json](../stix/output/enterprise/) |
| domain | the domain of ATT&CK to visualize (options: enterprise-attack, ics-attack, mobile-attack) | enterprise-attack |
| version | which ATT&CK version to use | 12.1 |
| output | folder to write output layers to | [../stix/output/enterprise/layers](../stix/output/enterprise/layers/) |
| clear | if flag specified, will remove the contents the output folder before writing layers | N/A |
| build-directory | if flag specified, will build a markdown file listing the output files for easy access in the Navigator | N/A |

Use with default arguments, but clear previous results and create markdown file
```
python mappings_to_heatmaps.py -clear -build-directory
```
## make.py
### Description
Utility script used to generate the data in this repository. It will automatically generate data for the provided attack-type and place it in the appropriate folders. This is useful so that users don't need to specify file paths for every version.
### Use
| Argument | Description | Default Value |
|:--|:--|:--|
| attack-type | What attack type do you want to generate. (options: all, enterprise, ics, mobile) | all |
| task | Create new mappings, or generate navigator layers based on existing mappings data. (options: mappings, layers) | mappings |

Generate all of the mappings ATT&CK types
```
python make.py -attack-type all -task mappings
```
Generate navigator layers for all attack types
```
python make.py -attack-type all -task layers
```
