import numpy as np
from sklearn.datasets import load_diabetes, load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso
from sklearn.metrics import r2_score, accuracy_score


def linear_regression_diabetes():
    """Train LinearRegression on diabetes, print R² and top features."""
    pass


def logistic_breast_cancer():
    """Train LogisticRegression on breast cancer, print accuracy and coef signs."""
    pass


def compare_regularization():
    """Compare LinearRegression, Ridge, Lasso on diabetes dataset."""
    pass


def alpha_sweep():
    """Train Lasso with varying alphas, observe sparsity vs performance."""
    pass


if __name__ == "__main__":
    linear_regression_diabetes()
    logistic_breast_cancer()
    compare_regularization()
    alpha_sweep()
