# Lab 9 guide

**Goal:** Ensure students are set up for the rest of the course and comfortable using Jupyter.

## Setup

Assumes students already have [Python 3](https://www.python.org/downloads/) and [VSCode](https://code.visualstudio.com/download) installed. Walk them through the following:

1. Create a folder (a.k.a. directory) for this class — like `computing-in-context/` — if they don't have one already.
1. [Open the working folder in VSCode.](https://code.visualstudio.com/docs/getstarted/getting-started#_open-a-folder-in-vs-code)
1. [Open a terminal.](https://code.visualstudio.com/docs/terminal/getting-started)
1. In the terminal, [create a virtual environment](https://docs.python.org/3/library/venv.html#creating-virtual-environments).

   ```sh
   python -m venv .venv
   ```

1. [Install the following packages.](notebooks.md#installing-packages)

   ```
   ipykernel
   pandas
   plotly

   # needed for plotly
   nbformat
   statsmodels
   ```

## Try it!

Have the do the following in VSCode:

1. [Create a `lab_9_example.ipynb` notebook.](https://code.visualstudio.com/docs/datascience/jupyter-notebooks#_create-or-open-a-jupyter-notebook)
1. Walk them through the Jupyter interface.
1. [Run](https://code.visualstudio.com/docs/datascience/jupyter-notebooks#_running-cells) [this example](https://plotly.com/python/linear-fits/#Linear-fit-trendlines-with-Plotly-Express) in that notebook.
1. Redo it, showing each step in their own cell:
   1. Data loading
   1. Displaying the `df`
   1. Creating the chart

_FYI `px.data.tips()` loads one of [Plotly's sample datasets](https://plotly.com/python-api-reference/generated/plotly.express.data.html). They don't need that when plotting other datasets._

## Walkthrough

1. Walk through [working with notebooks from course site](notebooks.md#downloading-notebooks).
1. Reiterate [Jupyter basics](lecture_16.ipynb#jupyter-basics).
1. Try some Markdown.
1. Talk through [Lab 9](lab_9.ipynb).
