# Project 3

[General Project information](projects.md)

## Objective

Prove or disprove a hypothesis using skills learned in this class.

## Intro

You can think of this as similar to the [Project 2](project_2.md) requirements, but expanded. [Examples of Final Projects for Python for Public Policy](https://python-public-policy.afeld.me/en/columbia/final_project/examples.html) - the result of this Project will be similar.

## Process

1. [Find a dataset](projects.md#requirements) that seems interesting.
   - To meet the [requirement](#analysis-requirements) that your project "not be trivial," you probably want a dataset that's large enough that you can't understand it at a glance.
     - If you're only using one dataset, you probably want it to have 500+ rows.
1. Load the data into a DataFrame.
1. Inspect the data a bit.
1. Fill out the prompt (below).
   - Work backwards: On a piece of paper / whiteboard, draw the visualization you imagine producing.
1. Use the data to answer the question.
1. If you end up answering your initial research question easily (haven't met [the requirements](#analysis-requirements)), that's fine. Ask and answer follow-up question(s).
   - Go deep, not broad.

## Prompt

Put the following in a Markdown cell in your notebook and fill it out:

<!-- https://myst-parser.readthedocs.io/en/latest/syntax/organising_content.html#inserting-other-documents-directly-into-the-current-document -->

```{include} ../src/project_3_prompt.md

```

:::{admonition} Raw Markdown
:class: dropdown

```{literalinclude} ../src/project_3_prompt.md
:language: md
```

:::

The question should be:

- Specific
- Objectively answerable through the data available
- _Just the right amount_ of ambitious ([non-trivial](#analysis-requirements))

If you want help/feedback, don't hesitate to ask on [Ed](https://courseworks2.columbia.edu/courses/230821/external_tools/37606?display=borderless) or come to [office hours](office_hours.md).

### Tips

- Don't overthink it; getting up through filling out the prompt shouldn't take more than a few hours.
- Your question/hypothesis doesn't need to be something novel; confirming something you read / heard about is fine.
- The point of the prompt is to ensure you've dug into the data and that your project scope is reasonable. Think of it as a guide rather than something you're locked into.
- Even the question can bake in assumptions.
  - Example: "What ZIP code has the highest number of food poisoning cases?" assumes a relationship between food-borne illness and geography.
  - What assumptions does your question make?

## Analysis requirements

Your submission must:

- **Meet the [general Project information](projects.md#requirements)**
- **Not be trivial** (or -30 points) - requiring:
  - At least 40 lines of code to come to a conclusion
    - That code should be relevant to answering your question. In other words, having 40 lines of `print("hello world")` wouldn't count.
    - If you meet all the other requirements, you will likely be well over this number.
    - You can count them automatically using a tool like [tokei](https://github.com/XAMPPRocky/tokei).
  - Operations that aren't easily done in a spreadsheet.
- **Transform data through [grouping](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html), [merging](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#merge), and/or [reshaping](https://pandas.pydata.org/docs/user_guide/reshaping.html)** of DataFrames (or -15 points)
- **Have a visualization** (chart or map) of some kind (or -5 points)
  - [General requirements](projects.md#visualizations)
- **Have the [prompt](#prompt) filled out**

---

[Submit.](notebooks.md#submission)
