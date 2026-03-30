# Task 01: Plotly Express

## Objective
Use the high-level Plotly Express API for quick, expressive charts.

## What to Learn
- `px.scatter`, `px.line`, `px.bar`, `px.histogram`, `px.box`
- Common kwargs: color, size, facet_col, facet_row, animation_frame

```python
# animation_frame turns a column into a slider that steps through values
fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year",
                 size="pop", color="continent", log_x=True)
```

- Trendlines with `trendline="ols"`

```python
fig = px.scatter(df, x="total_bill", y="tip", trendline="ols")
# requires statsmodels installed; one trendline per color group
```

- `fig.update_layout()` and `fig.update_traces()` for post-creation tweaks

```python
fig.update_layout(title="My Chart", showlegend=False)
fig.update_traces(marker=dict(size=10, opacity=0.7))
```

- `fig.show()` vs `fig.write_html()`

```python
fig.show()                     # opens browser (or renders in notebook)
fig.write_html("chart.html")   # self-contained interactive HTML file
```

## Exercises

### 1. `faceted_scatter(df, x, y, color, facet_col)`
Create a faceted scatter plot. Return the Figure.

```python
import plotly.express as px
df = px.data.tips()
fig = faceted_scatter(df, "total_bill", "tip", "smoker", "time")
fig.show()
```

### 2. `animated_bar(df, x, y, color, animation_frame)`
Create an animated bar chart. Return the Figure.

```python
df = px.data.gapminder()
fig = animated_bar(
    df.query("continent == 'Europe' and year >= 1990"),
    "country", "gdpPercap", "country", "year"
)
fig.show()
```

### 3. `scatter_with_trendline(df, x, y, color=None)`
Scatter with OLS trendline per group (if color is given) or overall. Return the Figure.

```python
df = px.data.tips()
fig = scatter_with_trendline(df, "total_bill", "tip", color="sex")
fig.show()
```
