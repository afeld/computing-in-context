all: site open test lint

setup:
	python -m venv .venv
	. .venv/bin/activate && \
	pip install -r requirements.txt

update:
	. .venv/bin/activate && \
	pip install --upgrade pip && \
	pip install --upgrade -r requirements.txt

lab:
	jupyter lab

clean:
	rm *.slides.html || true
	jupyter-book clean .

quick:
	# https://jupyterbook.org/v1/content/references.html#check-for-missing-references
	# https://jupyterbook.org/v1/advanced/sphinx.html#enable-a-custom-sphinx-builder-from-the-cli
	jupyter-book build -W -n --keep-going .

open_site:
	open _build/html/index.html

site: clean quick open_site

linkcheck:
	# https://sublime-and-sphinx-guide.readthedocs.io/en/latest/references.html#test-external-links
	jupyter-book build -W -n --keep-going --builder=linkcheck .

open:
	/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome _build/html/index.html

# https://nbconvert.readthedocs.io/en/latest/usage.html#convert-revealjs
slides:
	jupyter nbconvert --to slides \
		--SlidesExporter.reveal_scroll=True \
		--TemplateExporter.extra_template_basedirs=_templates \
		--template=reveal-with-css \
		--post serve $(notebook)

test:
	pytest

lint:
	ruff check

format:
	ruff format *.ipynb src
