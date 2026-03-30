import numpy as np
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer


def scale_wine():
    """Load wine dataset, apply StandardScaler, print before/after stats."""
    pass


def encode_colors():
    """OneHotEncode a color column, print encoded array and categories."""
    pass


def impute_missing():
    """Impute NaN values with median, print before/after."""
    pass


def column_transform():
    """Build ColumnTransformer for mixed numeric/categorical data."""
    pass


if __name__ == "__main__":
    scale_wine()
    encode_colors()
    impute_missing()
    column_transform()
