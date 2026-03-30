import numpy as np
from scipy.stats import randint
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier


def grid_search_svc():
    """GridSearchCV on SVC with wine dataset."""
    pass


def random_search_rf():
    """RandomizedSearchCV on RandomForest with wine dataset."""
    pass


def tune_pipeline():
    """GridSearchCV on a Pipeline with StandardScaler + SVC."""
    pass


def analyze_results():
    """Extract and display cv_results_ as a ranked table."""
    pass


if __name__ == "__main__":
    grid_search_svc()
    random_search_rf()
    tune_pipeline()
    analyze_results()
