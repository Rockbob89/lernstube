# Task 01: Figure & Axes

## Objective
Understand the matplotlib object model: Figure, Axes, and the difference between the OO API and pyplot.

## What to Learn
- `plt.subplots()` vs `plt.figure()` + `fig.add_subplot()`

```python
fig, axes = plt.subplots(2, 3, figsize=(12, 6))  # preferred
# or equivalently:
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(2, 3, 1)  # 1-indexed: row, col, index
```

- Figure vs Axes: what lives where (title, labels, legend on Axes; size, dpi, savefig on Figure)

```python
fig, ax = plt.subplots()
ax.set_title("title")      # on Axes
ax.set_xlabel("x")         # on Axes
fig.savefig("out.png")     # on Figure
```

- pyplot state machine vs explicit OO API

```python
# pyplot (implicit, operates on "current" axes):
plt.plot([1, 2, 3])
plt.title("implicit")

# OO (explicit, preferred for anything non-trivial):
fig, ax = plt.subplots()
ax.plot([1, 2, 3])
ax.set_title("explicit")
```

- When to use which approach

## Exercises

### 1. `create_figure_with_axes(nrows, ncols)`
Create and return a Figure with the given grid of Axes. Set figure size to `(4*ncols, 3*nrows)`.

```python
fig, axes = create_figure_with_axes(2, 3)
# fig.get_size_inches() -> (12, 6)
# axes.shape -> (2, 3)
```

### 2. `labeled_plot(x, y, title, xlabel, ylabel)`
Create a single-axes figure, plot y vs x, apply all labels. Return the Figure.

```python
import numpy as np
x = np.linspace(0, 2*np.pi, 100)
fig = labeled_plot(x, np.sin(x), "Sine Wave", "Radians", "Amplitude")
```

### 3. `save_figure(fig, path, dpi=150)`
Save a figure to disk at the given dpi. Use `bbox_inches='tight'`.

```python
save_figure(fig, "output.png", dpi=300)
```
