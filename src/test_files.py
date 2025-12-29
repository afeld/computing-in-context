import itertools
import re

import pytest

from src.nb_helper import NOTEBOOKS, PAGES_DIR

JINJA_EXPRESSION = re.compile(r"{{ ?\w+ ?}}")

files = list(itertools.chain(NOTEBOOKS, PAGES_DIR.glob("*.md")))


def get_content(file: str):
    with open(file) as f:
        return f.read()


@pytest.mark.parametrize("file", files)
def test_no_jinja(file):
    content = get_content(file)
    assert JINJA_EXPRESSION.search(content) is None, "Jinja expression found"
    assert "{%" not in content, "Jinja statement found"


@pytest.mark.parametrize("file", files)
def test_no_python_public_policy_stuff(file):
    # https://github.com/afeld/python-public-policy/blob/main/extras/lib/school.py
    words = [
        "Brightspace",
        "JupyterHub",
        "grader",
    ]

    content = get_content(file)
    for word in words:
        assert word not in content
