from glob import glob
import re
import pytest

from .nb_helper import is_code_cell, is_markdown, read_notebook


lecture_notebooks = glob("lecture_[0-9][0-9].ipynb")
lecture_notebooks.sort()


def slide_type(cell):
    return cell.metadata.get("slideshow", {}).get("slide_type")


def is_slide(cell):
    SLIDE_TYPES = ["slide", "subslide"]
    return slide_type(cell) in SLIDE_TYPES


def num_slides(cells):
    """Return a weighted number of slides"""

    slides = [cell for cell in cells if is_slide(cell)]
    count = len(slides)

    has_intro = any(re.match("# Intro(duction)?s", slide.source) for slide in slides)
    if has_intro:
        count += 5

    num_exercises = sum(1 for slide in slides if "# In-class exercise" in slide.source)
    # let's say that each exercise is worth this many slides
    count += num_exercises * 15

    return count


# see counts with `pytest -s -k num_slides`
@pytest.mark.parametrize("file", lecture_notebooks)
def test_num_slides(file):
    """Ensure there are a reasonable number of slides"""

    notebook = read_notebook(file)

    slide_count = num_slides(notebook.cells)
    print(f"{file}: {slide_count} slides")

    if "exercise" in file:
        pytest.skip("Not expected to be a full lecture")
    elif file == "lecture_20.ipynb":
        assert slide_count <= 28, "This exercise is long"
    elif file == "lecture_23.ipynb":
        assert slide_count <= 30, "This is mostly live demo"
    elif file == "lecture_25.ipynb":
        pytest.skip("The various pieces of the lecture can be scaled appropriately")
    else:
        assert slide_count >= 30, "Too few slides"
        assert slide_count <= 40, "Too many slides"


@pytest.mark.parametrize("file", lecture_notebooks)
def test_no_attendance(file):
    notebook = read_notebook(file)

    for cell in notebook.cells:
        if is_markdown(cell):
            assert "attendance" not in cell.source.lower()


@pytest.mark.parametrize("file", lecture_notebooks)
def test_hidden_imports(file):
    notebook = read_notebook(file)

    for cell in notebook.cells:
        if is_code_cell(cell):
            lines = cell.source.splitlines()

            imports_only = all(line.startswith("import ") for line in lines)
            if imports_only:
                assert slide_type(cell) == "skip", f"imports should be hidden:\n\n{cell.source}\n"


@pytest.mark.parametrize("file", lecture_notebooks)
def test_heading_slide_types(file):
    notebook = read_notebook(file)
    for cell in notebook.cells:
        meta = cell.metadata
        source = cell.source
        if is_markdown(cell) and "slideshow" in meta and source.startswith("#"):
            slide_type = meta["slideshow"]["slide_type"]

            # checking the inverse of test_notebooks::test_heading_levels()

            # H2 should always be a slide
            if source.startswith("## "):
                assert slide_type in ["slide", "skip"], f"should be a slide:\n\n{source}\n"
            # H3+ should always be a sub-slide
            if source.startswith("###"):
                assert slide_type in ["subslide", "skip"], f"should be a subslide:\n\n{source}\n"
