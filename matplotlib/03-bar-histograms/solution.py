import matplotlib.pyplot as plt
import numpy as np


def grouped_bar_chart(categories, group_data):
    pass


def stacked_bar_chart(categories, group_data):
    pass


def histogram_comparison(datasets, labels, bins=30):
    pass


if __name__ == "__main__":
    # Exercise 1
    fig = grouped_bar_chart(
        ["Q1", "Q2", "Q3", "Q4"],
        {"Product A": [20, 35, 30, 35], "Product B": [25, 32, 34, 20]}
    )
    plt.show()

    # Exercise 2
    fig = stacked_bar_chart(
        ["Engineering", "Marketing", "Sales"],
        {"Salary": [500, 300, 200], "Tools": [100, 150, 50], "Travel": [50, 200, 150]}
    )
    plt.show()

    # Exercise 3
    rng = np.random.default_rng(42)
    fig = histogram_comparison(
        [rng.normal(0, 1, 1000), rng.normal(2, 1.5, 1000)],
        ["Control", "Treatment"],
    )
    plt.show()
