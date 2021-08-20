# Visualization
This repository includes several ways to visualize the VERIS mappings to ATT&CK. 

## ATT&CK Navigator Layers

This project provides [ATT&CK Navigator](https://github.com/mitre-attack/attack-navigator) Layers representing the mappings to ATT&CK. You can find the Layer files in the `/frameworks/` folder:
- [VERIS Layers](/frameworks/veris/layers)

## STIX Visualization
The STIX content can be visualized using the [CTI STIX Visualization](https://github.com/oasis-open/cti-stix-visualization/) tool.
- [VERIS Mappings Graph Visualization](https://oasis-open.github.io/cti-stix-visualization/?url=https://raw.githubusercontent.com/center-for-threat-informed-defense/attack_to_veris/main/frameworks/veris/stix/veris135-enterprise-attack.json)

_Note: because of the large number of objects it will take significant resources to generate the graph._

## Mappings Spreadsheet

The Excel spreadsheet lists all mappings for the VERIS framework in a tabular format. You can find the spreadsheets within the `/frameworks/` folder:
- [VERIS Mappings Spreadsheet](/frameworks/veris/veris-mappings.xlsx)

The [listMappings](/src/) script can be used to generate this same information in additional formats:
- Excel spreadsheet
- CSV
- HTML table
- Markdown table

## Appending VERIS Framework objects into ATT&CK

The [append_mappings.py](/src/append_mappings.py) utility script creates a STIX Bundle where veris objects, mappings and ATT&CK content are together in a single file. This section describes the usage of these specialty bundles, which can be found on this repo alongside their data in the framework `stix` folders:
- [VERIS Appended STIX Bundle](/frameworks/veris/stix/veris135-enterprise-attack.json)

_Note: append_mappings.py will add veris objects to the STIX Bundle if they are mapped to ATT&CK. If you want to build the STIX Bundle with the full set of veris objects, run append_mappings.py with the `--allow-unmapped` flag._ 

## See also
- [Mapping Methodology](/docs/methodology.md) for a description of the general process used to create the veris mappings.
- [STIX Format](/docs/STIX_format.md) for more information about the STIX representation of the veris objects and mappings.
