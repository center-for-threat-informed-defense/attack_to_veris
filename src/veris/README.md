# Tools for VERIS Mappings to MITRE ATT&CK®

This directory contains a Python package of tools for working with the VERIS mappings to
ATT&CK.

## Set up

You will need the following prerequisites to run the tools:

1. [Python (≥3.8)](https://www.python.org/downloads/)
2. [Python Poetry](https://python-poetry.org/docs/#installation)

Once you have the repository cloned, run the following one-time command to initialize a
virtual environment and install dependenies:

```
poetry install
```

Once the dependencies are installed, you will need to source the environment in each
terminal window prior to using the Python tools.

```
poetry shell
```

## Tools

The tools are organized into the following subdirectories. Click the link to view
detailed instructions for working with those tools.

| Directory                     | Description                                                                                    |
| ----------------------------- | ---------------------------------------------------------------------------------------------- |
| [`parse/`](./parse)           | Tools for parsing VERIS data and mappings spreadsheets.                                        |
| [`util/`](./util)             | Utilities for generating content from mappings data, such as Navigator layers, CSV files, etc. |
| [`veris_diff/`](./veris_diff) | Tools for comparing versions of the VERIS schema and identifying changes.                      |

## Customization

To create customized mappings, edit the input data in the [`inputs/`](../../inputs)
directory and then use the tools above to regenerate the outputs.
