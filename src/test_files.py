from glob import glob

import pytest

files = glob("*.ipynb") + glob("*.md")


@pytest.mark.parametrize("file", files)
def test_no_jinja(file):
    with open(file) as f:
        content = f.read()

    assert "{{" not in content
    assert "{%" not in content
