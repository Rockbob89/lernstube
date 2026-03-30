import numpy as np
from sklearn.datasets import load_breast_cancer, load_wine, make_classification
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report,
    roc_curve, roc_auc_score,
)


def full_evaluation():
    """Train LogisticRegression on breast cancer, print classification_report and confusion_matrix."""
    pass


def roc_analysis():
    """Compute ROC curve and AUC on breast cancer dataset."""
    pass


def cross_validate_wine():
    """5-fold cross-validation with RandomForest on wine."""
    pass


def imbalanced_metrics():
    """Show why accuracy misleads on imbalanced data."""
    pass


if __name__ == "__main__":
    full_evaluation()
    roc_analysis()
    cross_validate_wine()
    imbalanced_metrics()
