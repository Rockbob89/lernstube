# Task 5: Model Evaluation

## Objective
Accuracy alone is misleading. Learn the full evaluation toolkit: precision, recall, F1, confusion matrix, ROC/AUC, and cross-validation. Know which metric to use for which problem.

## What to Learn
- `accuracy_score`, `precision_score`, `recall_score`, `f1_score`
- `confusion_matrix`, `classification_report`
- `roc_curve`, `roc_auc_score` — threshold-independent evaluation

```python
from sklearn.metrics import roc_curve, roc_auc_score
y_prob = clf.predict_proba(X_test)[:, 1]  # probability of positive class
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
auc = roc_auc_score(y_test, y_prob)
# fpr/tpr/thresholds are arrays; plot fpr vs tpr to get the ROC curve
```

- `cross_val_score` — k-fold cross-validation

```python
from sklearn.model_selection import cross_val_score
scores = cross_val_score(clf, X, y, cv=5, scoring="f1")
# Handles train/test splitting internally; never call fit() first
print(scores.mean(), scores.std())
```

- When accuracy is the wrong metric (imbalanced classes)

## Exercises

### 1. Classification Report
Train `LogisticRegression` on the breast cancer dataset. Print the full `classification_report` and the confusion matrix.

```python
full_evaluation()
# Prints classification_report and confusion_matrix
```

### 2. ROC Curve Data
Using the same model, compute `roc_curve` and `roc_auc_score`. Print the AUC and 5 sample (fpr, tpr, threshold) points.

```python
roc_analysis()
# AUC: ~0.99
# Sample points: [(fpr, tpr, threshold), ...]
```

### 3. Cross-Validation
Run `cross_val_score` with 5 folds on `RandomForestClassifier` using the wine dataset. Print individual fold scores, mean, and std.

```python
cross_validate_wine()
# Fold scores: [0.xx, 0.xx, 0.xx, 0.xx, 0.xx]
# Mean: 0.xx, Std: 0.xx
```

### 4. Metric Selection
Create an imbalanced dataset using `make_classification(n_samples=1000, weights=[0.95, 0.05])`. Train a `DummyClassifier(strategy="most_frequent")` and a `LogisticRegression`. Compare accuracy vs F1 for both. Show why accuracy is misleading here.

```python
imbalanced_metrics()
# DummyClassifier -> accuracy: 0.95, f1: 0.00
# LogisticRegression -> accuracy: ~0.95, f1: ~0.5+
```
