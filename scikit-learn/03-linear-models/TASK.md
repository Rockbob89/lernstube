# Task 3: Linear Models

## Objective
Linear models are the baseline for everything. Learn linear and logistic regression, understand regularization (L1/L2), and know when a linear model is sufficient.

## What to Learn
- `LinearRegression` — ordinary least squares
- `LogisticRegression` — classification despite the name
- `Ridge` (L2) and `Lasso` (L1) — regularization to prevent overfitting

```python
# L2 (Ridge): shrinks all coefficients, none become exactly zero
# L1 (Lasso): drives some coefficients to exactly zero (feature selection)
from sklearn.linear_model import Ridge, Lasso
Ridge(alpha=1.0)   # alpha controls regularization strength; higher = more
Lasso(alpha=0.1)
```

- `coef_` and `intercept_` — interpreting fitted models
- When linear models are enough vs when they fail

## Exercises

### 1. Linear Regression
Load the diabetes dataset. Train `LinearRegression`. Print R² score on test set and the top 3 features by absolute coefficient value.

```python
linear_regression_diabetes()
# R²: ~0.45
# Top 3 features: [('s5', coef), ('bmi', coef), ('s4', coef)]
```

### 2. Logistic Regression
Load the breast cancer dataset. Train `LogisticRegression(max_iter=10000)`. Print accuracy and the number of positive vs negative coefficients.

```python
logistic_breast_cancer()
# Accuracy: ~0.95+
# Positive coefficients: N, Negative coefficients: M
```

### 3. Regularization Comparison
On the diabetes dataset, train `LinearRegression`, `Ridge(alpha=1.0)`, and `Lasso(alpha=0.1)`. Print R² for each and the number of zero coefficients in Lasso (feature selection effect).

```python
compare_regularization()
# LinearRegression R²: ~0.45
# Ridge R²:            ~0.43
# Lasso R²:            ~0.44
# Lasso zero coefficients: N out of 10
```

### 4. Alpha Sweep
Train `Lasso` with alphas `[0.001, 0.01, 0.1, 1.0, 10.0]` on diabetes. Print R² and number of zero coefficients for each. Observe the bias-variance tradeoff.

```python
alpha_sweep()
# alpha=0.001 -> R²=0.xx, zeros=N
# alpha=0.01  -> R²=0.xx, zeros=N
# ...
```
