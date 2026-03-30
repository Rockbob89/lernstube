# Task 05: Aggregation & Statistics

## Objective
Use NumPy's aggregation functions along axes for statistical analysis.

## What to Learn
- `sum`, `mean`, `std`, `var`, `min`, `max` with `axis` parameter — `axis=0` collapses rows (result is one value per column); `axis=1` collapses columns (one value per row)
  ```python
  m = np.array([[1, 2], [3, 4]])
  m.sum(axis=0)  # array([4, 6]) — sum down each column
  m.sum(axis=1)  # array([3, 7]) — sum across each row
  ```
- `argmin`, `argmax`, `argsort`
- `cumsum`, `cumprod` — running total/product along an axis; output shape same as input
  ```python
  np.cumsum([1, 2, 3, 4])  # array([ 1,  3,  6, 10])
  ```
- `np.percentile`, `np.quantile`, `np.histogram`
- `np.nan*` variants (`nanmean`, `nanstd`, etc.) — same as their counterparts but skip NaN values instead of propagating them

## Exercises

Implement the functions in `solution.py`.

### 1. `column_zscore(mat) -> np.ndarray`
Z-score normalize each column of a 2D array. (value - mean) / std per column.
```python
m = np.array([[1, 2], [3, 4], [5, 6]], dtype=float)
column_zscore(m)
# array([[-1.22474487, -1.22474487],
#        [ 0.        ,  0.        ],
#        [ 1.22474487,  1.22474487]])
```

### 2. `rolling_mean(arr, window) -> np.ndarray`
Compute rolling mean with given window size. Output length = len(arr) - window + 1. No pandas.
```python
rolling_mean(np.array([1, 2, 3, 4, 5], dtype=float), 3)
# array([2., 3., 4.])
```

### 3. `top_k_per_row(mat, k) -> np.ndarray`
Return the top k values per row, sorted descending. Output shape (N, k).
```python
m = np.array([[3, 1, 4, 1, 5], [9, 2, 6, 5, 3]])
top_k_per_row(m, 3)
# array([[5, 4, 3],
#        [9, 6, 5]])
```

### 4. `nan_aware_summary(arr) -> dict`
Given a 1D array with possible NaNs, return dict with: `mean`, `std`, `median`, `pct_missing`, `p25`, `p75`.
```python
a = np.array([1.0, np.nan, 3.0, 4.0, np.nan, 6.0])
nan_aware_summary(a)
# {'mean': 3.5, 'std': 1.802..., 'median': 3.5, 'pct_missing': 33.33..., 'p25': 2.5, 'p75': 4.5}
```
