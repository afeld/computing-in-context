from glob import glob
import re

import pytest

JINJA_EXPRESSION = re.compile(r"{{ ?\w+ ?}}")

files = glob("*.ipynb") + glob("*.md")


@pytest.mark.parametrize("file", files)
def test_no_jinja(file):
    with open(file) as f:
        content = f.read()

    assert JINJA_EXPRESSION.search(content) is None
    assert "{%" not in content
