# Task 02: Graph Objects

## Objective
Use the lower-level `go` API for fine-grained control over traces and layouts.

## What to Learn
- `go.Figure`, `go.Scatter`, `go.Bar`, `go.Heatmap`
- Adding multiple traces with `fig.add_trace()`

```python
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6], name="A"))
fig.add_trace(go.Bar(x=[1, 2, 3], y=[2, 4, 2], name="B"))
```

- Layout control: axes, margins, annotations, shapes
- `fig.update_layout()` vs constructor kwargs

```python
# Equivalent; constructor is cleaner for initial config
fig = go.Figure(layout=dict(title="Title", xaxis_title="X"))
fig.update_layout(yaxis_title="Y")  # use for post-creation changes
```

- Secondary y-axes with `make_subplots(specs=[[{"secondary_y": True}]])`

```python
from plotly.subplots import make_subplots
fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(go.Scatter(x=x, y=y1, name="left"), secondary_y=False)
fig.add_trace(go.Scatter(x=x, y=y2, name="right"), secondary_y=True)
```

## Exercises

### 1. `dual_axis_plot(x, y1, y2, label1, label2)`
Line plot with two y-axes. Left axis for y1, right axis for y2. Different colors, legend. Return the Figure.

```python
import numpy as np
x = np.arange(12)
rng = np.random.default_rng(42)
fig = dual_axis_plot(x, np.cumsum(rng.integers(10, 50, 12)),
                     rng.uniform(0.5, 1.0, 12),
                     "Revenue ($k)", "Conversion Rate")
fig.show()
```

### 2. `annotated_heatmap(z, x_labels, y_labels)`
Heatmap with cell values displayed as text annotations. Add a colorbar title "Count". Return the Figure.

```python
z = np.random.default_rng(42).integers(0, 100, (5, 7))
fig = annotated_heatmap(z, [f"Day {i}" for i in range(7)], [f"Week {i}" for i in range(5)])
fig.show()
```

### 3. `waterfall_chart(categories, values)`
Build a waterfall chart using `go.Waterfall`. Categories are labels, values are deltas (positive/negative). Add a total bar at the end. Return the Figure.

```python
fig = waterfall_chart(
    ["Revenue", "COGS", "Gross Profit", "OpEx", "Tax", "Net Income"],
    [500, -200, None, -150, -30, None]  # None = subtotal
)
fig.show()
```
