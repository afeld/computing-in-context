# Project 3

**IN PROGRESS**

## Objectives

This project has two parts:

- [Publishing your Projects as a website](#project-site)
- [Proving or disproving a hypothesis using skills learned in this class](#data-analysis)

They can be done in either order, or in parallel.

## Project site

You don't know how to do this yet. You will need to read the documentation to figure it out.

1. Make a homepage in your JupyterBook.
   - Suggest making it a Markdown file, `index.md`
   - `project_3` will no longer be the `root`
   - Relevant documentation:
     - [Create your own content file](https://jupyterbook.org/en/stable/start/new-file.html)
     - [Configure the Table of Contents](https://jupyterbook.org/en/stable/structure/configure.html)
1. [Publish to Read the Docs](https://jupyterbook.org/en/stable/publish/readthedocs.html)

Please do not include your Lab notebooks in your site, per the [Academic Integrity Policy](index.md#academic-integrity).

## Data analysis

We're looking for you to be _just the right amount_ of ambitious.

### Once you start

- [General Project information](notebooks.md#projects)
- If you end up answering your initial research question easily (haven't met the requirements below), ask and answer follow-up question(s).

### Analysis requirements

Your submission should:

- **Meet the [general Project requirements](notebooks.md#projects)**
- **Not be trivial** - requiring:
  - At least 40 lines of code to come to a conclusion
    - That code should be relevant to answering your question. In other words, having 40 lines of `print("hello world")` wouldn't count.
    - If you meet all the other requirements, you will likely be well over this number.
    - You can count them automatically using a tool like [tokei](https://github.com/XAMPPRocky/tokei).
  - Transforming data through [grouping](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html), [merging](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#merge), and/or [reshaping](https://pandas.pydata.org/docs/user_guide/reshaping.html) of DataFrames
  - Operations that aren't easily done in a spreadsheet.
- **Have a visualization** (chart or map) of some kind
  - [General requirements](notebooks.md#visualizations)

If you answer the first question easily, that's fine; dig into / build off of it. Go deep, not broad.

### Submission

**DO NOT WAIT UNTIL THE LAST MINUTE TO SUBMIT.** Leave yourself time to fix any issues that come up in doing so, computer crashing, etc.

Instead of submitting via Gradescope, you will be publishing your notebooks for Project 1, 2, and 3 to the web. The suggested method is [Jupyter Book via Read the Docs](week_13.md). (If you want to publish a different way, please ask on Ed first and wait for the instructor/TAs to confirm.)

### Process

1. [Find a dataset](notebooks.md#projects) that seems interesting.
   - To meet the [requirement](#analysis-requirements) that your project "not be trivial," you probably want a dataset that's large enough that you can't understand it at a glance. In other words, you probably want it to have 500+ rows.
   - Finding a dataset available in CSV or JSON is recommended, though [pandas can read other formats](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html).
1. Load the data into a DataFrame.
1. Inspect the data a bit.
1. Come up with a question that the data is capable of answering and _isn't trivial to answer_.
   - If you aren't sure, ask.
1. Come up with a hypothesis (a.k.a. a guess of the answer to the question).

### Format

- **What dataset(s) are you going to use?**
  - Please include link(s).
- **What's the question you are trying to answer?**
  - It should be _specific, and objectively answerable_ through the data available.
- **What columns of the DataFrame(s) are you going to use to answer that?**
- If you're using multiple datasets: **What columns are you going to merge/join them on?**
- **What's your hypothesis?**

Feel free to include any questions/concerns/uncertainties that the TAs can help with.

### Tips

- Don't overthink it; [the process above](#process) shouldn't take more than a few hours.
- Your question/hypothesis doesn't need to be something novel; confirming something you read / heard about is fine.
- You won't be graded on the scientific soundness of your work.
  - That said, please think through and note assumptions/caveats/unknowns of your approach.
- The point of the proposal is to ensure you've dug into the data and that your project scope is reasonable. Think of it as a head start rather than something you're locked into.

#### Question your question

Even the question can bake in assumptions. For example:

> What ZIP code has the highest number of food poisoning cases?

assumes a relationship between food-borne illness and geography. What assumptions does your question make?
