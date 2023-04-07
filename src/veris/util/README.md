# Utility Scripts
Contains scripts used to create auxiliary data for mappings

| Script                                             | Purpose                                                                                                                                                                                                       |
| :------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [create_mappings.py](#create_mappingspy)           | From the master excel spreadsheet, generates the CSV for the VERIS enumerations and mappings. It also creates the JSON mappings that sit at the same level as the XLSX file.                                  |
| [mappings_to_heatmaps.py](#mappings_to_heatmapspy) | Enables visualization of the veris mappings in the ATT&CK Matrix. Builds ATT&CK Navigator heatmap layers. These layers can also be found in the `layers` folder of the attack type in the stix output folder. |
| [make.py](#makepy)                                 | Utility script used to generate the data in this repository.                                                                                                                                                  |

## create_mappings.py
### Description
From the master excel spreadsheet, generates the CSV for the VERIS enumerations and mappings. It also creates the JSON mappings that sit at the same level as the XLSX file.
### Use
| Argument             | Description                                              | Default Value                                                                                  |
| :------------------- | :------------------------------------------------------- | :--------------------------------------------------------------------------------------------- |
| config-location      | filepath to the configuration for the framework          | `../../../stix/input/config.json`                                                              |
| spreadsheet-location | filepath to the Excel spreadsheet for the mappings       | `../../../mappings/veris-1.3.7/input/enterprise/xlsx/veris-1_3_7-mappings-enterprise_v12.xlsx` |
| json-location        | filepath to the JSON version of the spreadsheet mappings | `../../../mappings/veris-1.3.7/input/enterprise/json/veris-1_3_7-mappings-enterprise.json`     |
| mappings-location    | filepath to the CSV spreadsheet to write the mappings    | `../../../mappings/veris-1.3.7/input/enterprise/csv/veris1_3_7-mappings-enterprise.csv`        |
| veris-location       | filepath to the CSV spreadsheet to write the enumeration | `../../../mappings/veris-1.3.7/input/enterprise/csv/veris1_3_7-enumerations-enterprise.csv`    |
| veris-version        | the veris version to use                                 | 1.3.7                                                                                          |

Use with default arguments
```
python create_mappings.py
```
## mappings_to_heatmaps.py
### Description
Enables visualization of the veris mappings in the ATT&CK Matrix. Builds ATT&CK Navigator heatmap layers. These layers can also be found in the `layers` folder of the attack type in the stix output folder.
### Use
| Argument        | Description                                                                                             | Default Value                                                                           |
| :-------------- | :------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------- |
| veris-objects   | filepath to the STIX Bundle representing the VERIS framework                                            | `../../../mappings/veris-1.3.7/stix/enterprise/veris1_3_7-enumerations-enterprise.json` |
| mappings        | filepath to the STIX Bundle mappings from VERIS to ATT&CK                                               | `../../../mappings/veris-1.3.7/stix/enterprise/veris1_3_7-mappings-enterprise.json`     |
| domain          | the domain of ATT&CK to visualize (options: enterprise-attack, ics-attack, mobile-attack)               | enterprise-attack                                                                       |
| version         | which ATT&CK version to use                                                                             | 12.1                                                                                    |
| output          | folder to write output layers to                                                                        | `../../../mappings/veris-1.3.7/layers)`                                                 |
| clear           | if flag specified, will remove the contents the output folder before writing layers                     | N/A                                                                                     |
| build-directory | if flag specified, will build a markdown file listing the output files for easy access in the Navigator | N/A                                                                                     |

To build layers from project root:

```
$ python src/veris/util/mappings_to_heatmaps.py -clear -build-directory \
    -domain enterprise-attack \
    -veris-objects mappings/veris-1.3.7/stix/enterprise/veris1_3_7-enumerations-enterprise.json \
    -mappings mappings/veris-1.3.7/stix/enterprise/veris1_3_7-mappings-enterprise.json


$ python src/veris/util/mappings_to_heatmaps.py -clear -build-directory \
    -domain mobile-attack \
    -veris-objects mappings/veris-1.3.7/stix/mobile/veris1_3_7-enumerations-mobile.json \
    -mappings mappings/veris-1.3.7/stix/mobile/veris1_3_7-mappings-mobile.json

$ python src/veris/util/mappings_to_heatmaps.py -clear -build-directory \
    -domain ics-attack \
    -veris-objects mappings/veris-1.3.7/stix/ics/veris1_3_7-enumerations-ics.json \
    -mappings mappings/veris-1.3.7/stix/ics/veris1_3_7-mappings-ics.json
```

## make.py
### Description
Utility script used to generate the data in this repository. It will automatically generate data for the provided attack-type and place it in the appropriate folders. This is useful so that users don't need to specify file paths for every version.
### Use
| Argument    | Description                                                                                                    | Default Value |
| :---------- | :------------------------------------------------------------------------------------------------------------- | :------------ |
| attack-type | What attack type do you want to generate. (options: all, enterprise, ics, mobile)                              | all           |
| task        | Create new mappings, or generate navigator layers based on existing mappings data. (options: mappings, layers) | mappings      |

Generate all of the mappings ATT&CK types
```
python make.py -attack-type all -task mappings
```
Generate navigator layers for all attack types
```
python make.py -attack-type all -task layers
```
