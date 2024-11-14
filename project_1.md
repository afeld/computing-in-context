# Project 1

In this project, you will:

- Work with a new dataset
- Practice working with data in:
  - pandas
  - [The Python standard library](https://docs.python.org/3/library/index.html)

## Steps

1. Read the [general Project information](notebooks.md#projects).
1. Find a dataset.
   - It must have:
     - At least one numeric column
     - Between one thousand and one million rows
       - If it's larger than that, you can filter it down.
   - Don't spend too long on this step.
1. If there's more than one numeric column, pick one.
1. Create a new notebook.
1. Using pandas:
   1. Read in the data.
   1. Compute:
      - The mean
      - The median
      - The mode
1. Repeat the previous step using only the Python standard library, a.k.a. [the hard way](#the-hard-way).
1. Create a data visualization, following [the instructions below](#data-visualization).
1. [Submit via Gradescope.](https://courseworks2.columbia.edu/courses/207091/assignments/1345872)

## The hard way

- You may not use pandas, [the statistics module](https://docs.python.org/3/library/statistics.html), a spreadsheet program, etc.
  - You should not be reusing the DataFrame/Series you read in in the pandas step.
    - In other words, if you deleted the code for the previous step and restarted the kernel, the code for this step should still work.
- You should be calculating the mean, median, and mode yourself, not using functions with those names (or equivalent).
  - Hint: Use a [dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) to keep track of value counts.

## Data visualization

Requirements:

- The data/calculations can come through pandas, but **the drawing code should only use the Python standard library.**
  - In other words, don't use [`plot()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html), [plotly](https://plotly.com/python/), or any other external packages.
- [General requirements](notebooks.md#visualizations)

We'll talk about data visualization in more detail in [week 10](index.md#schedule), but none of that knowledge is expected to complete this.

### Example

Data that looks like this:

**Rat sightings**

| Year | Count |
| ---- | ----- |
| 2014 | 3,162 |
| 2015 | 4,985 |
| 2016 | 4,091 |

could be turned into a [sparkline](https://en.wikipedia.org/wiki/Sparkline) that looks like this:

```
Rat sightings over time

2014: ***
2015: *****
2016: ****
```

Please don't print 3,162 asterisks (`*`) 😉

### Tips

- Start simple.
  - Start with the example above, get that working, then go from there.
  - Use only one or two columns of your dataset.
  - `print()`ing strings will probably be easiest, but you can get fancy and [generate HTML](https://mkonicek.medium.com/simple-tip-how-to-use-html-in-jupyter-notebook-eef14e81dbc5) if you want.
- Making your chart vertical (one data point per line) will probably be easier than doing something horizontal.
- Techniques that may be helpful:
  - [Repeating strings](https://phoenixnap.com/kb/python-repeat-string)
  - ["Rewinding" a CSV](https://stackoverflow.com/questions/431752/python-csv-reader-how-do-i-return-to-the-top-of-the-file)
- [Python strings can contain Unicode](https://docs.python.org/3/howto/unicode.html#the-string-type), including [emoji](https://getemoji.com/) 📈✨

## Rubric

- 30% [General project requirements](notebooks.md#projects)
- 15% [pandas steps](#steps): 5% x 3
- 30% [Python standard library steps](#steps): 10% x 3
- 25% [Data visualization](#data-visualization)
