# Task 9: Capstone -- ML Pipeline

## Objective
Build an end-to-end ML classification pipeline on a real-world dataset. Apply everything from tasks 1-8: preprocessing, model selection, evaluation, hyperparameter tuning, and model serialization.

## Requirements

Use the **Adult Income dataset** (`fetch_openml("adult", version=2)`), which predicts whether income exceeds $50K/year. It has mixed numeric/categorical features and missing values — a realistic scenario.

### Steps

1. **Load and explore**: Load the dataset. Print shape, dtypes, missing value counts, class distribution.

2. **Preprocessing pipeline**: Build a `ColumnTransformer` that:
   - Scales numeric columns with `StandardScaler`
   - Imputes missing numerics with median
   - One-hot encodes categorical columns
   - Imputes missing categoricals with most frequent

3. **Model comparison**: Wrap the preprocessor in a `Pipeline` with at least 3 different classifiers (e.g., LogisticRegression, RandomForest, GradientBoosting). Use 5-fold cross-validation. Print mean F1 score for each.

4. **Hyperparameter tuning**: Take the best model. Run `RandomizedSearchCV` with at least 3 hyperparameters. Print best params and best score.

5. **Final evaluation**: Train the tuned model on the full training set. Evaluate on the held-out test set. Print classification report, confusion matrix, and ROC AUC.

6. **Serialize**: Save the final trained pipeline to `model.joblib` using `joblib.dump()`. Reload it and verify predictions match.

## Deliverable
A single `solution.py` that runs all steps sequentially and prints results. The script should be runnable with `python solution.py`.

## Evaluation Criteria
- Pipeline prevents data leakage (no fit on test data)
- At least 3 models compared
- Hyperparameter tuning on best model
- F1 score on test set > 0.60
- Model serialized and verified
