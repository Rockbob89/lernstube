# Task 03: Data Cleaning

## Objective
Handle messy real-world data: missing values, duplicates, type issues, and string manipulation.

## What to Learn
- `isna()`, `fillna()`, `dropna()`, `interpolate()`
- `duplicated()`, `drop_duplicates()`
- `astype()`, `pd.to_numeric()`, `pd.to_datetime()`
- `.str` accessor methods — exposes Python string methods on a whole Series without a loop
  ```python
  s = pd.Series(["  Hello ", "WORLD"])
  s.str.strip().str.lower()   # Series(["hello", "world"])
  s.str.contains("ello")      # boolean mask
  s.str.replace(r"[aeiou]", "*", regex=True)
  ```
- `replace()`, `map()`, `apply()` — `map` applies a function or dict element-wise to a Series; `apply` applies a function along an axis of a DataFrame; `replace` swaps values without a function
  ```python
  s = pd.Series([1, 2, 3])
  s.map({1: "one", 2: "two"})         # Series(["one", "two", NaN])
  df.apply(lambda col: col.max(), axis=0)  # max of each column
  ```

## Exercises

Implement the functions in `solution.py`.

### 1. `clean_numeric_column(series) -> pd.Series`
Convert a messy string column to float. Handle: dollar signs, commas, whitespace, "N/A"/"NA"/"-" as NaN.
```python
s = pd.Series(["$1,234.56", " 789 ", "N/A", "$-42.10", "-"])
clean_numeric_column(s)
# 0    1234.56
# 1     789.00
# 2       NaN
# 3     -42.10
# 4       NaN
# dtype: float64
```

### 2. `deduplicate(df, subset, keep) -> pd.DataFrame`
Drop duplicates on `subset` columns, keeping `keep` ('first', 'last', or False). Reset index.
```python
df = pd.DataFrame({"a": [1, 1, 2], "b": [10, 20, 30]})
deduplicate(df, subset=["a"], keep="last")
#    a   b
# 0  1  20
# 1  2  30
```

### 3. `fill_strategy(df, strategies) -> pd.DataFrame`
Fill NaN values per column using different strategies. `strategies` is `{col: strategy}` where strategy is one of: `"mean"`, `"median"`, `"mode"`, `"ffill"`, `"zero"`, or a literal value.
```python
df = pd.DataFrame({"a": [1, None, 3], "b": [None, 5, None]})
fill_strategy(df, {"a": "mean", "b": "zero"})
#      a    b
# 0  1.0  0.0
# 1  2.0  5.0
# 2  3.0  0.0
```

### 4. `standardize_strings(series, operations) -> pd.Series`
Apply a list of string operations in order. Supported: `"lower"`, `"upper"`, `"strip"`, `"title"`, `"remove_punctuation"`.
```python
s = pd.Series(["  Hello, World!  ", "FOO-BAR  "])
standardize_strings(s, ["strip", "lower", "remove_punctuation"])
# 0    hello world
# 1        foobar
# dtype: object
```
