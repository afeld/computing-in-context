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
	# https://jupyterbook.org/en/stable/content/references.html#check-for-missing-references
	# https://jupyterbook.org/en/stable/advanced/sphinx.html#enable-a-custom-sphinx-builder-from-the-cli
	jupyter-book build -W -n --keep-going .

site: clean quick
	open _build/html/index.html

linkcheck:
	# https://sublime-and-sphinx-guide.readthedocs.io/en/latest/references.html#test-external-links
	jupyter-book build -W -n --keep-going --builder=linkcheck .

open:
	/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome _build/html/index.html

# https://nbconvert.readthedocs.io/en/latest/usage.html#convert-revealjs
slides:
	jupyter nbconvert --to slides \
		--SlidesExporter.reveal_scroll=True \
		--post serve lecture_$(lec).ipynb

test:
	pytest

lint:
	ruff check

format:
	ruff format *.ipynb src
