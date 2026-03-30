# Task 02: Selection & Filtering

## Objective
Master row/column selection, boolean indexing, and the query API.

## What to Learn
- `.loc[]` (label-based) vs `.iloc[]` (position-based) — `loc` uses index labels; `iloc` uses integer positions (like Python list indexing)
  ```python
  df = pd.DataFrame({"v": [10, 20, 30]}, index=["a", "b", "c"])
  df.loc["b"]      # row with label "b" → v=20
  df.iloc[1]       # row at position 1 → v=20
  df.loc["a":"b"]  # label slice, inclusive on both ends
  df.iloc[0:2]     # position slice, exclusive on right (standard Python)
  ```
- Boolean indexing with single and multiple conditions
- `.query()` method
- `.isin()`, `.between()`
- Chained indexing pitfalls and `SettingWithCopyWarning` — `df[mask]["col"] = val` may silently not modify `df` because the first `[]` may return a copy; use `df.loc[mask, "col"] = val` instead

## Exercises

Implement the functions in `solution.py`.

### 1. `select_high_earners(df, threshold) -> pd.DataFrame`
Given a DataFrame with a `salary` column, return rows where salary > threshold. Use `.loc`.
```python
df = pd.DataFrame({"name": ["A", "B", "C"], "salary": [50000, 120000, 80000]})
select_high_earners(df, 75000)
#   name  salary
# 1    B  120000
# 2    C   80000
```

### 2. `multi_filter(df, filters) -> pd.DataFrame`
Apply multiple column filters. `filters` is a dict of `{column: value}` for exact match, or `{column: (op, value)}` for comparison. Supported ops: `>`, `<`, `>=`, `<=`, `==`, `!=`.
```python
df = pd.DataFrame({"age": [25, 35, 45], "dept": ["Eng", "Sales", "Eng"]})
multi_filter(df, {"dept": "Eng", "age": (">", 30)})
#    age dept
# 2   45  Eng
```

### 3. `safe_slice(df, start_label, end_label) -> pd.DataFrame`
Slice rows by index labels. Return empty DataFrame if labels don't exist (don't raise).
```python
df = pd.DataFrame({"v": [1, 2, 3]}, index=["a", "b", "c"])
safe_slice(df, "a", "b")
#    v
# a  1
# b  2
safe_slice(df, "x", "z")
# Empty DataFrame
```

### 4. `query_builder(df, query_string) -> pd.DataFrame`
Thin wrapper around `.query()`. Return empty DataFrame on invalid query (don't raise).
```python
df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
query_builder(df, "x > 1 and y < 6")
#    x  y
# 1  2  5
```
