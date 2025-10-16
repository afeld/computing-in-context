# Lab 8 guide

**Goal:** Ensure students are set up for the rest of the course and comfortable using Jupyter.

## Setup

Assumes you already have Python 3 and VSCode installed.

1. Create a folder (a.k.a. directory) for this class — like `computing-in-context/` — if you don't have one already.
1. [Open the working folder in VSCode.](https://code.visualstudio.com/docs/getstarted/getting-started#_open-a-folder-in-vs-code)
1. [Open a terminal.](https://code.visualstudio.com/docs/terminal/getting-started)
1. In the terminal, [create a virtual environment](https://docs.python.org/3/library/venv.html#creating-virtual-environments).

   ```sh
   python -m venv .venv
   ```

1. [Install the following packages.](notebooks.md#installing-packages)

   ```
   jupyterlab
   pandas
   plotly

   # needed for plotly
   nbformat
   statsmodels
   ```

## Try it!

1. Create a `lab_8.ipynb` notebook.
1. Run [this example](https://plotly.com/python/linear-fits/#Linear-fit-trendlines-with-Plotly-Express) in that notebook.

_FYI `px.data.tips()` loads one of [Plotly's sample datasets](https://plotly.com/python-api-reference/generated/plotly.express.data.html). You don't need that when plotting other datasets._

## Walkthrough

1. Walk through [working with notebooks from course site](notebooks.md#downloading-notebooks).
1. Reiterate [Jupyter basics](lecture_15.ipynb#jupyter-basics).
1. Try some Markdown.
1. Talk through [Lab 8](lab_8.ipynb).
