browser := chrome

all: site open test lint

setup:
	# https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file
	# https://mamba.readthedocs.io/
	mamba env create --file environment.yml

update:
	mamba env update --file environment.yml --prune

lab:
	jupyter lab --browser $(browser)

clean:
	jupyter-book clean .

quick:
	jupyter-book build -W -n --keep-going .

site: clean
	# https://jupyterbook.org/en/stable/content/references.html#check-for-missing-references
	# https://jupyterbook.org/en/stable/advanced/sphinx.html#enable-a-custom-sphinx-builder-from-the-cli
	jupyter-book build -W -n --keep-going .

linkcheck:
	# https://sublime-and-sphinx-guide.readthedocs.io/en/latest/references.html#test-external-links
	jupyter-book build -W -n --keep-going --builder=linkcheck .

open:
	/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome _build/html/index.html

slides:
	jupyter nbconvert --to slides \
		--SlidesExporter.reveal_scroll=True \
		--ServePostProcessor.browser $(browser) \
		--post serve lecture_$(lec).ipynb

test:
	pytest

lint:
	ruff check

format:
	ruff format *.ipynb src
