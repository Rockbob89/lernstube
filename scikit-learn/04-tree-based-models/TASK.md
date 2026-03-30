# Task 4: Tree-Based Models

## Objective
Tree-based models are the workhorses of tabular ML. Learn decision trees, random forests, and gradient boosting. Understand why ensembles beat single trees and how feature importance works.

## What to Learn
- `DecisionTreeClassifier` / `DecisionTreeRegressor` — interpretable but overfit-prone
- `RandomForestClassifier` — bagging ensemble, reduces variance
- `GradientBoostingClassifier` — boosting ensemble, reduces bias
- `feature_importances_` — which features matter

```python
rf.fit(X_train, y_train)
importances = rf.feature_importances_   # array of shape (n_features,), sums to 1
top = sorted(zip(feature_names, importances), key=lambda t: t[1], reverse=True)
```

- `max_depth`, `n_estimators`, `learning_rate` — key hyperparameters

## Exercises

### 1. Decision Tree Overfitting
Train a `DecisionTreeClassifier` on Iris with no depth limit. Print train and test accuracy. Then train with `max_depth=3` and compare.

```python
tree_overfit_demo()
# No limit  -> train: 1.00, test: ~0.96
# max_depth=3 -> train: ~0.98, test: ~0.96
```

### 2. Random Forest
Train `RandomForestClassifier(n_estimators=100, random_state=42)` on the wine dataset. Print accuracy and the top 5 features by importance.

```python
random_forest_wine()
# Accuracy: ~0.97+
# Top 5 features: [(name, importance), ...]
```

### 3. Gradient Boosting
Train `GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42)` on wine. Compare accuracy with Random Forest.

```python
gradient_boosting_wine()
# GradientBoosting accuracy: ~0.95+
```

### 4. Feature Importance Comparison
On the wine dataset, extract `feature_importances_` from both RandomForest and GradientBoosting. Print side-by-side top 5 for each. Note the differences.

```python
compare_importances()
# RandomForest top 5:       [(feat, imp), ...]
# GradientBoosting top 5:   [(feat, imp), ...]
```
