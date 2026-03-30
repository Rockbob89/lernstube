# Task 04: Linear Algebra

## Objective
Use `np.linalg` and matrix operations for practical linear algebra tasks.

## What to Learn
- `@` operator, `np.dot`, `np.matmul` — `@` is the matrix multiply operator for 2D+ arrays; `np.dot` on 2D is the same; avoid for batched ops (use `np.matmul`)
  ```python
  A = np.array([[1, 2], [3, 4]])
  b = np.array([1, 2])
  A @ b          # array([ 5, 11]) — matrix-vector product
  ```
- `np.linalg`: `inv`, `det`, `eig`, `svd`, `solve`, `norm`
- Matrix decompositions and when to use them — prefer `solve` over `inv` for linear systems (more numerically stable and faster); use SVD for PCA/rank; use `lstsq` for overdetermined systems
- Least squares fitting with `np.linalg.lstsq` — finds x that minimizes ‖Ax - b‖; works even when A is non-square
  ```python
  # fit y = mx + c: build design matrix with column of x and column of 1s
  A = np.column_stack([x, np.ones_like(x)])
  coeffs, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
  m, c = coeffs
  ```

## Exercises

Implement the functions in `solution.py`.

### 1. `solve_system(A, b) -> np.ndarray | None`
Solve Ax = b. Return solution vector or `None` if singular.
```python
A = np.array([[2, 1], [5, 3]])
b = np.array([4, 7])
solve_system(A, b)  # array([5., -6.])
```

### 2. `fit_line(x, y) -> tuple[float, float]`
Fit a line y = mx + c using least squares. Return (m, c).
```python
x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2.1, 3.9, 6.2, 7.8, 10.1])
fit_line(x, y)  # approximately (1.99, 0.05)
```

### 3. `pca_reduce(data, n_components) -> np.ndarray`
Reduce (N, D) data to (N, n_components) using PCA via SVD. Center data first.
```python
data = np.random.randn(100, 5)
reduced = pca_reduce(data, 2)
reduced.shape  # (100, 2)
```

### 4. `matrix_power_stable(mat, n) -> np.ndarray`
Compute matrix power mat^n using eigendecomposition (more stable for large n than repeated multiplication).
```python
m = np.array([[1, 1], [0, 1]], dtype=float)
matrix_power_stable(m, 3)
# array([[1., 3.], [0., 1.]])
```
