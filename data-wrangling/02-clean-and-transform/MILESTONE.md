# Milestone 2: Clean and Transform

## File Structure

```
data-wrangling/
├── 01-load-and-explore/
│   └── ...
├── 02-clean-and-transform/
│   ├── MILESTONE.md
│   └── clean.py          ← you write this
```

Use the same `listings.csv.gz` from milestone 1 (symlink it, copy it, or just reference the path).

## What You're Building

A script that takes the raw dataset, selects your working columns, and produces a clean DataFrame ready for analysis. By the end, every column has the right type, nulls are handled deliberately, and prices are actual numbers.

## What You Need to Know

### Selecting columns

You picked your subset in milestone 1. Now load only those:

```python
cols = ["neighbourhood_cleansed", "room_type", "price", "bedrooms", "number_of_reviews"]
df = pd.read_csv("listings.csv.gz", usecols=cols)
```

### Fixing dtypes — the `price` problem

Look at the `price` column. It looks like numbers, but it's stored as strings because of the `$` and `,`:

```python
df["price"].head()
# 0    $75.00
# 1    $150.00
# 2    $44.00
```

To make it numeric, strip the junk and convert:

```python
df["price"] = df["price"].str.replace("$", "", regex=False).str.replace(",", "", regex=False).astype(float)
```

**What's happening:** `.str` gives you string methods on a whole Series. `replace` strips characters. `astype(float)` converts. This is a chain — each step returns a new Series.

### Handling nulls

Three strategies, pick per column:

```python
# Drop rows where a column is null
df = df.dropna(subset=["price"])

# Fill with a value
df["bedrooms"] = df["bedrooms"].fillna(0)

# Fill with a computed value
df["review_scores_rating"] = df["review_scores_rating"].fillna(df["review_scores_rating"].median())
```

**Which to use when:**
- **Drop** if the row is useless without that value (no price = can't analyze pricing).
- **Fill with 0** if absence means zero (no bedrooms listed likely means studio/0).
- **Fill with median/mean** if you want to keep the row but need a reasonable stand-in. Median is safer than mean — outliers don't skew it.

There's no universally right answer. The point is to make a deliberate choice per column and know why.

### NumPy under the hood — vectorized operations

When you do `df["price"].str.replace(...)`, Pandas is looping internally. But when you do math on numeric columns, it dispatches to NumPy:

```python
import numpy as np

# These are NumPy-speed operations, not Python loops
df["price_per_review"] = df["price"] / df["number_of_reviews"]

# NumPy functions work on Pandas Series directly
np.log1p(df["price"])     # log(1 + x), useful for skewed distributions
df["price"].values         # the raw NumPy array underneath
```

You don't need to engineer features yet — but know that any arithmetic you do on columns is already vectorized.

### Boolean percentage columns

Some columns like `host_is_superhost` or `host_response_rate` might be stored as strings (`"t"/"f"` or `"95%"`). Convert them:

```python
# t/f to boolean
df["host_is_superhost"] = df["host_is_superhost"].map({"t": True, "f": False})

# percentage string to float
df["host_response_rate"] = df["host_response_rate"].str.rstrip("%").astype(float) / 100
```

## Goal

Write `clean.py` that:

1. Loads `listings.csv.gz` with only your selected columns.
2. Prints the dtypes and a sample before cleaning (so you can see the mess).
3. Converts `price` to a numeric float.
4. Handles nulls in every column — drop, fill, or justify ignoring. Print your null counts after.
5. Fixes any other dtype issues you spot (strings that should be numbers, etc.).
6. Prints a final `df.info()` and `df.describe()` showing a clean, typed DataFrame.

Document your decisions as comments — "dropped nulls because X", "filled with median because Y".
