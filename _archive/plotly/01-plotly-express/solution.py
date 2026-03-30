import plotly.express as px


def faceted_scatter(df, x, y, color, facet_col):
    pass


def animated_bar(df, x, y, color, animation_frame):
    pass


def scatter_with_trendline(df, x, y, color=None):
    pass


if __name__ == "__main__":
    # Exercise 1
    df = px.data.tips()
    fig = faceted_scatter(df, "total_bill", "tip", "smoker", "time")
    fig.show()

    # Exercise 2
    df = px.data.gapminder()
    fig = animated_bar(
        df.query("continent == 'Europe' and year >= 1990"),
        "country", "gdpPercap", "country", "year"
    )
    fig.show()

    # Exercise 3
    df = px.data.tips()
    fig = scatter_with_trendline(df, "total_bill", "tip", color="sex")
    fig.show()
