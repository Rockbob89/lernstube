# Task 04: Maps & 3D

## Objective
Build geographic visualizations and 3D plots with Plotly.

## What to Learn
- `px.choropleth` / `go.Choropleth`: country-level data, GeoJSON
- `px.scatter_geo` / `go.Scattergeo`: point data on maps
- Map projections and `fitbounds`

```python
fig = px.choropleth(df, locations="iso_alpha", color="gdpPercap",
                    projection="natural earth")
fig.update_geos(fitbounds="locations")  # zoom to data extent
```

- `px.scatter_3d`, `go.Scatter3d`, `go.Surface`
- Camera angle control with `scene.camera`

```python
fig.update_layout(scene_camera=dict(
    eye=dict(x=1.5, y=1.5, z=0.8)  # x/y/z distance from origin
))
```

## Exercises

### 1. `choropleth_map(df, locations, color, location_mode="ISO-3166-1 alpha-3")`
Choropleth map colored by `color` column. Use natural earth projection. Add a descriptive colorbar title. Return the Figure.

```python
df = px.data.gapminder().query("year == 2007")
fig = choropleth_map(df, "iso_alpha", "gdpPercap")
fig.show()
```

### 2. `scatter_geo_plot(df, lat, lon, size, color, hover_name)`
Scatter points on a map with variable size and color. Return the Figure.

```python
# Use any city dataset or fabricate one
import pandas as pd
cities = pd.DataFrame({
    "city": ["Berlin", "Paris", "Madrid", "Rome", "London"],
    "lat": [52.52, 48.86, 40.42, 41.90, 51.51],
    "lon": [13.40, 2.35, -3.70, 12.50, -0.13],
    "pop_m": [3.6, 2.1, 3.2, 2.8, 8.9],
    "gdp_idx": [110, 105, 95, 90, 120],
})
fig = scatter_geo_plot(cities, "lat", "lon", "pop_m", "gdp_idx", "city")
fig.show()
```

### 3. `surface_3d(x, y, z_func)`
3D surface plot where `z_func(X, Y)` computes Z from meshgrid arrays. Add axis labels. Return the Figure.

```python
import numpy as np
fig = surface_3d(
    np.linspace(-3, 3, 50),
    np.linspace(-3, 3, 50),
    lambda X, Y: np.sin(np.sqrt(X**2 + Y**2))
)
fig.show()
```
