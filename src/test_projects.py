import pytest

from src.nb_helper import PAGES_DIR

projects = list(PAGES_DIR.glob("project_*.md"))


@pytest.mark.parametrize("file", projects)
def test_submit_info(file):
    with open(file) as f:
        content = f.read()
    assert "notebooks.md#submission" in content
