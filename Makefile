setup:
	uv sync

update:
	uv lock --upgrade
	uv sync

lab:
	uv run jupyter lab

site:
	cd pages && \
	uv run jupyter book start

clean:
	cd pages && \
	uv run jupyter book clean -y

# create redirects from old URL structure
# https://github.com/jupyter-book/jb1-redirect-generator
html:
	cd pages && \
	uv run jupyter book build --html && \
	uv run python generate_redirects.py --base-url https://computing-in-context.afeld.me/

# https://nbconvert.readthedocs.io/en/latest/usage.html#convert-revealjs
# Serves from the repo root rather than using `--post serve`, which only serves the notebook's directory, so the CSS and `../img` paths wouldn't resolve.
slides:
	uv run jupyter nbconvert --to slides \
		--SlidesExporter.reveal_scroll=True \
		--TemplateExporter.extra_template_basedirs=_templates \
		--template=reveal-with-css $(notebook)
	@echo "Serving at http://localhost:8000/$(notebook:.ipynb=.slides.html)"
	uv run python -m http.server 8000

test:
	uv run pytest

lint:
	uv run ruff check

format:
	uv run ruff format *.ipynb src
