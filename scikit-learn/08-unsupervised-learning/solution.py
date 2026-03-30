import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


def kmeans_iris():
    """KMeans on Iris (no labels), print centers, inertia, contingency."""
    pass


def elbow_method():
    """Run KMeans k=2..10, print inertia for each."""
    pass


def pca_iris():
    """PCA to 2D on Iris, print explained variance."""
    pass


def pca_then_kmeans():
    """Compare KMeans silhouette on original vs PCA-reduced data."""
    pass


if __name__ == "__main__":
    kmeans_iris()
    elbow_method()
    pca_iris()
    pca_then_kmeans()
