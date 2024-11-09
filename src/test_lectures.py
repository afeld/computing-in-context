from glob import glob
import re
import pytest

from .nb_helper import read_notebook


lecture_notebooks = glob("lecture_*.ipynb")
lecture_notebooks.sort()


def is_slide(cell):
    SLIDE_TYPES = ["slide", "subslide"]
    slide_type = cell.metadata.get("slideshow", {}).get("slide_type")
    return slide_type in SLIDE_TYPES


def num_slides(cells):
    """Return a weighted number of slides"""

    slides = [cell for cell in cells if is_slide(cell)]
    count = len(slides)

    has_intro = any(re.match("# Intro(duction)?s", slide.source) for slide in slides)
    if has_intro:
        count += 5

    num_exercises = sum(
        1 for slide in slides if re.match("#.+exercise", slide.source, re.IGNORECASE)
    )
    # let's say that each exercise is worth ten slides
    count += num_exercises * 10

    return count


# see counts with `pytest -s -k num_slides`
@pytest.mark.parametrize("file", lecture_notebooks)
def test_num_slides(file):
    """Ensure there are a reasonable number of slides"""

    notebook = read_notebook(file)

    if file in ["lecture_20.ipynb", "lecture_21.ipynb"]:
        pytest.xfail("In progress")
    # the various pieces of the lecture can be scaled appropriately
    if file == "lecture_25.ipynb":
        pytest.xfail("The various pieces of the lecture can be scaled appropriately")

    slide_count = num_slides(notebook.cells)
    print(f"{file}: {slide_count} slides")
    assert 30 <= slide_count <= 40


@pytest.mark.parametrize("file", lecture_notebooks)
def test_no_attendance(file):
    notebook = read_notebook(file)

    for cell in notebook.cells:
        if cell.cell_type == "markdown":
            assert "attendance" not in cell.source.lower()
