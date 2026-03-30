# Task 03: Interactivity

## Objective
Add interactive controls to Plotly figures: hover templates, dropdowns, sliders, and buttons.

## What to Learn
- Custom hover templates with `hovertemplate`

```python
fig.update_traces(
    hovertemplate="<b>%{customdata[0]}</b><br>GDP: %{x:,.0f}<br>Life Exp: %{y:.1f}<extra></extra>"
    # <extra></extra> suppresses the default trace name tooltip box
)
```

- `updatemenus`: dropdown menus and buttons via `fig.update_layout(updatemenus=[...])`

```python
fig.update_layout(updatemenus=[dict(
    buttons=[
        dict(label="Show A", method="update", args=[{"visible": [True, False]}]),
        dict(label="Show B", method="update", args=[{"visible": [False, True]}]),
    ],
    x=0.1, y=1.15, direction="down"
)])
```

- `sliders` for frame-based or parameter-based navigation
- Visibility toggling traces with `args=[{"visible": [...]}]`

```python
# visible list must have one entry per trace in the figure
args=[{"visible": [True, False, False]}]  # only first trace shown
```

- Click events conceptually (full handling requires Dash)

## Exercises

### 1. `hover_template_scatter(df, x, y, hover_cols)`
Scatter plot with a custom hover template showing all columns in `hover_cols` with their column names as labels. Return the Figure.

```python
import plotly.express as px
df = px.data.gapminder().query("year == 2007")
fig = hover_template_scatter(df, "gdpPercap", "lifeExp", ["country", "pop", "continent"])
fig.show()
```

### 2. `dropdown_filter_plot(df, x, y, filter_col)`
Line/scatter plot with a dropdown menu that filters by unique values of `filter_col`. One menu option per unique value, plus "All". Return the Figure.

```python
df = px.data.gapminder().query("country in ['Germany','France','Spain','Italy']")
fig = dropdown_filter_plot(df, "year", "gdpPercap", "country")
fig.show()
```

### 3. `slider_parameter_plot(x, func_dict)`
Build a figure with a slider that switches between mathematical functions. `func_dict` maps label -> y-values. Use `go.Figure` with `go.Scatter` traces (one per function, only the first visible). Add a `sliders` entry to the layout where each step sets the matching trace visible and hides the rest. Return the Figure.

```python
import numpy as np
x = np.linspace(0, 4 * np.pi, 200)
fig = slider_parameter_plot(x, {
    "sin": np.sin(x),
    "cos": np.cos(x),
    "sinc": np.sinc(x / np.pi),
})
fig.show()
```
