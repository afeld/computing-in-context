import ast
import re
from pathlib import Path
from typing import Union

import pytest
from markdown_it import MarkdownIt
from markdown_it.token import Token

from .nb_helper import NOTEBOOKS, is_code_cell, is_h1, is_markdown, is_python, read_notebook


def check_metadata(notebook, expected_kernel):
    metadata = notebook.metadata
    runtime = metadata.kernelspec.name

    assert runtime == expected_kernel
    assert metadata.language_info.version.startswith("3.")


def check_file(file: Path, expected_kernel="python3"):
    notebook = read_notebook(file)
    check_metadata(notebook, expected_kernel)


@pytest.mark.parametrize("notebook", NOTEBOOKS)
def test_class_notebooks(notebook):
    check_file(notebook)


@pytest.mark.parametrize("file", NOTEBOOKS)
def test_one_h1(file):
    notebook = read_notebook(file)
    h1s = [cell.source.split("\n")[0] for cell in notebook.cells if is_h1(cell)]
    assert len(h1s) == 1


def get_slide_type(cell) -> str:
    return cell.metadata.get("slideshow", {}).get("slide_type", "")


def has_slides(notebook):
    return any(get_slide_type(cell) == "slide" for cell in notebook.cells)


@pytest.mark.parametrize("file", NOTEBOOKS)
def test_heading_levels(file):
    notebook = read_notebook(file)

    if not has_slides(notebook):
        pytest.skip("No slides")

    for cell in notebook.cells:
        source = cell.source
        if is_markdown(cell) and source.startswith("#"):
            # it's a heading

            slide_type = get_slide_type(cell)

            # slides should start with an H1 or H2
            if slide_type == "slide":
                assert source.startswith(("# ", "## ")), "should be an H1 or H2"
            # sub-slides should start with an H3+
            elif slide_type == "subslide":
                assert source.startswith("###"), "should be H3+"

            # checking the inverse of the above

            # H2 should always be a slide
            if source.startswith("## "):
                assert slide_type in ["slide", "skip"], f"should be a slide:\n\n{source}\n"
            # H3+ should always be a sub-slide
            if source.startswith("###"):
                assert slide_type in ["subslide", "skip"], f"should be a subslide:\n\n{source}\n"


def check_link(token: Token, parent: Token | None = None):
    if token.type == "link_open":
        href = str(token.attrGet("href"))
        # escaped Jinja2 tags
        if not re.match(r"http|#|%7B%7B", href):
            source = parent.content if parent else token.content
            assert False, f"Link should be absolute. Text:\n\n{source}\n"


@pytest.mark.parametrize("file", NOTEBOOKS)
def test_links(file):
    """To ensure that links work from the coding environment, ensure all links are absolute."""

    notebook = read_notebook(file)

    has_code_cells = any(is_code_cell(cell) for cell in notebook.cells)
    if not has_code_cells:
        pytest.skip("No code cells; unlikely anyone will download")

    md = MarkdownIt()
    for cell in notebook.cells:
        if is_markdown(cell):
            source = cell.source
            tokens = md.parse(source)
            for token in tokens:
                check_link(token)
                if token.type == "inline":
                    for child in token.children:  # type: ignore
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
            method = node.func.attr  # type: ignore

            if method == "get_trendline_results":
                # `title` not applicable
                return

            assert "title" in args, f"call to `{method}()` missing a `title`"


def get_tags(cell):
    return cell.metadata.get("tags", [])


@pytest.mark.parametrize("file", NOTEBOOKS)
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


def num_lines(output):
    html = output.data.get("text/html")
    if html:
        # rows of table
        return html.count("<tr")

    text = output.data["text/plain"]
    return text.count("\n")


@pytest.mark.parametrize("file", NOTEBOOKS)
def test_long_outputs_scrolled(file):
    notebook = read_notebook(file)

    for cell in notebook.cells:
        if is_python(cell):
            for output in cell.outputs:
                if output.output_type in ["display_data", "execute_result"]:
                    num_rows = num_lines(output)
                    if num_rows > 30:
                        # if not set, the notebook will automatically scroll
                        assert cell.metadata.get("scrolled"), f"Long output should be scrollable. Cell:\n\n{cell.source}\n"


@pytest.mark.parametrize("file", NOTEBOOKS)
def test_no_python_public_policy_tags(file):
    notebook = read_notebook(file)

    for cell in notebook.cells:
        tags = get_tags(cell)
        for tag in ["columbia-only", "nyu-only"]:
            assert tag not in tags, f"Notebook contains a `{tag}` tag. Cell:\n\n{cell.source}\n"


@pytest.mark.parametrize("file", NOTEBOOKS)
def test_plotly_renderer_configured(file):
    """If a notebook imports plotly, ensure it sets the correct renderer.

    https://computing-in-context.afeld.me/notebooks.html#jupyter-book"""

    notebook = read_notebook(file)

    is_slideshow = has_slides(notebook)
    imports_plotly = False
    has_renderer_config = False

    for cell in notebook.cells:
        if is_python(cell):
            source = cell.source

            if "import plotly" in source:
                imports_plotly = True

            if 'pio.renderers.default = "notebook_connected+plotly_mimetype"' in source:
                has_renderer_config = True

                if is_slideshow:
                    assert get_slide_type(cell) == "skip", "Renderer config cell should have slide_type 'skip'"

    if imports_plotly:
        assert has_renderer_config, "Notebook imports plotly but doesn't set `pio.renderers.default = 'notebook_connected+plotly_mimetype'`"
