#!/bin/bash

set -e
set -x


# https://jupyterbook.org/en/stable/content/references.html#check-for-missing-references
# https://jupyterbook.org/en/stable/advanced/sphinx.html#enable-a-custom-sphinx-builder-from-the-cli
# https://sublime-and-sphinx-guide.readthedocs.io/en/latest/references.html#test-external-links
jupyter-book build --all -W -n --keep-going --builder=linkcheck .

pytest
