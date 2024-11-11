# Notebook info

This site is built from Jupyter notebooks and Markdown files using [Jupyter Book](https://jupyterbook.org/). You can take a look at [the source code](https://github.com/afeld/computing-in-context), if curious.

## Downloading notebooks

For lecture slides / labs, download the page as a notebook to work with it locally.

1. Open the page for the Homework/Lecture on this site.
   - For example: [Lab 8](lab_8.ipynb)
1. Hover over the download icon (⬇️) in the toolbar at the top.
   - Feel free to move it to whatever folder you like.
1. You may then see the [notebook JSON](https://nbformat.readthedocs.io/en/latest/format_description.html) - go to:
   1. `File` menu
   1. `Save Page As...`
1. [Open the notebook in JupyterLab.](https://jupyterlab.readthedocs.io/en/latest/user/files.html#opening-files)

That is now your own copy; you can execute/add cells as you like, including adding your own notes in [Markdown cells](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html). For Labs, the intention is for you to turn in the template via Gradescope, filled in with your code.

Known issue: images will be broken.

## Projects

### Requirements

All Projects must:

- **Be done in a Jupyter notebook**
- **Follow the [style guide](https://courseworks2.columbia.edu/courses/203144/files?preview=21151852)**
- **Use at least one dataset you aren't familiar with**
  - Using data from a primary source is preferred.
  - [Open data portals](https://python-public-policy.afeld.me/en/columbia/final_project/resources.html#open-data-portals)
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
- **Values should not be [hard-coded](https://en.wikipedia.org/wiki/Hard_coding)**
  - In other words, if the dataset got additional rows, had values changed, etc., the rest of the notebook should work as expected.
- **Don't leave any sensitive information in the notebook**, such as:
  - API keys
  - Personally-identifiable information (PII)

### Tips

- The dataset/analysis can be serious or silly.
- You can be creative, but **start simple**.
- Go back and find any information that's available _around_ the data, to get a better understanding of what it contains and means.
  - Might include a data dictionary
  - Might involve poking around a government agency's web site to understand their processes
  - Understand what all the different columns and values represent
- For these Projects, the important thing is getting practice with the mechanics of working with data in code.
  - You won’t be graded on the scientific soundness of your work.
