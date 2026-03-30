# Task 8: Unsupervised Learning

## Objective
Not all problems have labels. Learn clustering with KMeans and dimensionality reduction with PCA. Understand how to evaluate unsupervised models and when to use them.

## What to Learn
- `KMeans` — partitional clustering, inertia, elbow method

```python
from sklearn.cluster import KMeans
km = KMeans(n_clusters=3, random_state=42)
km.fit(X)
print(km.inertia_)        # sum of squared distances to nearest cluster center
print(km.cluster_centers_) # shape (n_clusters, n_features)
```

- `PCA` — principal component analysis, explained variance

```python
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
X_2d = pca.fit_transform(X)
print(pca.explained_variance_ratio_)   # fraction of variance per component
print(pca.explained_variance_ratio_.sum())  # total variance retained
```

- `silhouette_score` — cluster quality without labels

```python
from sklearn.metrics import silhouette_score
score = silhouette_score(X, km.labels_)
# ranges -1 to 1; higher = denser, better-separated clusters
```

- Combining PCA + KMeans for high-dimensional data
- Contingency tables (`pd.crosstab`) — comparing clusters to true labels

```python
import pandas as pd
pd.crosstab(y_true, km.labels_, rownames=["true"], colnames=["cluster"])
```

- When unsupervised learning is useful (exploration, preprocessing, anomaly detection)

## Exercises

### 1. KMeans Clustering
Load the Iris dataset (ignore labels). Run `KMeans(n_clusters=3, random_state=42)`. Print cluster centers shape and inertia. Compare predicted clusters to actual labels using a contingency table.

```python
kmeans_iris()
# Cluster centers shape: (3, 4)
# Inertia: ~78.xx
# Contingency table printed
```

### 2. Elbow Method
Run KMeans with k=2..10 on Iris. Print inertia for each k. Identify the "elbow" (diminishing returns point).

```python
elbow_method()
# k=2: inertia=xxx
# k=3: inertia=xxx
# ...
```

### 3. PCA
Apply `PCA(n_components=2)` to the Iris dataset. Print `explained_variance_ratio_` and total variance explained. Print the shape before and after.

```python
pca_iris()
# Shape: (150, 4) -> (150, 2)
# Variance explained: [0.xx, 0.xx]
# Total: 0.xx
```

### 4. PCA + KMeans
Apply PCA(n_components=2) to Iris, then KMeans(n_clusters=3). Print silhouette score. Compare with KMeans on the original 4D data.

```python
pca_then_kmeans()
# Silhouette (4D): 0.xx
# Silhouette (2D after PCA): 0.xx
```
