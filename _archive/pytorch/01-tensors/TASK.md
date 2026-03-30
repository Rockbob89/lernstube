# Task 1: Tensors

## Objective
Understand PyTorch tensors as the fundamental data structure — creation, manipulation, device placement, and relationship to NumPy.

## What to Learn
- Creating tensors: `torch.tensor()`, `torch.zeros()`, `torch.ones()`, `torch.randn()`, `torch.arange()`
- Tensor attributes: `.shape`, `.dtype`, `.device`
- Operations: arithmetic, matrix multiplication (`@`, `torch.matmul`), reshaping (`.view()`, `.reshape()`), slicing
- NumPy interop: `.numpy()`, `torch.from_numpy()` (shared memory!)
  ```python
  import numpy as np
  arr = np.array([1.0, 2.0])
  t = torch.from_numpy(arr)  # shared memory — modifying arr changes t
  arr[0] = 99.0
  print(t)  # tensor([99., 2.]) — same buffer
  ```
- Device placement: `.to("cuda")`, `.cpu()`, `torch.cuda.is_available()`
  ```python
  device = "cuda" if torch.cuda.is_available() else "cpu"
  t = torch.randn(3, 3).to(device)
  ```
- In-place operations (trailing `_`) vs out-of-place
  ```python
  x = torch.tensor([1.0, 2.0])
  x.add_(1)   # in-place: modifies x, no new allocation
  y = x.add(1)  # out-of-place: returns new tensor, x unchanged
  ```

## Exercises

### 1. `create_tensors()`
Return a dict with keys:
- `"zeros"`: 3x4 float tensor of zeros
- `"ones"`: 2x2 int tensor of ones
- `"random"`: 5x5 tensor from standard normal
- `"range"`: 1D tensor [0, 2, 4, 6, 8]

```python
result = create_tensors()
assert result["zeros"].shape == (3, 4)
assert result["range"].tolist() == [0, 2, 4, 6, 8]
```

### 2. `tensor_ops(a, b)`
Given two 1D tensors of same length, return a dict:
- `"dot"`: dot product (scalar tensor)
- `"stack"`: stack them into a 2xN matrix
- `"norm"`: L2 norm of `a` (scalar tensor)

```python
a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])
result = tensor_ops(a, b)
assert result["dot"].item() == 32.0
assert result["stack"].shape == (2, 3)
```

### 3. `reshape_drill(x)`
Given a 1D tensor of 24 elements, return a dict:
- `"mat"`: reshaped to 4x6
- `"cube"`: reshaped to 2x3x4
- `"flat"`: flattened back to 1D

```python
x = torch.arange(24, dtype=torch.float32)
result = reshape_drill(x)
assert result["cube"].shape == (2, 3, 4)
assert result["flat"].shape == (24,)
```

### 4. `numpy_roundtrip(np_array)`
Take a NumPy array, convert to tensor, multiply by 2, convert back to NumPy. Return the NumPy array. Ensure the original is not modified.

```python
import numpy as np
arr = np.array([1.0, 2.0, 3.0])
result = numpy_roundtrip(arr)
assert (result == [2.0, 4.0, 6.0]).all()
assert (arr == [1.0, 2.0, 3.0]).all()  # original unchanged
```
