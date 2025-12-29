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
	jupyter book start

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
