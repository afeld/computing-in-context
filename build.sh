#!/bin/bash

set -e
set -x


jupyter-book clean .
# https://jupyterbook.org/en/stable/advanced/sphinx.html#enable-a-custom-sphinx-builder-from-the-cli
# https://sublime-and-sphinx-guide.readthedocs.io/en/latest/references.html#test-external-links
jupyter-book build --builder=linkcheck .

pytest
