from dash import Dash, html, dcc, Input, Output
import plotly.express as px


def app_basic_layout():
    pass


def app_with_callback(df):
    pass


def app_multi_input(df):
    pass


if __name__ == "__main__":
    # Uncomment one at a time to test:

    # Exercise 1
    # app = app_basic_layout()
    # app.run(debug=True)

    # Exercise 2
    # app = app_with_callback(px.data.gapminder().query("year == 2007"))
    # app.run(debug=True)

    # Exercise 3
    app = app_multi_input(px.data.tips())
    app.run(debug=True)
