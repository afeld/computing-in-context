from glob import glob
import pytest

from .nb_helper import read_notebook


lecture_notebooks = glob("lecture_*.ipynb")
lecture_notebooks.sort()


def is_slide(cell):
    SLIDE_TYPES = ["slide", "subslide"]
    slide_type = cell.metadata.get("slideshow", {}).get("slide_type")
    return slide_type in SLIDE_TYPES


def num_slides(cells):
    slides = [cell for cell in cells if is_slide(cell)]
    return len(slides)


# see counts with `pytest -s -k num_slides`
@pytest.mark.parametrize("file", lecture_notebooks)
def test_num_slides(file):
    """Ensure there are a reasonable number of slides"""

    notebook = read_notebook(file)

    # the various pieces of the lecture can be scaled appropriately
    if file == "lecture_25.ipynb":
        pytest.xfail("The various pieces of the lecture can be scaled appropriately")

    slide_count = num_slides(notebook.cells)
    print(f"{file}: {slide_count} slides")
    assert 30 <= slide_count <= 40
