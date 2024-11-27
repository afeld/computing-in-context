from glob import glob

import pytest

projects = glob("project_*.md")


@pytest.mark.parametrize("file", projects)
def test_rubric(file):
    with open(file) as f:
        content = f.read()
    assert "# Rubric" in content
