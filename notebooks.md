# Notebooks

## General guidance

- This site is built from Jupyter notebooks and Markdown files using [Jupyter Book](https://jupyterbook.org/). You can take a look at [the source code](https://github.com/afeld/computing-in-context), if curious.
- Labs are structured, while [Projects](projects.md) are more open-ended. Both are meant to be challenging, but not impossible.
  - Try and work through problems on your own to start. If you are stuck for more than a half hour, [step away](https://dankim.org/posts/cant-crack-that-programming-problem/). If you _still_ can't figure it out, ask for help.
    - [Ed](https://courseworks2.columbia.edu/courses/230821/external_tools/37606?display=borderless)
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

```{warning}
Images will be broken in downloaded notebooks.
```

## Installing packages

To install Python packages, do the following through VSCode:

1. [Open your working folder.](https://code.visualstudio.com/docs/getstarted/getting-started#_open-a-folder-in-vs-code)
1. [Open a terminal.](https://code.visualstudio.com/docs/terminal/getting-started)
1. [Create a virtual environment](https://docs.python.org/3/library/venv.html#creating-virtual-environments), if you haven't already.

   ```sh
   python -m venv .venv
   ```

1. [Activate the environment](https://docs.python.org/3/library/venv.html#how-venvs-work)
1. Add packages to a [`requirements.txt`](https://pip.pypa.io/en/stable/reference/requirements-file-format/) file.
1. Install the packages.

   ```sh
   pip install -r requirements.txt
   ```

## Submission

You will [submit your Lab/Project notebooks via Gradescope](https://courseworks2.columbia.edu/courses/230821/external_tools/29680?display=borderless).

```{note}
You can ignore Gradescope saying "Large file hidden". The TAs can download the notebook to view.
```

```{warning}
[Gradescope limits submissions to 100MB.](https://guides.gradescope.com/hc/en-us/articles/21861529742477-File-Requirements-for-Assignment-Types#h_01HGKC7CC57Q7MMHMYJ5G6F80E) If you're unable to submit for this (or any other) reason, reach out to the TAs.
```
