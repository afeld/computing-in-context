# Notebook info

## General guidance

- This site is built from Jupyter notebooks and Markdown files using [Jupyter Book](https://jupyterbook.org/). You can take a look at [the source code](https://github.com/afeld/computing-in-context), if curious.
- Labs are structured, while Projects are more open-ended. Both are meant to be challenging, but not impossible.
  - Try and work through problems on your own to start. If you are stuck for more than a half hour, [step away](https://dankim.org/posts/cant-crack-that-programming-problem/). If you _still_ can't figure it out, ask for help.
    - [Ed](https://courseworks2.columbia.edu/courses/207091/external_tools/37606?display=borderless)
    - [Office hours](office_hours.md)

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

## Known issues

- Images will be broken in downloaded notebooks
- [Gradescope limits submissions to 100MB.](https://guides.gradescope.com/hc/en-us/articles/21861529742477-File-Requirements-for-Assignment-Types#h_01HGKC7CC57Q7MMHMYJ5G6F80E) If you're unable to submit for this (or any other) reason, reach out to the TAs.

## Installing packages

1. [Open Anaconda Navigator.](https://docs.anaconda.com/navigator/getting-started/#starting-navigator)
1. Navigate to [Environments](https://docs.anaconda.com/navigator/tutorials/manage-environments/).
1. [Add the `conda-forge` channel](https://docs.anaconda.com/navigator/tutorials/manage-channels/#adding-a-channel-in-navigator), if you haven't already.
1. [Update the index.](https://docs.anaconda.com/navigator/tutorials/manage-packages/)
1. [Find and install the relevant package(s).](https://docs.anaconda.com/navigator/tutorials/manage-packages/#installing-a-package)
   - The interface is a bit confusing, so read these instructions carefully.

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
- **Values must not be [hard-coded](https://en.wikipedia.org/wiki/Hard_coding)**
  - In other words, if the dataset got additional rows, had values changed, etc., the rest of the notebook should work as expected.
- **Don't leave any sensitive information in the notebook**, such as:
  - API keys
  - Personally-identifiable information (PII)

#### Visualizations

All visualizations must:

- **Have a title** that's clear
- **Have axis labels** that are clear
  - Include units, if applicable
  - Not required for Project 1.
- **Look decent on a narrow (11") laptop screen**

[Best practices.](https://xdgov.github.io/data-design-standards/)

### Tips

- [The Final Project resources from Python for Public Policy](https://python-public-policy.afeld.me/en/columbia/final_project/resources.html) may be helpful, as that Project is similar.
- The dataset/analysis can be serious or silly.
- You can be creative, but **start simple**.
- Go back and find any information that's available _around_ the data, to get a better understanding of what it contains and means.
  - Might include a data dictionary
  - Might involve poking around a government agency's web site to understand their processes
  - Understand what all the different columns and values represent
- For these Projects, the important thing is getting practice with the mechanics of working with data in code.
  - You won’t be graded on the scientific soundness of your work.

### Grading

The Rubrics in Gradescope have [Items](https://guides.gradescope.com/hc/en-us/articles/22249389005709-Grading-Submissions#h_01HHDFGS9DRQ52GVJAG04KPBVV) that correspond to the different sections/requirements. Each will be broken down to:

- Full credit
- Partial credit (half points)
- Incomplete (zero points)

There will no points assigned between those values. In other words, if a specific section that is attempted but didn't meet all the requirements, it will get half the points for that Rubric Item, no matter how far off it was.
