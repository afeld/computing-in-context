# Computing in Context course site

[![Documentation Status](https://readthedocs.org/projects/computing-in-context/badge/?version=latest)](https://computing-in-context.afeld.me/?badge=latest)

Built using [Jupyter Book](https://jupyterbook.org/).

## Setup

```sh
make setup
```

## [Building the site](https://jupyterbook.org/en/stable/basics/build.html#build-via-the-command-line)

Building the site from scratch and running tests:

```sh
make
```

If just testing a change within a page:

```sh
make quick
```

## [Starting Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html)

```sh
make lab
```

## Slides

### Presenting

```sh
make slides lec=N
```

### Creating/editing

Most of the notebooks in this repository are also slide decks, with the Slide Type specified as cell metadata. In JupyterLab:

![Slide type selection](img/slide_type.png)

In general, the presentations are organized as:

- One intro Slide per topic, then Sub-Slides that go into details
- Slides have an H2, while Sub-Slides have an H3+

Easiest to understand this by viewing the presentation.

## Merging notebooks

[nbmerge](https://github.com/jbn/nbmerge?tab=readme-ov-file#usage) seems to be easier than copying across them.
