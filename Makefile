book_dir := site/

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
	jupyter-book clean $(book_dir)

quick:
	cd $(book_dir) && \
		jupyter-book build -W -n .

site: clean quick
	open _build/html/index.html

linkcheck:
	# https://sublime-and-sphinx-guide.readthedocs.io/en/latest/references.html#test-external-links
	cd $(book_dir) && \
		jupyter-book build -W -n --keep-going --builder=linkcheck .

open:
	/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome $(book_dir)/_build/html/index.html

slides:
	jupyter nbconvert --to slides \
		--SlidesExporter.reveal_scroll=True \
		--post serve $(book_dir)/lecture_$(lec).ipynb

test:
	pytest

lint:
	ruff check

format:
	ruff format $(book_dir)/*.ipynb src
