import ast
from glob import glob
from typing import Union
from markdown_it import MarkdownIt
from markdown_it.token import Token
import pytest
import re
from .nb_helper import is_code_cell, is_h1, is_markdown, is_python, read_notebook


def check_metadata(notebook, expected_kernel):
    metadata = notebook.metadata
    runtime = metadata.kernelspec.display_name

    # seems the asterisk is added for the "preferred kernel"
    assert runtime == expected_kernel or runtime == f"{expected_kernel} *"
    assert metadata.language_info.version.startswith("3.")


def check_file(file, expected_kernel="Python [conda env:computing-in-context]"):
    notebook = read_notebook(file)
    check_metadata(notebook, expected_kernel)


notebooks = glob("*.ipynb")
notebooks.sort()


@pytest.mark.parametrize("notebook", notebooks)
def test_class_notebooks(notebook):
    check_file(notebook)


@pytest.mark.parametrize("file", notebooks)
def test_one_h1(file):
    notebook = read_notebook(file)
    num_h1s = sum(is_h1(cell) for cell in notebook.cells)
    assert num_h1s == 1


@pytest.mark.parametrize("file", notebooks)
def test_heading_levels(file):
    notebook = read_notebook(file)
    for cell in notebook.cells:
        meta = cell.metadata
        source = cell.source
        if is_markdown(cell) and "slideshow" in meta and source.startswith("#"):
            # slide with a heading
            slide_type = meta["slideshow"]["slide_type"]
            if slide_type == "slide":
                assert source.startswith(("# ", "## ")), "should be an H1 or H2"
            elif slide_type == "subslide":
                assert source.startswith("###"), "should be H3+"


@pytest.mark.parametrize("file", notebooks)
def test_nested_lists(file):
    """JupyterBook's markdown parser doesn't support nested lists with two spaces."""

    notebook = read_notebook(file)
    for cell in notebook.cells:
        if is_markdown(cell):
            source = cell.source
            for line in source.splitlines():
                match = re.match(r"^( +)(-|\d\.)", line)
                if match:
                    num_spaces = len(match[1])
                    assert (
                        num_spaces % 3 == 0 or num_spaces % 4 == 0
                    ), f"Lists should be indented in multiples of three or four spaces. Text:\n\n{source}\n"


def check_link(token: Token, parent: Token = None):
    if token.type == "link_open":
        href = token.attrGet("href")
        # escaped Jinja2 tags
        if not re.match(r"http|#|%7B%7B", href):
            source = parent.content if parent else token.content
            assert False, f"Link should be absolute. Text:\n\n{source}\n"


@pytest.mark.parametrize("file", notebooks)
def test_links(file):
    """To ensure that links work from the coding environment, ensure all links are absolute."""

    md = MarkdownIt()

    notebook = read_notebook(file)
    for cell in notebook.cells:
        if is_markdown(cell):
            source = cell.source
            tokens = md.parse(source)
            for token in tokens:
                check_link(token)
                if token.type == "inline":
                    for child in token.children:
                        check_link(child, token)


def base_obj(node: ast.Call) -> Union[str, None]:
    """If this is a method call, return the name of the base object it was called on"""
    if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name):
        return node.func.value.id
    else:
        return None


class PlotChecker(ast.NodeVisitor):
    def visit_Call(self, node):
        if base_obj(node) == "px":
            args = [kw.arg for kw in node.keywords]
            method = node.func.attr

            if method == "get_trendline_results":
                # `title` not applicable
                return

            assert "title" in args, f"call to `{method}()` missing a `title`"


def get_tags(cell):
    return cell.metadata.get("tags", [])


@pytest.mark.parametrize("file", notebooks)
def test_chart_titles(file):
    """Make sure all charts have titles"""

    notebook = read_notebook(file)
    for cell in notebook.cells:
        tags = get_tags(cell)
        if "skip-plot-check" in tags or not is_python(cell):
            continue

        tree = ast.parse(cell.source)
        checker = PlotChecker()
        checker.visit(tree)


def is_slide(cell):
    SLIDE_TYPES = ["slide", "subslide"]
    slide_type = cell.metadata.get("slideshow", {}).get("slide_type")
    return slide_type in SLIDE_TYPES


def num_slides(cells):
    slides = [cell for cell in cells if is_slide(cell)]
    return len(slides)


lecture_notebooks = glob("lecture_*.ipynb")
lecture_notebooks.sort()


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


def num_lines(output):
    html = output.data.get("text/html")
    if html:
        # rows of table
        return html.count("<tr")

    text = output.data["text/plain"]
    return text.count("\n")


@pytest.mark.parametrize("file", notebooks)
def test_long_outputs_scrolled(file):
    notebook = read_notebook(file)

    for cell in notebook.cells:
        if is_python(cell):
            for output in cell.outputs:
                if output.output_type in ["display_data", "execute_result"]:
                    num_rows = num_lines(output)
                    if num_rows > 30:
                        # if not set, the notebook will automatically scroll
                        assert cell.metadata.get(
                            "scrolled"
                        ), f"Long output should be scrollable. Cell:\n\n{cell.source}\n"


lab_notebooks = glob("lab_*.ipynb")
lab_notebooks.sort()


@pytest.mark.parametrize("file", lab_notebooks)
def test_lab_outputs_cleared(file):
    notebook = read_notebook(file)

    for cell in notebook.cells:
        if is_code_cell(cell):
            assert (
                cell.outputs == []
            ), f"Output should be cleared. Cell:\n\n{cell.source}\n"
