# Task 05: Dash Intro

## Objective
Build a basic Dash app with layout components and callbacks.

## What to Learn
- `Dash` app initialization, `app.layout`

```python
from dash import Dash, html, dcc
app = Dash(__name__)
app.layout = html.Div([
    html.H1("Title"),
    dcc.Dropdown(id="dd", options=["A", "B", "C"], value="A"),
    dcc.Graph(id="graph"),
])
```

- Core components: `dcc.Graph`, `dcc.Dropdown`, `dcc.Slider`, `dcc.Input`
- HTML components: `html.Div`, `html.H1`, etc.
- Callbacks: `@app.callback`, `Input`, `Output`, `State`

```python
from dash import callback, Input, Output, State

@app.callback(Output("graph", "figure"), Input("dd", "value"))
def update_graph(selected):
    # called whenever "dd" value changes; return a plotly Figure
    return px.bar(df[df["col"] == selected], x="x", y="y")
# State is like Input but doesn't trigger the callback when it changes
```

- Multi-output callbacks

```python
@app.callback(Output("g1", "figure"), Output("g2", "figure"), Input("dd", "value"))
def update_both(val):
    return fig1, fig2  # return one value per Output, in order
```

- Running the dev server

## Exercises

### 1. `app_basic_layout()`
Create a Dash app with: a title (H1), a dropdown with 3 options, and a `dcc.Graph`. No callback yet -- just static layout with a default figure. Return the app.

```python
app = app_basic_layout()
app.run(debug=True)
```

### 2. `app_with_callback(df)`
Dash app with a dropdown listing unique values of `df`'s first column. Selecting a value filters the df and updates a scatter plot (column 2 vs column 3). Return the app.

```python
import plotly.express as px
app = app_with_callback(px.data.gapminder().query("year == 2007"))
app.run(debug=True)
```

### 3. `app_multi_input(df)`
Dash app with two dropdowns (x-axis column, y-axis column) and a radio button for plot type (scatter/bar). A single callback updates the graph based on all three inputs. Return the app.

```python
app = app_multi_input(px.data.tips())
app.run(debug=True)
```
