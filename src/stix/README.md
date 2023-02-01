# Stix Scripts and Data
This folder contains mappings of the VERIS framework to MITRE ATT&CK along with parsers

| File | Description |
|:--|:--|
| [input](./input/) | Folder that contains the config file with version numbers |
| [output](./output/) | Folder that contains veris objects and navigator layers for each ATT&CK type |
| [parse.py](#parsepy) | Script to build the raw STIX data from the input spreadsheets |
| [parse_veris.py](#parse_verispy) | Helper Script used to parse the veris enumerations and generate STIX data |
| [parse_mappings.py](#parse_mappingspy) | Helper script used to parse ATT&CK mappings data and generate STIX relationships between ATT&CK and Veris objects |

## parse.py
### Description
Script to build the raw STIX data from the input spreadsheets
### Use
| Argument | Description | Default Value |
|:--|:--|:--|
| input-enumerations | csv file with VERIS entries | [../mappings/enterprise/csv/veris137-enumerations-enterprise.csv](../mappings/enterprise/csv/) |
| input-mappings | csv file with mappings between VERIS and ATT&CK | [../mappings/enterprise/csv/veris137-mappings-enterprise.csv](../mappings/enterprise/csv/) |
| output-enumerations | output STIX bundle file for the veris entries | [../mappings/enterprise/json/veris137-enumerations-enterprise.json](../mappings/enterprise/json/) |
| output-mappings | output STIX bundle file for the mappings | [../mappings/enterprise/json/veris137-mappings-enterprise.json](../mappings/enterprise/json/) |
| config-location | filepath to the configuration for the framework | [input/config.json](./input/config.json) |
| attack-domain | attack domain we are mapping. i.e. 'enterprise-attack', 'mobile-attack', 'ics-atack' | enterprise-attack |

Generate STIX data from Enterprise ATT&CK
```
python parse.py -attack-domain enterprise-attack
```

## parse_veris.py
Helper Script used to parse the veris enumerations and generate STIX data. It is called by [parse.py](#parsepy) and converts all of the objects in the provided input-enumerations file to STIX attack-patterns.

## parse_mappings.py
Helper script used to parse ATT&CK mappings data and generate STIX relationships between ATT&CK and Veris objects. The script pulls the specified ATT&CK domain and version data down in STIX format and uses the given input-mappings file to create STIX relationships.