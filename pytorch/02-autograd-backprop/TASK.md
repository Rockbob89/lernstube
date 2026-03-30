# Task 2: Autograd & Backprop

## Objective
Understand PyTorch's automatic differentiation engine — how gradients are computed, the computational graph, and how to control gradient tracking.

## What to Learn
- `requires_grad=True` and the computational graph
  ```python
  x = torch.tensor(2.0, requires_grad=True)
  y = x ** 3       # builds graph: y depends on x
  y.backward()     # computes dy/dx
  print(x.grad)    # tensor(12.) — dy/dx = 3x^2 at x=2
  ```
- `.backward()` to compute gradients
- `.grad` attribute on leaf tensors
- `torch.no_grad()` context manager
  ```python
  with torch.no_grad():
      pred = model(x)  # no graph built — faster inference, less memory
  ```
- `.detach()` to break graph connections
  ```python
  y = model(x)
  z = y.detach()  # z has the same values but no gradient history
  ```
- Gradient accumulation and `.zero_()` for clearing
  ```python
  # PyTorch accumulates gradients by default — you must clear before each step
  optimizer.zero_grad()  # same as model.parameters() zero_()
  loss.backward()
  optimizer.step()
  ```

## Exercises

### 1. `manual_gradient(x_val)`
Create a scalar tensor `x` with value `x_val` and `requires_grad=True`. Compute `y = x^3 + 2x^2 - 5x + 3`. Call `.backward()`. Return `x.grad.item()` (the derivative dy/dx evaluated at x_val).

Verify: dy/dx = 3x^2 + 4x - 5

```python
assert manual_gradient(2.0) == 15.0   # 3*4 + 4*2 - 5
assert manual_gradient(0.0) == -5.0
```

### 2. `gradient_accumulation()`
Demonstrate that gradients accumulate. Create `x = tensor(1.0, requires_grad=True)`. Compute `y = x * 2` and call backward twice without zeroing. Return the accumulated gradient value.

```python
assert gradient_accumulation() == 4.0  # 2.0 + 2.0
```

### 3. `no_grad_demo(x_val)`
Create `x` with `requires_grad=True`. Inside `torch.no_grad()`, compute `y = x * 3`. Return a dict:
- `"y_value"`: y.item()
- `"y_requires_grad"`: y.requires_grad (should be False)
- `"x_requires_grad"`: x.requires_grad (should still be True)

```python
result = no_grad_demo(5.0)
assert result["y_value"] == 15.0
assert result["y_requires_grad"] is False
assert result["x_requires_grad"] is True
```

### 4. `detach_demo(x_val)`
Create `x` with `requires_grad=True`. Compute `y = x ** 2`. Detach `y` to get `z`. Compute `w = z + 1`. Return a dict:
- `"z_requires_grad"`: z.requires_grad
- `"w_value"`: w.item()
- `"can_backward"`: whether calling w.backward() would raise an error (bool: True if error)

```python
result = detach_demo(3.0)
assert result["z_requires_grad"] is False
assert result["w_value"] == 10.0
```
