# Test

The test will contain fill-in-the-blank and free response questions, coding and high-level. It will be done on paper, closed-book (no cheat sheets, phones, laptops, etc).

## Topics

The test will cover some or all of the following:

- Working with data using only the Python standard library ("pure Python")
- Python/pandas data types/structures
- Jupyter concepts
- Data manipulation
  - Boolean indexing
  - Grouping
  - Cleaning
  - Merging
- Data visualization
- Time series
  - Resampling
- APIs, conceptually
- Best practices

## Example questions

- How would you read from a CSV using only the Python standard library (not pandas)? Pseudocode is fine.
- List all the types that a pandas column can be. Come up with at least three.
- What are some scenarios where you'd need to convert between Python/pandas types? Come up with at least three.
- How do you make a link in Markdown?
- How does `groupby()` work?
- What is resampling used for? Include an example.
- What's a kernel, in the context of this course?
- Write the equivalent of the following in pandas.

  ```python
  import csv

  lowest_gdp = None
  lowest_country = None

  with open("gdp.csv") as f:
     reader = csv.DictReader(f)
     for row in reader:
        gdp = float(row["GDP"])
        if lowest_gdp is None or gdp < lowest_gdp:
              lowest_gdp = gdp
              lowest_country = row["Country"]

  print(lowest_country)
  ```

- What's wrong with the following code?
- What are the different kinds of merges? Can describe through text and/or visuals.
- You have the following Dataframes. Write the code to merge them.

**`intros`**

| Name         | Year introduced |
| ------------ | --------------- |
| Mickey Mouse | 1928            |
| Big Bird     | 1969            |
| Lisa Simpson | 1987            |

**`shows`**

| First  | Last    | Series        |
| ------ | ------- | ------------- |
| Lisa   | Simpson | The Simpsons  |
| Mickey | Mouse   | multiple      |
| Big    | Bird    | Sesame Street |
