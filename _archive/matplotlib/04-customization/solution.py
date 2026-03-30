import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.colors import LinearSegmentedColormap
import numpy as np


def apply_style_context(style_name, plot_func):
    pass


def clean_axis_plot(x, y):
    pass


def custom_colormap_heatmap(data, cmap_colors=None):
    pass


if __name__ == "__main__":
    # Exercise 1
    def my_plot():
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3], [1, 4, 9])
        return fig

    fig = apply_style_context("ggplot", my_plot)
    plt.show()

    # Exercise 2
    x = np.arange(0, 20, 0.5)
    y = np.random.default_rng(42).uniform(0, 1, len(x))
    fig = clean_axis_plot(x, y)
    plt.show()

    # Exercise 3
    data = np.random.default_rng(42).normal(size=(10, 10))
    fig = custom_colormap_heatmap(data, cmap_colors=["#000000", "#ff6600", "#ffff00"])
    plt.show()
