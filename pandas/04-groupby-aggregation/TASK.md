# Task 04: GroupBy & Aggregation

## Objective
Use groupby, aggregation functions, and pivot tables for data summarization.

## What to Learn
- `.groupby()` single and multiple keys
- `.agg()` with named aggregations
- `.transform()` vs `.apply()` vs `.agg()` — key distinction: `agg` reduces the group to a scalar; `transform` returns a same-size result aligned to the original index; `apply` is the escape hatch for arbitrary operations
  ```python
  df = pd.DataFrame({"dept": ["A","A","B"], "salary": [100,200,150]})
  df.groupby("dept")["salary"].agg("mean")      # dept → scalar (A:150, B:150)
  df.groupby("dept")["salary"].transform("mean") # original index, group mean broadcast back
  # transform is useful for things like: df["salary_vs_dept_mean"] = df["salary"] - transform_result
  ```
- `pd.pivot_table()`, `pd.crosstab()`
- GroupBy object internals: groups, iteration, filtering

## Exercises

Implement the functions in `solution.py`.

### 1. `sales_summary(df) -> pd.DataFrame`
Given a DataFrame with `region`, `product`, `revenue`, `quantity`, group by `region` and compute: total revenue, mean quantity, number of transactions. Name columns: `total_revenue`, `avg_quantity`, `n_transactions`.
```python
df = pd.DataFrame({
    "region": ["East", "East", "West"],
    "product": ["A", "B", "A"],
    "revenue": [100, 200, 150],
    "quantity": [10, 20, 15]
})
sales_summary(df)
#        total_revenue  avg_quantity  n_transactions
# region
# East             300          15.0               2
# West             150          15.0               1
```

### 2. `group_rank(df, group_col, value_col) -> pd.Series`
Add a rank within each group (1 = highest value). Use transform.
```python
df = pd.DataFrame({"dept": ["A", "A", "B", "B"], "score": [90, 80, 70, 95]})
group_rank(df, "dept", "score")
# 0    1.0
# 1    2.0
# 2    2.0
# 3    1.0
# dtype: float64
```

### 3. `pivot_summary(df, index, columns, values, aggfunc) -> pd.DataFrame`
Create a pivot table. Fill NaN with 0.
```python
df = pd.DataFrame({
    "month": ["Jan", "Jan", "Feb"],
    "product": ["A", "B", "A"],
    "sales": [10, 20, 15]
})
pivot_summary(df, "month", "product", "sales", "sum")
# product     A     B
# month
# Feb      15.0   0.0
# Jan      10.0  20.0
```

### 4. `filter_groups(df, group_col, min_size) -> pd.DataFrame`
Keep only groups that have at least `min_size` rows.
```python
df = pd.DataFrame({"cat": ["a", "a", "b", "a", "b", "c"], "val": range(6)})
filter_groups(df, "cat", 2)
#   cat  val
# 0   a    0
# 1   a    1
# 2   b    2
# 3   a    3
# 4   b    4
```
