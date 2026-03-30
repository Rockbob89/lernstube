# Task 6: Pipelines

## Objective
Pipelines chain preprocessing and modeling into a single object. This prevents data leakage, simplifies code, and makes models deployable. The `Pipeline` is how production sklearn looks.

## What to Learn
- `Pipeline` — sequential chain of transforms + final estimator

```python
from sklearn.pipeline import Pipeline
pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", LogisticRegression()),
])
pipe.fit(X_train, y_train)   # fits scaler on X_train, transforms, then fits clf
pipe.predict(X_test)          # applies scaler.transform then clf.predict
```

- `make_pipeline` — shorthand constructor

```python
from sklearn.pipeline import make_pipeline
pipe = make_pipeline(StandardScaler(), LogisticRegression())
# step names are auto-generated from class names (lowercased)
```

- `FeatureUnion` — parallel feature extraction paths

```python
from sklearn.pipeline import FeatureUnion
# Concatenates outputs of multiple transformers column-wise
union = FeatureUnion([("pca", PCA(n_components=2)), ("svd", TruncatedSVD(n_components=2))])
```

- Accessing pipeline steps and their parameters

```python
pipe.named_steps["scaler"].mean_        # fitted attribute of the scaler step
pipe.get_params()                        # all params, prefixed by step name
pipe.set_params(clf__C=0.1)             # use the step name you gave it ("clf")
# make_pipeline auto-names by class: pipe.set_params(logisticregression__C=0.1)
```

- Why pipelines prevent data leakage (fit on train only, transform on both)

## Exercises

### 1. Basic Pipeline
Build a `Pipeline` with `StandardScaler` and `LogisticRegression`. Train on breast cancer dataset. Print accuracy.

```python
basic_pipeline()
# Accuracy: ~0.97+
```

### 2. Pipeline with ColumnTransformer
Create a mixed-type DataFrame (numeric + categorical). Build a pipeline that uses `ColumnTransformer` for preprocessing, then feeds into `RandomForestClassifier`. Print accuracy.

```python
mixed_pipeline()
# Accuracy printed
```

### 3. Named Steps Access
Build a pipeline. After fitting, access the scaler's `mean_` and the model's `coef_` through `named_steps`. Print them.

```python
access_pipeline_internals()
# Scaler mean: [...]
# Model coefficients shape: (...)
```

### 4. Pipeline Parameters
Print all parameters of a Pipeline using `get_params()`. Show how parameter names are prefixed with step names (e.g., `logisticregression__C`). Set `C=0.1` using `set_params()` and refit.

```python
pipeline_params()
# Lists all params with step prefixes
# Refits with C=0.1
```
