# Task 01: Arrays & dtypes

## Objective
Master NumPy array creation, shape manipulation, and dtype control.

## What to Learn
- `np.array`, `np.zeros`, `np.ones`, `np.arange`, `np.linspace`
- `.shape`, `.ndim`, `.size`, `.dtype`
- `reshape`, `ravel`, `flatten`, `transpose`
- dtype specification and casting (`astype`)
- Difference between C-order and Fortran-order memory layout — affects iteration performance; C-order (default) stores rows contiguously, Fortran-order stores columns contiguously
  ```python
  a = np.array([[1, 2], [3, 4]], order='C')  # row-major: [1,2,3,4] in memory
  b = np.array([[1, 2], [3, 4]], order='F')  # col-major: [1,3,2,4] in memory
  a.flags['C_CONTIGUOUS']  # True
  b.flags['F_CONTIGUOUS']  # True
  ```

## Exercises

Implement the functions in `solution.py`.

### 1. `create_checkerboard(n) -> np.ndarray`
Create an n x n checkerboard pattern of 0s and 1s (dtype `int8`).
```python
create_checkerboard(4)
# array([[0, 1, 0, 1],
#        [1, 0, 1, 0],
#        [0, 1, 0, 1],
#        [1, 0, 1, 0]], dtype=int8)
```

### 2. `reshape_safe(arr, shape) -> np.ndarray | None`
Reshape array to given shape. Return `None` if incompatible (don't raise).
```python
reshape_safe(np.arange(12), (3, 4))  # array([[ 0,  1,  2,  3], ...])
reshape_safe(np.arange(12), (5, 5))  # None
```

### 3. `dtype_report(arr) -> dict`
Return a dict with keys: `dtype`, `itemsize`, `total_bytes`, `shape`, `ndim`.
```python
dtype_report(np.zeros((3, 4), dtype=np.float32))
# {'dtype': dtype('float32'), 'itemsize': 4, 'total_bytes': 48, 'shape': (3, 4), 'ndim': 2}
```

### 4. `memory_efficient_range(start, stop, step) -> np.ndarray`
Like `np.arange` but always returns the smallest integer dtype that fits the values.
```python
memory_efficient_range(0, 100, 1).dtype   # dtype('int8')
memory_efficient_range(0, 300, 1).dtype   # dtype('int16')
```
