#!/bin/bash

set -e
set -x


jupyter-book clean .
jupyter-book build .

pytest
