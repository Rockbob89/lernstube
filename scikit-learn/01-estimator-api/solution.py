from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def load_and_split():
    """Load Iris dataset, split 80/20, print shapes."""
    pass


def predict_iris(n_neighbors=3):
    """Train KNN on Iris, predict on test set, print accuracy."""
    pass


def inspect_estimator():
    """Fit KNN and print classes_, n_features_in_, effective_metric_."""
    pass


def predict_iris_tree():
    """Same as predict_iris but with DecisionTreeClassifier."""
    pass


if __name__ == "__main__":
    load_and_split()
    predict_iris(n_neighbors=3)
    inspect_estimator()
    predict_iris_tree()
