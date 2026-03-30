# Task 03: Vectorized Operations

## Objective
Replace Python loops with vectorized NumPy operations. Understand broadcasting rules and ufuncs.

## What to Learn
- Broadcasting rules and shape compatibility — NumPy aligns shapes from the right; dimensions of size 1 are stretched to match
  ```python
  a = np.ones((3, 4))   # shape (3, 4)
  b = np.ones((4,))     # shape    (4,) — treated as (1, 4), broadcast to (3, 4)
  (a + b).shape         # (3, 4)

  col = np.array([[1], [2], [3]])  # shape (3, 1)
  row = np.array([10, 20, 30, 40]) # shape (4,) → (1, 4)
  (col + row).shape                 # (3, 4) — outer sum
  ```
- Universal functions (ufuncs): element-wise operations
- `np.vectorize` vs true vectorization — `np.vectorize` is syntactic sugar over a Python loop; no performance benefit. True vectorization uses built-in NumPy operations which are implemented in C.
- Performance: vectorized vs loop-based approaches
- `np.einsum` basics — Einstein summation notation; concisely expresses matrix ops
  ```python
  # matrix multiply: np.einsum('ij,jk->ik', A, B) == A @ B
  # dot product:     np.einsum('i,i->', a, b)  == np.dot(a, b)
  # trace:           np.einsum('ii->', A)       == np.trace(A)
  ```

## Exercises

Implement the functions in `solution.py`.

### 1. `pairwise_distances(points) -> np.ndarray`
Given an (N, D) array of N points in D dimensions, return an (N, N) Euclidean distance matrix. No loops.
```python
pts = np.array([[0, 0], [3, 4], [1, 1]])
pairwise_distances(pts)
# array([[0.        , 5.        , 1.41421356],
#        [5.        , 0.        , 3.60555128],
#        [1.41421356, 3.60555128, 0.        ]])
```

### 2. `normalize_rows(mat) -> np.ndarray`
Normalize each row to unit length (L2 norm). Handle zero-rows by leaving them as zeros.
```python
normalize_rows(np.array([[3.0, 4.0], [0.0, 0.0], [1.0, 0.0]]))
# array([[0.6, 0.8], [0. , 0. ], [1. , 0. ]])
```

### 3. `apply_discount_matrix(prices, discount_tiers) -> np.ndarray`
`prices` is (N,), `discount_tiers` is (M,). Return (N, M) matrix where each element is `price * (1 - discount)`. Use broadcasting, no loops.
```python
apply_discount_matrix(np.array([100, 200]), np.array([0.1, 0.2, 0.3]))
# array([[ 90.,  80.,  70.],
#        [180., 160., 140.]])
```

### 4. `batch_polynomial(x, coeffs) -> np.ndarray`
Evaluate polynomial for each x. `x` is (N,), `coeffs` is (D,) for degree D-1 polynomial (highest power first). Return (N,) array. Vectorized, no loops.
```python
# 2x^2 + 3x + 1
batch_polynomial(np.array([0, 1, 2]), np.array([2, 3, 1]))
# array([ 1,  6, 15])
```
