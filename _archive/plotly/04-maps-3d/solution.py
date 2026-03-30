import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd


def choropleth_map(df, locations, color, location_mode="ISO-3166-1 alpha-3"):
    pass


def scatter_geo_plot(df, lat, lon, size, color, hover_name):
    pass


def surface_3d(x, y, z_func):
    pass


if __name__ == "__main__":
    # Exercise 1
    df = px.data.gapminder().query("year == 2007")
    fig = choropleth_map(df, "iso_alpha", "gdpPercap")
    fig.show()

    # Exercise 2
    cities = pd.DataFrame({
        "city": ["Berlin", "Paris", "Madrid", "Rome", "London"],
        "lat": [52.52, 48.86, 40.42, 41.90, 51.51],
        "lon": [13.40, 2.35, -3.70, 12.50, -0.13],
        "pop_m": [3.6, 2.1, 3.2, 2.8, 8.9],
        "gdp_idx": [110, 105, 95, 90, 120],
    })
    fig = scatter_geo_plot(cities, "lat", "lon", "pop_m", "gdp_idx", "city")
    fig.show()

    # Exercise 3
    fig = surface_3d(
        np.linspace(-3, 3, 50),
        np.linspace(-3, 3, 50),
        lambda X, Y: np.sin(np.sqrt(X**2 + Y**2))
    )
    fig.show()
