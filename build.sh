#!/bin/bash

set -e
set -x


jupyter-book clean .
# https://jupyterbook.org/en/stable/advanced/sphinx.html#enable-a-custom-sphinx-builder-from-the-cli
# https://sublime-and-sphinx-guide.readthedocs.io/en/latest/references.html#test-external-links
jupyter-book build --builder=linkcheck .

# check for Jinja tags, copied from Python for Public Policy
git ls-files '*.md' '*.ipynb' | xargs grep -q -E '\{\{|\{%' && exit 1 || echo "No Jinja tags found"

pytest
