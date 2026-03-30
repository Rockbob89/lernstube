# Task 7: Hyperparameter Tuning

## Objective
Model performance depends heavily on hyperparameters. Learn systematic search with `GridSearchCV` and `RandomizedSearchCV`. Understand the search space, scoring, and how to extract results.

## What to Learn
- `GridSearchCV` — exhaustive search over a parameter grid

```python
from sklearn.model_selection import GridSearchCV
gs = GridSearchCV(SVC(), param_grid={"C": [0.1, 1, 10], "kernel": ["linear", "rbf"]},
                  cv=5, scoring="accuracy")
gs.fit(X_train, y_train)
print(gs.best_params_, gs.best_score_)
```

- `RandomizedSearchCV` — sampled search, better for large spaces

```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint
rs = RandomizedSearchCV(RandomForestClassifier(), n_iter=20, cv=5,
    param_distributions={"n_estimators": randint(50, 300), "max_depth": [3, 5, 10, None]})
```

- `param_grid` / `param_distributions` — defining search spaces
- `best_params_`, `best_score_`, `cv_results_` — extracting results

```python
import pandas as pd
results = pd.DataFrame(gs.cv_results_)[["params", "mean_test_score", "rank_test_score"]]
```

- Tuning pipeline parameters (step__param syntax)

```python
# Use double underscore to address params inside pipeline steps
param_grid = {"svc__C": [0.1, 1, 10], "svc__kernel": ["linear", "rbf"]}
GridSearchCV(pipe, param_grid=param_grid)
```

## Exercises

### 1. Grid Search
Run `GridSearchCV` on `SVC` with the wine dataset. Search over `C=[0.1, 1, 10]` and `kernel=["linear", "rbf"]`. Print best params and best score.

```python
grid_search_svc()
# Best params: {'C': ..., 'kernel': '...'}
# Best score: 0.xx
```

### 2. Randomized Search
Run `RandomizedSearchCV` on `RandomForestClassifier` with wine. Search `n_estimators` from `randint(50, 300)` and `max_depth` from `[3, 5, 10, None]`. Use `n_iter=10`. Print best params and score.

```python
random_search_rf()
# Best params: {'max_depth': ..., 'n_estimators': ...}
# Best score: 0.xx
```

### 3. Tune a Pipeline
Build a Pipeline with `StandardScaler` + `SVC`. Use `GridSearchCV` to tune `svc__C` and `svc__kernel`. Print best params.

```python
tune_pipeline()
# Best params: {'svc__C': ..., 'svc__kernel': '...'}
```

### 4. Results Analysis
From a completed `GridSearchCV`, extract `cv_results_` and print a table of `params`, `mean_test_score`, and `rank_test_score` sorted by rank.

```python
analyze_results()
# Rank | Params                        | Mean Score
# 1    | {'C': 10, 'kernel': 'rbf'}    | 0.xx
# ...
```
