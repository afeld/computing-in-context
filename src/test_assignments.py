from glob import glob

import pytest

assignments = glob("lab_*.ipynb") + glob("project_*.md")


@pytest.mark.parametrize("file", assignments)
def test_submit_info(file):
    with open(file) as f:
        content = f.read()
    assert "submit via gradescope" in content.lower()
