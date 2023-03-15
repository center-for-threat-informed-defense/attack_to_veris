# Visualization
This repository includes several ways to visualize the VERIS mappings to ATT&CK. 

## ATT&CK Navigator Layers

This project provides [ATT&CK Navigator](https://github.com/mitre-attack/attack-navigator) Layers representing the mappings to ATT&CK. You can find the Layer files in the `/src/stix/output/` folder:
- [VERIS Layers](stix/output/attack_type/layers)

## STIX Visualization
The STIX content can be visualized using the [CTI STIX Visualization](https://github.com/oasis-open/cti-stix-visualization/) tool.
- [VERIS Mappings Graph Visualization](https://oasis-open.github.io/cti-stix-visualization/?url=https://raw.githubusercontent.com/center-for-threat-informed-defense/attack_to_veris/main/frameworks/veris/stix/veris135-enterprise-attack.json)

_Note: because of the large number of objects it will take significant resources to generate the graph._

## Mappings Spreadsheet

The mappings for the VERIS framework are provided in a tabular format in Excel spreadsheets. You can find the spreadsheets within the `src/mappings/` folder:
- [VERIS Enterprise Mappings Spreadsheet](src/mappings/enterprise/xlsx/veris-1_3_7-mappings-enterprise_v12.xlsx)
- [VERIS Mobile Mappings Spreadsheet](src/mappings/mobile/xlsx/veris-1_3_7-mappings-mobile_v12.xlsx)
- [VERIS ICS Mappings Spreadsheet](src/mappings/ics/xlsx/veris-1_3_7-mappings-ics_v12.xlsx)
- [VERIS Groups Mappings Spreadsheet](src/mappings/groups/xlsx/veris-1_3_7-mappings-groups_v12.xlsx)

The [STIX scripts] (src/stix/) and [utility scripts](/src/util/) can be used to generate mapping information in additional formats:
- CSV
- STIX/JSON
- HTML table
- Markdown table

## Appending VERIS Framework objects into ATT&CK

The [append_mappings.py](/src/append_mappings.py) utility script creates a STIX Bundle where VERIS objects, mappings and ATT&CK content are together in a single file. This section describes the usage of these specialty bundles, which can be found on this repo alongside their data in the framework `stix` folders:
- [VERIS Appended STIX Bundle](/frameworks/veris/stix/veris135-enterprise-attack.json)

_Note: append_mappings.py will add VERIS objects to the STIX Bundle if they are mapped to ATT&CK. If you want to build the STIX Bundle with the full set of VERIS objects, run append_mappings.py with the `--allow-unmapped` flag._ 

## See also
- [Mapping Methodology](/docs/methodology.rst) for a description of the general process used to create the VERIS mappings.
- [STIX Format](/docs/STIX_format.rst) for more information about the STIX representation of the VERIS objects and mappings.
