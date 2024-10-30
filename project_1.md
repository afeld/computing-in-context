# Project 1

In this project, you will:

- Work with a new dataset
- Practice working with data in:
  - pandas
  - [The Python standard library](https://docs.python.org/3/library/index.html)

## Steps

For all steps, explain what you're doing and what you found using [Markdown cells](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html).

1. Find a dataset you aren't familiar with.
   - It must have:
     - At least one numeric column
     - Between one thousand and one million rows
       - If it's larger than that, you can filter it down.
   - See [this list of open data portals](https://python-public-policy.afeld.me/en/columbia/final_project/resources.html#open-data-portals).
   - Don't spend too long on this step.
1. If there's more than one numeric column, pick one.
1. Create a new notebook.
1. Using pandas:
   1. Read in the data.
   1. Compute:
      - The mean
      - The median
      - The mode
1. Repeat the previous step using only the Python standard library ("the hard way" - not using pandas, a spreadsheet program, etc).
   - Hint: Use a [dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) to keep track of value counts.
1. Create a data visualization, following the instructions below.
1. [Submit via Gradescope.](https://courseworks2.columbia.edu/courses/207091/assignments/1345872)

## Data visualization

- The data/calculations can come through pandas, but the drawing code should only use the Python standard library.
  - In other words, don't use [`plot()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html), [plotly](https://plotly.com/python/), or any other external packages.
- `print()`ing strings will probably be easiest, but you can get fancy and [generate HTML](https://mkonicek.medium.com/simple-tip-how-to-use-html-in-jupyter-notebook-eef14e81dbc5) if you want.
- It should not be [hard-coded](https://en.wikipedia.org/wiki/Hard_coding).
  - In other words, if the dataset got additional rows, had values changed, etc., it should display those appropriately.
- It should look decent on a narrow (11") laptop screen.
- You can be creative here, but **start simple**.
  - Use only one or two columns of your dataset.

### Example

Data that looks like this:

| Year | Count |
| ---- | ----- |
| 2014 | 3,162 |
| 2015 | 4,985 |
| 2016 | 4,091 |

could be turned into a [sparkline](https://en.wikipedia.org/wiki/Sparkline) that looks like this:

```
2014: ***
2015: *****
2016: ****
```

### Tips

- Making your chart vertical (one data point per line) will probably be easier than doing something horizontal.
- [Repeating strings](https://phoenixnap.com/kb/python-repeat-string)
- ["Rewinding" a CSV](https://stackoverflow.com/questions/431752/python-csv-reader-how-do-i-return-to-the-top-of-the-file)
- [Python strings can contain Unicode](https://docs.python.org/3/howto/unicode.html#the-string-type), including [emoji](https://getemoji.com/) 📈✨
