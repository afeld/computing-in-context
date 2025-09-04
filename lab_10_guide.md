# Lab 10 guide

**Goal:** Get students to think ahead to the visualizations they want to produce, then work through the steps to get there.

## First half

Do the following as a group, with students directing.

1. Pick [a `Dataset` from the NYC Open Data Portal](https://data.cityofnewyork.us/browse?sortBy=most_accessed&limitTo=datasets).
1. Look at the columns/data through the Portal (don't download).
1. Decide how you want to visualize.
   - What columns should be used?
   - What chart type should be used?
   - Keep it simple.
     - Avoid anything that would require complex transformations.
     - For the purposes of this lab, it's ok to cut corners.
   - Avoid using date/time columns - we'll cover those in [Week 11](index.md#topics). Years are fine.
1. Get the CSV URL.
1. Create a new notebook.
1. Read in the data.
1. Do any necessary data cleaning.
1. Create the visualization.

If you have time, repeat with a different visualization type, using a different dataset if you need. It's ok if it's a bit bumpy; use any dead ends as teachable moments.

### Examples

- Using [crash data](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95/explore), make a histogram of contributing factors.
- Using [city payroll data](https://data.cityofnewyork.us/City-Government/Citywide-Payroll-Data-Fiscal-Year-/k397-673e/explore), make a scatterplot of base salary vs. total other pay.
  - You'll need to deal with formatting / data types.

## Second half

Walk through [Lab 10 Exercise](lab_10.ipynb).
