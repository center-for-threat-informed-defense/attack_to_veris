# Veris Diff Scripts
This folder contains a script used to generate a diff file between versions of the VERIS schema

## diff_veris.py
### Description
Generates a file that describes the differences between two different versions of the VERIS schema. This has been tested on the verisc versions of the schema.

It outputs both a .json and .md file that include the changes.

Veris has multiple versions of their schemas, for this project we used the 'verisc' version. Because of that, the verisc version is the only one that has been tested.

https://github.com/vz-risk/veris/tree/master/bin/veris_webapp_legacy/assets/schema

### Use
* Place the older verisc version of the schema in the 'old' directory and new version in the 'new' directory.
* Run the script 
    * ```python diff_veris.py```
* Check the 'output' folder for the resulting files