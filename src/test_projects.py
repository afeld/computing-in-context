from glob import glob

import pytest

projects = glob("project_*.md")


@pytest.mark.parametrize("file", projects)
def test_submit_info(file):
    with open(file) as f:
        content = f.read()
    assert "notebooks.md#submission" in content
