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

## Viewing slides

```sh
make slides lec=N
```

## Merging notebooks

[nbmerge](https://github.com/jbn/nbmerge?tab=readme-ov-file#usage) seems to be easier than copying across them.
