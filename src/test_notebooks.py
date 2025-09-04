import ast
from glob import glob
from typing import Union
from markdown_it import MarkdownIt
from markdown_it.token import Token
import pytest
import re
from .nb_helper import is_h1, is_markdown, is_python, read_notebook


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


def get_slide_type(cell) -> str:
    return cell.metadata.get("slideshow", {}).get("slide_type")


@pytest.mark.parametrize("file", notebooks)
def test_heading_levels(file):
    notebook = read_notebook(file)

    if not any(get_slide_type(cell) == "slide" for cell in notebook.cells):
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


@pytest.mark.parametrize("file", notebooks)
def test_links(file):
    """To ensure that links work from the coding environment, ensure all links are absolute."""

    if file == "lecture_23.ipynb":
        pytest.skip("Unlikely students will download this notebook, so ok that links are relative")

    md = MarkdownIt()

    notebook = read_notebook(file)
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
                        assert cell.metadata.get("scrolled"), f"Long output should be scrollable. Cell:\n\n{cell.source}\n"


@pytest.mark.parametrize("file", notebooks)
def test_no_python_public_policy_tags(file):
    notebook = read_notebook(file)

    for cell in notebook.cells:
        tags = get_tags(cell)
        for tag in ["columbia-only", "nyu-only"]:
            assert tag not in tags, f"Notebook contains a `{tag}` tag. Cell:\n\n{cell.source}\n"
