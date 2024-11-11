from glob import glob

import pytest

from .nb_helper import is_code_cell, read_notebook


lab_notebooks = glob("lab_[0-9].ipynb") + glob("lab_[0-9][0-9].ipynb")
lab_notebooks.sort()


@pytest.mark.parametrize("file", lab_notebooks)
def test_lab_outputs_cleared(file):
    notebook = read_notebook(file)

    for cell in notebook.cells:
        if is_code_cell(cell):
            assert (
                cell.outputs == []
            ), f"Output should be cleared. Cell:\n\n{cell.source}\n"


@pytest.mark.parametrize("file", lab_notebooks)
def test_boilerplate(file):
    notebook = read_notebook(file)

    boilerplate = "_[General notebook information](https://computing-in-context.afeld.me/notebooks.html)_"
    assert any(
        boilerplate in cell.source for cell in notebook.cells
    ), "General assignment info is missing from lab"
