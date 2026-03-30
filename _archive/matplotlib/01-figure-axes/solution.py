import matplotlib.pyplot as plt
import numpy as np


def create_figure_with_axes(nrows, ncols):
    pass


def labeled_plot(x, y, title, xlabel, ylabel):
    pass


def save_figure(fig, path, dpi=150):
    pass


if __name__ == "__main__":
    # Exercise 1
    fig, axes = create_figure_with_axes(2, 3)
    print(f"Figure size: {fig.get_size_inches()}")
    print(f"Axes shape: {axes.shape}")

    # Exercise 2
    x = np.linspace(0, 2 * np.pi, 100)
    fig = labeled_plot(x, np.sin(x), "Sine Wave", "Radians", "Amplitude")
    plt.show()

    # Exercise 3
    save_figure(fig, "output.png", dpi=300)
