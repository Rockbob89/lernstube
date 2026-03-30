# Task 1: Estimator API

## Objective
Understand scikit-learn's core abstraction: the Estimator API. Every model in sklearn follows the same fit/predict/transform pattern. Master this and the entire library becomes predictable.

## What to Learn
- The three core methods: `fit()`, `predict()`, `transform()`
- Estimator vs Transformer vs Predictor distinction
- Loading built-in datasets (`sklearn.datasets`)
- `train_test_split` for holdout validation
- Inspecting fitted attributes (those ending with `_`)

```python
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)
# Attributes set by fit() always end with _:
print(clf.classes_)          # learned class labels
print(clf.n_features_in_)    # number of features seen during fit
```

## Exercises

### 1. Load and Split
Load the Iris dataset. Split it 80/20 with `random_state=42`. Print the shapes of all four arrays.

```python
# Expected output:
# X_train: (120, 4)
# X_test: (30, 4)
# y_train: (120,)
# y_test: (30,)
```

### 2. Fit and Predict
Train a `KNeighborsClassifier(n_neighbors=3)` on the training set. Predict on the test set. Print accuracy using `accuracy_score`.

```python
predict_iris(n_neighbors=3)
# Expected: accuracy around 0.96-1.0
```

### 3. Inspect the Estimator
After fitting, print `classes_`, `n_features_in_`, and `effective_metric_`. These are fitted attributes sklearn exposes after `fit()`.

```python
inspect_estimator()
# classes_: [0 1 2]
# n_features_in_: 4
# effective_metric_: 'minkowski'
```

### 4. Swap the Estimator
Replace KNN with `DecisionTreeClassifier(random_state=42)`. Change only the model — the rest of the code should work identically. Print accuracy.

```python
predict_iris_tree()
# Expected: accuracy around 0.96-1.0
```
