import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np


def gridspec_layout(data_main, data_hist_x, data_hist_y):
    pass


def inset_zoom(x, y, zoom_xlim, zoom_ylim):
    pass


def shared_axes_grid(datasets, ncols=3):
    pass


if __name__ == "__main__":
    rng = np.random.default_rng(42)

    # Exercise 1
    x, y = rng.multivariate_normal([0, 0], [[1, 0.5], [0.5, 1]], 500).T
    fig = gridspec_layout(np.column_stack([x, y]), x, y)
    plt.show()

    # Exercise 2
    x = np.linspace(0, 10, 1000)
    y = np.sin(x) + 0.1 * rng.normal(size=len(x))
    fig = inset_zoom(x, y, (4, 5), (-0.2, 0.2))
    plt.show()

    # Exercise 3
    datasets = [(np.sort(rng.uniform(0, 10, 50)), rng.uniform(0, 1, 50)) for _ in range(7)]
    fig = shared_axes_grid(datasets, ncols=3)
    plt.show()
