# Veris Diff Scripts
This folder contains a script used to generate a diff file between versions of the Veris schema

## diff_veris.py
### Description
Generates a file that describes the differences between two different versions of the Veris schema. This has been tested on the verisc versions of the schema.

It outputs both a .json and .md file that include the changes.

### Use
* Place the older verisc version of the schema in the 'old' directory and new version in the 'new' directory.
* Run the script 
    * ```python diff_veris.py```
* Check the 'output' folder for the resulting files