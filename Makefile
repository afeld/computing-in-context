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

site:
	cd pages && \
	jupyter book start

# create redirects from old URL structure
# https://github.com/jupyter-book/jb1-redirect-generator
html:
	. .venv/bin/activate && \
	cd pages && \
	jupyter book build --html && \
	wget -N https://raw.githubusercontent.com/jupyter-book/jb1-redirect-generator/main/generate_redirects.py && \
	python generate_redirects.py --base-url https://computing-in-context.afeld.me/

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
