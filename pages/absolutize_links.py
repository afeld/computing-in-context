"""Rewrites relative links in the built notebook downloads to absolute URLs, so they still work once the .ipynb is saved elsewhere."""

import re
import sys
from pathlib import Path

import nbformat
from generate_redirects import sanitize_for_myst_url

# Markdown links/images `](target)` and HTML `src="target"` / `href="target"`
LINK = re.compile(r"""(\]\(|(?:src|href)=["'])([^)"'\s#]+)(#[^)"'\s]*)?""")


def absolutize(text: str, base_url: str, assets: dict[str, str]) -> str:
    """The text with relative page and image links made absolute."""
    base_url = base_url.rstrip("/")

    def replace(match: re.Match) -> str:
        prefix, target, fragment = match.group(1), match.group(2), match.group(3) or ""
        if target in assets:
            return f"{prefix}{base_url}/{assets[target]}{fragment}"
        path = Path(target)
        if path.suffix in (".md", ".ipynb") and not re.match(r"[a-z]+:", target):
            slug = sanitize_for_myst_url(str(path.with_suffix("")))
            url = f"{base_url}/" if slug == "index" else f"{base_url}/{slug}/"
            return f"{prefix}{url}{fragment}"
        return match.group(0)

    return LINK.sub(replace, text)


def find_assets(pages_dir: Path, built_dir: Path) -> dict[str, str]:
    """Maps source image paths (`img/foo.png`) to the hashed copies MyST emits under `build/`."""
    assets = {}
    for source in (pages_dir / "img").rglob("*.*"):
        hashed = re.compile(rf"{re.escape(source.stem)}-[0-9a-f]{{32}}{re.escape(source.suffix)}")
        built = sorted(p for p in (built_dir / "build").iterdir() if hashed.fullmatch(p.name))
        if built:
            assets[source.relative_to(pages_dir).as_posix()] = built[-1].relative_to(built_dir).as_posix()
    return assets


def main(pages_dir: Path, built_dir: Path, base_url: str) -> None:
    assets = find_assets(pages_dir, built_dir)
    for path in (built_dir / "build").glob("*.ipynb"):
        notebook = nbformat.read(path, as_version=4)
        for cell in notebook.cells:
            if cell.cell_type == "markdown":
                cell.source = absolutize(cell.source, base_url, assets)
        nbformat.write(notebook, path)
    # The slide decks are served from `build/`, so their relative links would resolve there.
    for path in (built_dir / "build").glob("*.slides.html"):
        path.write_text(absolutize(path.read_text(), base_url, assets))


if __name__ == "__main__":
    main(Path(__file__).parent, Path(sys.argv[2]), sys.argv[1])
