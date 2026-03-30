import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np


def dual_axis_plot(x, y1, y2, label1, label2):
    pass


def annotated_heatmap(z, x_labels, y_labels):
    pass


def waterfall_chart(categories, values):
    pass


if __name__ == "__main__":
    # Exercise 1
    x = np.arange(12)
    rng = np.random.default_rng(42)
    fig = dual_axis_plot(x, np.cumsum(rng.integers(10, 50, 12)),
                         rng.uniform(0.5, 1.0, 12),
                         "Revenue ($k)", "Conversion Rate")
    fig.show()

    # Exercise 2
    z = np.random.default_rng(42).integers(0, 100, (5, 7))
    fig = annotated_heatmap(z, [f"Day {i}" for i in range(7)], [f"Week {i}" for i in range(5)])
    fig.show()

    # Exercise 3
    fig = waterfall_chart(
        ["Revenue", "COGS", "Gross Profit", "OpEx", "Tax", "Net Income"],
        [500, -200, None, -150, -30, None]
    )
    fig.show()
