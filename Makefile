browser := chrome

all: site open test

lab:
	jupyter lab --browser $(browser)

quick:
	jupyter-book build -W -n --keep-going .

site:
	# https://jupyterbook.org/en/stable/content/references.html#check-for-missing-references
	# https://jupyterbook.org/en/stable/advanced/sphinx.html#enable-a-custom-sphinx-builder-from-the-cli
	# https://sublime-and-sphinx-guide.readthedocs.io/en/latest/references.html#test-external-links
	jupyter-book build --all -W -n --keep-going --builder=linkcheck .

open:
	/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome _build/html/index.html

slides:
	jupyter nbconvert --to slides \
		--SlidesExporter.reveal_scroll=True \
		--ServePostProcessor.browser $(browser) \
		--post serve lecture_$(lec).ipynb

test:
	pytest
