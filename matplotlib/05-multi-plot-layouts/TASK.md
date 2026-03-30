# Task 05: Multi-plot Layouts

## Objective
Build complex multi-panel figures using GridSpec, insets, shared axes, and layout engines.

## What to Learn
- `GridSpec` and `SubplotSpec` for unequal subplot sizes

```python
from matplotlib.gridspec import GridSpec
fig = plt.figure(figsize=(10, 6))
gs = GridSpec(2, 3, figure=fig)
ax_main = fig.add_subplot(gs[:, :2])  # spans all rows, first 2 cols
ax_top  = fig.add_subplot(gs[0, 2])
ax_bot  = fig.add_subplot(gs[1, 2])
```

- `fig.add_axes()` for inset axes

```python
# [left, bottom, width, height] in figure-fraction coordinates (0-1)
ax_inset = fig.add_axes([0.6, 0.6, 0.3, 0.3])
```

- Shared axes: `sharex`, `sharey`

```python
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
# zooming/panning ax1 also zooms ax2
```

- `constrained_layout` vs `tight_layout`

```python
fig, axes = plt.subplots(2, 2, constrained_layout=True)  # preferred; avoids overlap automatically
# tight_layout() is called manually and can fail with complex layouts
```

- `fig.subfigures()` for nested layouts

## Exercises

### 1. `gridspec_layout(data_main, data_hist_x, data_hist_y)`
Create a layout with a large central scatter plot and marginal histograms (top and right), like a joint plot. The scatter takes 3/4 of each dimension. No axis labels on the marginals. Return the Figure.

```python
rng = np.random.default_rng(42)
x, y = rng.multivariate_normal([0, 0], [[1, 0.5], [0.5, 1]], 500).T
fig = gridspec_layout(np.column_stack([x, y]), x, y)
```

### 2. `inset_zoom(x, y, zoom_xlim, zoom_ylim)`
Plot the full data, then add an inset axes showing a zoomed region defined by `zoom_xlim` and `zoom_ylim` (both tuples). Draw connector lines between the zoomed region and the inset. Return the Figure.

```python
x = np.linspace(0, 10, 1000)
y = np.sin(x) + 0.1 * np.random.default_rng(42).normal(size=len(x))
fig = inset_zoom(x, y, (4, 5), (-0.2, 0.2))
```

### 3. `shared_axes_grid(datasets, ncols=3)`
Plot each dataset (list of (x, y) tuples) in a grid with `ncols` columns. All subplots share x and y axes. Only leftmost column has y-labels, only bottom row has x-labels. Return the Figure.

```python
rng = np.random.default_rng(42)
datasets = [(np.sort(rng.uniform(0, 10, 50)), rng.uniform(0, 1, 50)) for _ in range(7)]
fig = shared_axes_grid(datasets, ncols=3)
```
