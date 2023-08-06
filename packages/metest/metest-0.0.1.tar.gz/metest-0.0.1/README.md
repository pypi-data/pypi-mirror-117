# metest
Test, check and compare logs and data from meteorological computations. 

# Usage
Submodules can be imported, but this software is designed to be used as a CLI (Command-Line-Interface), by calling the `__main__` module.

`python -m metest`: Prints a help message

`python -m metest logmetric`: Calls the logmetric submodule and prints a help message (as flags are needed for this command to work)

`python -m metest logmetric -m harmonie --individual -f /path/to/log`: Computes standard metrics on a single logfile from Harmonie

# Documentation
Documentation is auto-build from in-line code using sphinx: dmidk.github.io/metest/

# Prerequisites
*metest* is a script tool based on python. Dependencies is defined in `metest.yml` and a python environment can be made using (mini)conda:

`conda env create -f metest.yml`

# For developers

## Build documentation
```shell
cd doc
sphinx-apidoc -f --private --ext-autodoc --separate -o . ../metest/
make html
```
The html source files goes into `doc/_build/html`