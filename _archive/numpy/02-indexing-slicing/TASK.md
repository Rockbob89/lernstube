# Task 02: Indexing & Slicing

## Objective
Master NumPy's indexing strategies: basic, fancy, boolean, and understand views vs copies.

## What to Learn
- Basic slicing (start:stop:step) on N-d arrays
- Fancy indexing with integer arrays — selecting with an array of indices; always returns a copy, not a view
  ```python
  a = np.array([10, 20, 30, 40])
  idx = np.array([3, 1, 0])
  a[idx]  # array([40, 20, 10]) — picks elements at those positions
  ```
- Boolean masks / conditional selection
- `np.where`, `np.argwhere`
- Views vs copies: when mutations propagate — basic slicing gives a view (shared memory); fancy/boolean indexing gives a copy
  ```python
  a = np.arange(5)
  v = a[1:4]    # view — modifying v modifies a
  c = a[[1, 2]] # copy — modifying c does not affect a
  v[0] = 99     # a becomes [0, 99, 2, 3, 4]
  ```

## Exercises

Implement the functions in `solution.py`.

### 1. `extract_diagonal_blocks(mat, block_size) -> list[np.ndarray]`
Given a square matrix, extract square blocks along the diagonal.
```python
m = np.arange(16).reshape(4, 4)
extract_diagonal_blocks(m, 2)
# [array([[0, 1], [4, 5]]), array([[10, 11], [14, 15]])]
```

### 2. `mask_outliers(arr, n_std) -> np.ndarray`
Replace values more than `n_std` standard deviations from the mean with `np.nan`. Input is float64. Return a copy, don't mutate.
```python
a = np.array([1.0, 2.0, 3.0, 100.0, 2.5])
mask_outliers(a, 1.5)
# array([1. , 2. , 3. , nan, 2.5])
```

### 3. `fancy_select(arr, row_indices, col_indices) -> np.ndarray`
Use fancy indexing to select elements at the given (row, col) pairs.
```python
m = np.arange(12).reshape(3, 4)
fancy_select(m, [0, 1, 2], [3, 2, 1])
# array([3, 6, 9])
```

### 4. `is_view(a, b) -> bool`
Determine whether array `b` is a view of array `a` (shares memory).
```python
a = np.arange(10)
is_view(a, a[::2])   # True
is_view(a, a[[1,3]])  # False
```
