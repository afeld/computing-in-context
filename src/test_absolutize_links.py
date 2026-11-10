import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "pages"))

from absolutize_links import absolutize

BASE = "https://example.com"
ASSETS = {"img/logo.svg": "build/logo-abc123.svg"}


def test_page_links():
    assert absolutize("[x](lab_8.ipynb)", BASE, ASSETS) == "[x](https://example.com/lab-8/)"
    assert absolutize("[x](notebooks.md#installing-packages)", BASE, ASSETS) == "[x](https://example.com/notebooks/#installing-packages)"
    assert absolutize("[x](index.md)", BASE, ASSETS) == "[x](https://example.com/)"


def test_slide_html_links():
    assert absolutize('<a href="lab_8.ipynb">x</a>', BASE, ASSETS) == '<a href="https://example.com/lab-8/">x</a>'


def test_images():
    assert absolutize("![x](img/logo.svg)", BASE, ASSETS) == "![x](https://example.com/build/logo-abc123.svg)"
    assert absolutize('<img src="img/logo.svg">', BASE, ASSETS) == '<img src="https://example.com/build/logo-abc123.svg">'


def test_leaves_other_links_alone():
    text = "[a](https://x.org/a.md) [b](#anchor) [c](mailto:a@b.co) [d](unknown.png)"
    assert absolutize(text, BASE, ASSETS) == text
