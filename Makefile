book_dir := site/

all: site open test lint

setup:
	# https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-channels.html#strict-channel-priority
	conda config --set channel_priority strict

	# https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file
	# https://mamba.readthedocs.io/
	mamba env create --file environment.yml

update:
	mamba env update --file environment.yml --prune

lab:
	jupyter lab

clean:
	rm *.slides.html || true
	jupyter-book clean $(book_dir)

quick:
	cd $(book_dir) && \
		jupyter-book build -W -n .

site: clean quick

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
