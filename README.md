# Computing in Context course site

[![Documentation Status](https://readthedocs.org/projects/computing-in-context/badge/?version=latest)](https://computing-in-context.afeld.me/?badge=latest)

Built using [Jupyter Book](https://jupyterbook.org/).

## Setup

1. [Install the dependencies](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) - using [mamba](https://mamba.readthedocs.io/) is recommended.

   ```sh
   mamba install -f environment.yml
   ```

1. [Activate the environment.](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment)

   ```sh
   conda activate computing-in-context
   ```

## [Building the site](https://jupyterbook.org/en/stable/basics/build.html#build-via-the-command-line)

```sh
jupyter-book build .
```

## [Starting Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html)

```sh
jupyter lab --no-browser
```
