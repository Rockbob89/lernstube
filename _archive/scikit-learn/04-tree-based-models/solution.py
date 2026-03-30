import numpy as np
from sklearn.datasets import load_iris, load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score


def tree_overfit_demo():
    """Show overfitting with unlimited depth vs constrained tree."""
    pass


def random_forest_wine():
    """Train RandomForest on wine, print accuracy and top features."""
    pass


def gradient_boosting_wine():
    """Train GradientBoosting on wine, compare with RF."""
    pass


def compare_importances():
    """Side-by-side feature importances from RF and GB."""
    pass


if __name__ == "__main__":
    tree_overfit_demo()
    random_forest_wine()
    gradient_boosting_wine()
    compare_importances()
