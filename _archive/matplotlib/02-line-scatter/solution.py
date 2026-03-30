import matplotlib.pyplot as plt
import numpy as np


def multi_line_plot(x, y_dict):
    pass


def styled_scatter(x, y, sizes, colors, cmap="viridis"):
    pass


def annotated_peaks(x, y, n_peaks=3):
    pass


if __name__ == "__main__":
    # Exercise 1
    x = np.linspace(0, 10, 100)
    fig = multi_line_plot(x, {
        "sin": np.sin(x),
        "cos": np.cos(x),
        "tan_clipped": np.clip(np.tan(x), -3, 3),
    })
    plt.show()

    # Exercise 2
    rng = np.random.default_rng(42)
    n = 200
    fig = styled_scatter(rng.normal(size=n), rng.normal(size=n),
                         rng.uniform(20, 200, n), rng.uniform(0, 1, n))
    plt.show()

    # Exercise 3
    x = np.linspace(0, 4 * np.pi, 500)
    y = np.sin(x) * np.exp(-0.1 * x)
    fig = annotated_peaks(x, y, n_peaks=3)
    plt.show()
