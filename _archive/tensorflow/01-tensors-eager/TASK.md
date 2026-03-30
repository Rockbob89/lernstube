# Task 1: Tensors & Eager Execution

## Objective
Understand TensorFlow tensors, eager execution, `tf.function` for graph mode, and `GradientTape` for computing gradients.

## What to Learn
- `tf.constant()`, `tf.Variable()`, `tf.zeros()`, `tf.ones()`, `tf.random.normal()`
- Tensor attributes: `.shape`, `.dtype`, `.numpy()`
- Operations: arithmetic, matmul (`@`), reshaping, slicing
- `tf.function` decorator and tracing behavior
  ```python
  @tf.function
  def add(a, b):
      return a + b
  # First call with (float32, float32) traces + compiles a graph
  # Second call with same signature reuses the graph (faster)
  # Different dtypes or ranks → retrace
  ```
- `tf.GradientTape` for manual gradient computation
  ```python
  x = tf.Variable(2.0)
  with tf.GradientTape() as tape:
      y = x ** 3
  grad = tape.gradient(y, x)  # dy/dx = 3x^2 = 12.0
  ```
- Differences: `tf.constant` (immutable) vs `tf.Variable` (mutable)
  ```python
  c = tf.constant([1.0, 2.0])  # fixed — no assign method
  v = tf.Variable([1.0, 2.0])  # mutable
  v.assign([3.0, 4.0])         # in-place update, tracked by GradientTape
  ```

## Exercises

### 1. `create_tensors()`
Return a dict with:
- `"zeros"`: 3x4 float tensor of zeros
- `"ones"`: 2x2 int tensor of ones
- `"random"`: 5x5 tensor from standard normal
- `"range"`: 1D tensor [0, 2, 4, 6, 8] using `tf.range`
- `"variable"`: a `tf.Variable` initialized to [[1.0, 2.0], [3.0, 4.0]]

```python
result = create_tensors()
assert result["zeros"].shape == (3, 4)
assert result["range"].numpy().tolist() == [0, 2, 4, 6, 8]
assert isinstance(result["variable"], tf.Variable)
```

### 2. `tensor_ops(a, b)`
Given two 1D tensors of same length, return a dict:
- `"dot"`: dot product (scalar)
- `"stack"`: stack into 2xN matrix
- `"norm"`: L2 norm of `a`

```python
a = tf.constant([1.0, 2.0, 3.0])
b = tf.constant([4.0, 5.0, 6.0])
result = tensor_ops(a, b)
assert result["dot"].numpy() == 32.0
assert result["stack"].shape == (2, 3)
```

### 3. `gradient_tape_demo(x_val)`
Use `GradientTape` to compute dy/dx for `y = x^3 + 2x^2 - 5x + 3`. Return the gradient value as a float.

```python
assert gradient_tape_demo(2.0) == 15.0  # 3*4 + 4*2 - 5
assert gradient_tape_demo(0.0) == -5.0
```

### 4. `tf_function_demo()`
Create a function that multiplies two tensors, decorate it with `@tf.function`. Call it twice with same-shape inputs, then once with a different shape. Return a dict:
- `"same_shape_result"`: result of the second call (same shape as first)
- `"diff_shape_result"`: result of the call with different shape
- `"num_traces"`: number of times the function was traced (int)

Hint for verifying: `tf.function` retraces when input signatures change.

```python
result = tf_function_demo()
assert result["num_traces"] == 2  # one per distinct input shape
```
