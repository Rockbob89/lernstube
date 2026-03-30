# Task 02: Line & Scatter Plots

## Objective
Master line and scatter plots with full control over styling, labels, legends, and annotations.

## What to Learn
- `ax.plot()` kwargs: color, linestyle, linewidth, marker, markersize
- `ax.scatter()` kwargs: c, s, cmap, alpha, edgecolors

```python
# c = per-point color values (mapped through cmap); s = per-point size
sc = ax.scatter(x, y, c=values, s=sizes, cmap="viridis", alpha=0.7)
fig.colorbar(sc)  # colorbar must be added manually
```

- Legends: `ax.legend()` with loc, frameon, fontsize
- Annotations: `ax.annotate()` with arrowprops

```python
ax.annotate("peak", xy=(x_peak, y_peak), xytext=(x_peak + 0.5, y_peak + 0.2),
            arrowprops=dict(arrowstyle="->"))
# xy = point to annotate; xytext = where the label sits
```

- Format strings (e.g., `'ro--'`)

```python
ax.plot(x, y, 'ro--')  # r=red, o=circle marker, --=dashed line
```

## Exercises

### 1. `multi_line_plot(x, y_dict)`
Plot multiple lines on one Axes. `y_dict` maps label -> y-values. Each line gets a distinct style. Add a legend. Return the Figure.

```python
x = np.linspace(0, 10, 100)
fig = multi_line_plot(x, {
    "sin": np.sin(x),
    "cos": np.cos(x),
    "tan_clipped": np.clip(np.tan(x), -3, 3),
})
```

### 2. `styled_scatter(x, y, sizes, colors, cmap="viridis")`
Scatter plot with variable size and color. Add a colorbar. Return the Figure.

```python
rng = np.random.default_rng(42)
n = 200
fig = styled_scatter(rng.normal(size=n), rng.normal(size=n),
                     rng.uniform(20, 200, n), rng.uniform(0, 1, n))
```

### 3. `annotated_peaks(x, y, n_peaks=3)`
Plot a line, find the top `n_peaks` by y-value, annotate each with an arrow pointing to the peak and text showing the y-value rounded to 2 decimals. Return the Figure.

```python
x = np.linspace(0, 4*np.pi, 500)
y = np.sin(x) * np.exp(-0.1*x)
fig = annotated_peaks(x, y, n_peaks=3)
```
