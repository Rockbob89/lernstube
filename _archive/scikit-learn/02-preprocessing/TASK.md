# Task 2: Preprocessing

## Objective
Raw data is never ready for models. Learn sklearn's preprocessing transformers: scaling, encoding categoricals, handling missing values, and composing them with `ColumnTransformer`.

## What to Learn
- `StandardScaler`, `MinMaxScaler` — when to use which
- `OneHotEncoder`, `OrdinalEncoder` — categorical handling
- `SimpleImputer` — filling missing values
- `ColumnTransformer` — applying different transforms to different columns

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

ct = ColumnTransformer([
    ("num", StandardScaler(), ["age", "income"]),   # (name, transformer, columns)
    ("cat", OneHotEncoder(), ["city"]),
])
X_out = ct.fit_transform(X_train)
```

- The `fit_transform()` shortcut and why you must `fit` on train only

```python
# CORRECT: fit on train, then transform both
scaler.fit(X_train)
X_train_s = scaler.transform(X_train)
X_test_s  = scaler.transform(X_test)   # uses train's mean/std — no leakage

# WRONG: fitting on test reveals test statistics to the model
scaler.fit_transform(X_test)
```

## Exercises

### 1. Scale Features
Load the wine dataset. Apply `StandardScaler` to all features. Print mean and std of the first feature before and after scaling.

```python
scale_wine()
# Before: mean=13.00, std=0.81
# After:  mean≈0.00, std≈1.00
```

### 2. Encode Categoricals
Given a DataFrame with a "color" column containing ["red", "green", "blue", "green", "red"], apply `OneHotEncoder(sparse_output=False)`. Print the encoded array and `categories_`.

```python
encode_colors()
# [[0. 0. 1.]
#  [0. 1. 0.]
#  [1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
# categories: [['blue', 'green', 'red']]
```

### 3. Impute Missing Values
Create a numpy array with some `np.nan` values. Use `SimpleImputer(strategy="median")` to fill them. Print before and after.

```python
impute_missing()
# Before: [1. nan 3. nan 5.]
# After:  [1. 3. 3. 3. 5.]
```

### 4. ColumnTransformer
Create a DataFrame with numeric columns ("age", "income") and a categorical column ("city"). Build a `ColumnTransformer` that scales numerics and one-hot encodes categoricals. Fit-transform and print the result shape.

```python
column_transform()
# Output shape: (n_samples, n_numeric + n_encoded_categories)
```
