# ATT&CK to VERIS Documentation

This directory contains the project documentation. This documentation is published to
https://center-for-threat-informed-defense.github.io/attack_to_veris. (NOTE -- this link
will not work until the project is published later this year!).

If you want to edit the documentation, go through the following steps to get set up on
your local machine.

## Dependencies

You'll need the following dependenies before getting started.

1. [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) or [GitHub Desktop](https://desktop.github.com/)
2. Make
    * For MacOS, use [these
      instructions](https://stackoverflow.com/questions/10265742/how-to-install-make-and-gcc-on-a-mac).
    * For Windows, try [Windows Subsystem for Linux
      v2](https://learn.microsoft.com/en-us/windows/wsl/install).
    * For Linux, install the `binutils` package from your package manager.
3. [Python ≥3.8](https://realpython.com/installing-python/)
4. Python Poetry
5. A text editor
    * If you don't have a preferred one, [Visual Studio
      Code](https://code.visualstudio.com/) is free and very popular.


## Initial Setup

This initial setup is a one-time step.

1. Clone this repository onto your local machine.
2. Open a terminal and go into the project directory.
3.

## Editing Documentation

With dependencies and initial setup out of the way, the following workflow can be used
for editing documentation.

1. Git pull to make sure you have latest version of documents.
2. Generally, you want to create a new Git branch if you don't already have an open
   branch.
3. Open a terminal and go to the project directory.
4. Run `poetry shell` to create a shell inside the Python virtual environment. This will
   make all project commands available in your terminal.
5. Run `make docs-server`. This will start up a local web server displaying the
   documentation on [http://127.0.0.1:8000](http://127.0.0.1:8000).
6. Edit the documentation in your text editor.
    * When you save any changes, the terminal will show some activitythen the browser
      will refresh to display your changes.
    * The terminal can also display errors/warnings if you have any syntax errors, so
      keep an eye on what it's saying. If your documentation page isn't refreshing
      correctly, it's probably due to an error.
7. When you are done, you can type `ctrl+c` to kill the web server and `ctrl+d` to exit
   the Poetry shell. (Or you can just close the terminal!)
8. Commit and push your changes.

## reStructured Text

The  markup language used is called reStructuredText. It is similar to Markdown but with
a slightly different syntax and support for a lot of rich formatting options such as
figures (with captions), tables, etc.

See [this
tutorial](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) to
get started.
