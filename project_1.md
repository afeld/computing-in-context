# Project 1

In this project, you will:

- Get the feel of working in a Jupyter Notebook
- Work with a new dataset
- Practice working with data in:
  - Pure Python
  - pandas

## Steps

For all steps, explain what you're doing and what you found using [Markdown cells](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html).

1. Find a dataset you aren't familiar with.
   - It must have:
     - At least one numeric column
     - Between one thousand and one million rows
       - If it's larger than that, you can filter it down.
   - See [this list of open data portals](https://python-public-policy.afeld.me/en/columbia/final_project/resources.html#open-data-portals).
   - Don't spend too long on this step.
1. Create a new notebook.
1. In pure Python (not using pandas, a spreadsheet program, etc):
   1. Read in the data.
   1. If there's more than one numeric column, pick one.
   1. Compute:
      - The mean
      - The median
      - The mode
1. Repeat previous step using pandas.
1. Create a data visualization in pure Python. More details below.
1. [Submit via Gradescope.](https://courseworks2.columbia.edu/courses/207091/assignments/1345872)

## Data visualization

- Using plain text ([ASCII](https://www.techtarget.com/whatis/definition/ASCII-American-Standard-Code-for-Information-Interchange), via `print()`) is strongly recommended, but you can get fancy and use [HTML](https://mkonicek.medium.com/simple-tip-how-to-use-html-in-jupyter-notebook-eef14e81dbc5) if you want.
- The data can come from pandas, but you should be writing the drawing code from scratch in pure Python.
  - In other words, don't use [`plot()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html), [plotly](https://plotly.com/python/), etc.
- It should not be hard-coded.
  - In other words, it should work if the dataset got additional rows, values were changed, etc.
- You can be creative here, but **start simple**.

### Example

Data that looks like this:

| Year | Count |
| ---- | ----- |
| 2014 | 3     |
| 2015 | 5     |
| 2016 | 4     |

could be turned into a vertical [sparkline](https://en.wikipedia.org/wiki/Sparkline) that looks like this:

```
2014: ***
2015: *****
2016: ****
```
