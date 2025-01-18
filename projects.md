# Projects

[Due dates](index.md#schedule)

## Requirements

```{warning}
This section was expanded as the class went on. Past Project grades won't be held to the modified requirements.
```

All Projects must:

- **Be done in a Jupyter notebook**
- **Follow the [style guide](https://courseworks2.columbia.edu/courses/203144/files?preview=21151852)**
- **Use at least one dataset you aren't familiar with**
  - Using data from a primary source is preferred.
  - Using a dataset available in CSV or JSON is recommended, though [pandas can read other formats](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html).
  - [Open data portals](https://python-public-policy.afeld.me/en/columbia/assignments.html#open-data-portals)
  - If you'd be interested in working with [SIPA alumni employment data](https://www.sipa.columbia.edu/pathways-careers/employment-statistics), [reach out to the instructor](index.md#instructors).
- **Link to the source dataset(s)**
- **Read like a blog post**
  - Pretend you're explaining to a peer who hasn't taken this class. You don't need to teach them to code, but they should be able to follow what's going on.
  - Walk the reader through what you're doing in every step and what they should be taking away from it.
    - You are more than welcome to inject personality in there; doesn't need to be dry.
  - Use text cells with [Markdown](https://www.markdownguide.org/basic-syntax/) for formatting.
    - You'll need to [change the cell type to Markdown](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html).
  - If you hit any dead ends in your analysis, leave them in.
    - For example, include charts that you generate that may not show anything interesting and explain what you are choosing to look at instead.
    - You should still be cleaning up unused/broken code to make your notebook readable.
    - You may need to tweak your research question as you go. Show and explain why.
- **Values must not be [hard-coded](https://en.wikipedia.org/wiki/Hard_coding)**
  - In other words, if the dataset got additional rows, had values changed, etc., the rest of the notebook should work as expected.
- **Don't leave any sensitive information in the notebook**, such as:
  - API keys
  - Personally-identifiable information (PII)

### Visualizations

All visualizations must:

- **Have a title** that's clear
- **Have axis labels** that are clear
  - Include units, if applicable
  - Not required for Project 1.
- **Look decent on a narrow (11") laptop screen**

## Tips

- [The Final Project resources from Python for Public Policy](https://python-public-policy.afeld.me/en/columbia/final_project/resources.html) may be helpful.
- The dataset/analysis can be serious or silly.
- You can be creative, but **start simple**.
- Go back and find any information that's available _around_ the data, to get a better understanding of what it contains and means.
  - Might include a data dictionary
  - Might involve poking around a government agency's web site to understand their processes
  - Understand what all the different columns and values represent
- For these Projects, the important thing is getting practice with the mechanics of working with data in code.
  - You won’t be graded on the scientific soundness of your work.
    - That said, please think through and note assumptions/caveats/unknowns of your approach.
- **DO NOT WAIT UNTIL THE LAST MINUTE TO SUBMIT.** Leave yourself time to fix any issues that come up in doing so, computer crashing, etc.

### Visualizations

- [Consider which visualization type is most appropriate.](lecture_20.ipynb#what-visualization-should-i-use)
- If you’re trying to show more than three variables at once (e.g. X axis, Y axis, and color), try simplifying.
- [Other best practices.](https://xdgov.github.io/data-design-standards/)
