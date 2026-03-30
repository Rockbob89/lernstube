# Task 01: Series & DataFrames

## Objective
Create, inspect, and manipulate the core Pandas data structures.

## What to Learn
- `pd.Series` and `pd.DataFrame` constructors (from dicts, lists, NumPy arrays)
- `.dtypes`, `.shape`, `.info()`, `.describe()`
- Index: setting, resetting, custom indices — the Index is a labeled axis used for alignment and lookup; every DataFrame has one
  ```python
  df = pd.DataFrame({"a": [1, 2]}, index=["x", "y"])
  df.loc["x"]           # select by label
  df.reset_index()      # move index back to a column
  df.set_index("a")     # promote column to index
  ```
- Column operations: add, rename, drop, reorder
- `.values`, `.to_numpy()`, `.index`, `.columns` — `.values` returns the underlying NumPy array (or object array for mixed types); `.to_numpy()` is preferred as it's explicit about dtype

## Exercises

Implement the functions in `solution.py`.

### 1. `create_employee_df(names, salaries, departments) -> pd.DataFrame`
Create a DataFrame with columns `name`, `salary`, `department`. Index should be `emp_001`, `emp_002`, etc.
```python
create_employee_df(["Alice", "Bob"], [90000, 85000], ["Eng", "Sales"])
#          name  salary department
# emp_001  Alice   90000        Eng
# emp_002    Bob   85000      Sales
```

### 2. `df_summary(df) -> dict`
Return dict with: `n_rows`, `n_cols`, `dtypes` (dict of col->dtype string), `memory_bytes` (deep memory usage).
```python
df_summary(pd.DataFrame({"a": [1, 2], "b": ["x", "y"]}))
# {'n_rows': 2, 'n_cols': 2, 'dtypes': {'a': 'int64', 'b': 'object'}, 'memory_bytes': ...}
```

### 3. `reindex_by_column(df, col) -> pd.DataFrame`
Set the given column as the index and drop it from columns. Raise ValueError if column doesn't exist.
```python
df = pd.DataFrame({"id": [10, 20], "val": [1, 2]})
reindex_by_column(df, "id")
#     val
# id
# 10    1
# 20    2
```

### 4. `safe_add_column(df, col_name, values) -> pd.DataFrame`
Add a column. If it already exists, raise ValueError. Return a copy, don't mutate input.
```python
df = pd.DataFrame({"a": [1, 2]})
safe_add_column(df, "b", [3, 4])
#    a  b
# 0  1  3
# 1  2  4
```
