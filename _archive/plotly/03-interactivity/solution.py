import plotly.express as px
import plotly.graph_objects as go


def hover_template_scatter(df, x, y, hover_cols):
    pass


def dropdown_filter_plot(df, x, y, filter_col):
    pass


def slider_parameter_plot(x, func_dict):
    pass


if __name__ == "__main__":
    import numpy as np

    # Exercise 1
    df = px.data.gapminder().query("year == 2007")
    fig = hover_template_scatter(df, "gdpPercap", "lifeExp", ["country", "pop", "continent"])
    fig.show()

    # Exercise 2
    df = px.data.gapminder().query("country in ['Germany','France','Spain','Italy']")
    fig = dropdown_filter_plot(df, "year", "gdpPercap", "country")
    fig.show()

    # Exercise 3
    x = np.linspace(0, 4 * np.pi, 200)
    fig = slider_parameter_plot(x, {
        "sin": np.sin(x),
        "cos": np.cos(x),
        "sinc": np.sinc(x / np.pi),
    })
    fig.show()
