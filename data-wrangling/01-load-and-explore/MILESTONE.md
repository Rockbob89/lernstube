# Milestone 1: Load and Explore

## What You're Building

A script that loads the Berlin Airbnb listings dataset, inspects it, and produces a summary of the columns you'll work with going forward. Think of it as the "what have we got?" step before any real analysis.

## What You Need to Know

### NumPy — the foundation under everything

Pandas is built on top of NumPy. Every Pandas column is a NumPy array (or an extension of one). Understanding NumPy means you understand what Pandas is actually doing.

**Core concept: the ndarray.** A NumPy array is a fixed-type, contiguous block of memory. This is why it's fast — no Python object overhead per element.

```python
import numpy as np

# Create from a list
a = np.array([1, 2, 3, 4, 5])

# Shape tells you dimensions
a.shape         # (5,)

# dtype tells you the element type — this matters for memory and precision
a.dtype         # int64

# Vectorized operations — no loops, operates on the whole array
a * 2           # array([ 2,  4,  6,  8, 10])
a[a > 3]        # array([4, 5]) — boolean indexing
```

You won't use NumPy directly much in this milestone, but know that when Pandas acts on a column, it's dispatching to NumPy under the hood.

### Pandas — DataFrames and Series

**DataFrame** = a table. Rows and columns, like a SQL table or a spreadsheet. Each column is a **Series**.

```python
import pandas as pd

# Read a CSV — this is how 90% of Pandas work starts
df = pd.read_csv("listings.csv")

# What did we get?
df.shape              # (rows, cols)
df.dtypes             # type of each column
df.columns.tolist()   # column names as a list
df.head()             # first 5 rows

# Selecting columns
df["name"]            # single column → Series
df[["name", "price"]] # multiple columns → DataFrame

# Quick stats
df.describe()                # summary stats for numeric columns
df.isnull().sum()            # null count per column
df["room_type"].value_counts()  # frequency counts
```

### Reading CSVs with options

Real-world CSVs are messy. `read_csv` has parameters to deal with that:

```python
# Only load specific columns (faster, less memory)
cols = ["id", "name", "neighbourhood_cleansed", "room_type", "price", "number_of_reviews"]
df = pd.read_csv("listings.csv", usecols=cols)

# Preview without loading everything
df = pd.read_csv("listings.csv", nrows=100)  # just first 100 rows
```

## Goal

Write `explore.py` that:

1. Downloads or loads `listings.csv` (the detailed version from Inside Airbnb Berlin).
2. Prints: row count, column count, dtypes.
3. Prints: null counts for each column (only columns that have nulls).
4. Selects a working subset of ~10-15 columns relevant to pricing analysis and prints their names.
5. Prints `value_counts()` for `room_type` and `neighbourhood_cleansed`.

No cleaning yet — just load, look, and decide what to keep.

## File Structure

```
data-wrangling/
├── 01-load-and-explore/
│   ├── MILESTONE.md
│   └── explore.py        ← you write this
```

Put the CSV in this directory or a `data/` subdirectory — your call. Don't commit the CSV.
