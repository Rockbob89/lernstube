# Task 05: Merging & Joining

## Objective
Combine DataFrames using merge, join, and concat with proper key handling.

## What to Learn
- `pd.merge()`: inner, left, right, outer joins
- `on`, `left_on`, `right_on`, suffixes
- `pd.concat()` along axis 0 and 1
- `.join()` (index-based) — merges on index rather than columns; shorthand for `merge(..., left_index=True, right_index=True)`
- Indicator column (`_merge`) for debugging joins — adds a column showing `"both"`, `"left_only"`, or `"right_only"` for each row
  ```python
  pd.merge(left, right, on="id", how="outer", indicator=True)
  # _merge column tells you which side each row came from
  ```
- Many-to-many join behavior — if both sides have duplicate keys, the result is the cartesian product of matching rows; row count can explode unexpectedly

## Exercises

Implement the functions in `solution.py`.

### 1. `safe_merge(left, right, on, how) -> pd.DataFrame`
Merge two DataFrames with a `_merge` indicator column showing where each row came from (`both`, `left_only`, `right_only`). Always perform an outer merge internally with `indicator=True`, then filter based on `how`: `"inner"` keeps only `both`, `"left"` keeps `both` + `left_only`, `"right"` keeps `both` + `right_only`, `"outer"` keeps all.
```python
left = pd.DataFrame({"id": [1, 2, 3], "val": ["a", "b", "c"]})
right = pd.DataFrame({"id": [2, 3, 4], "score": [90, 80, 70]})
safe_merge(left, right, on="id", how="left")
#    id val  score     _merge
# 0   1   a    NaN  left_only
# 1   2   b   90.0       both
# 2   3   c   80.0       both
```

### 2. `multi_table_join(dfs, on) -> pd.DataFrame`
Left-join a list of DataFrames sequentially on the same key column.
```python
df1 = pd.DataFrame({"id": [1, 2], "a": [10, 20]})
df2 = pd.DataFrame({"id": [1, 2], "b": [30, 40]})
df3 = pd.DataFrame({"id": [1], "c": [50]})
multi_table_join([df1, df2, df3], on="id")
#    id   a   b     c
# 0   1  10  30  50.0
# 1   2  20  40   NaN
```

### 3. `concat_with_source(dfs, names) -> pd.DataFrame`
Concatenate DataFrames vertically, adding a `source` column from `names`. Reset index.
```python
df1 = pd.DataFrame({"x": [1, 2]})
df2 = pd.DataFrame({"x": [3, 4]})
concat_with_source([df1, df2], ["file_a", "file_b"])
#    x  source
# 0  1  file_a
# 1  2  file_a
# 2  3  file_b
# 3  4  file_b
```

### 4. `find_unmatched(left, right, on) -> tuple[pd.DataFrame, pd.DataFrame]`
Return (left_only, right_only) rows that don't match on the key.
```python
left = pd.DataFrame({"id": [1, 2, 3], "val": ["a", "b", "c"]})
right = pd.DataFrame({"id": [2, 4], "score": [90, 70]})
left_only, right_only = find_unmatched(left, right, on="id")
# left_only:  id=1,3  right_only: id=4
```
