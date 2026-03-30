# Task 6: MLflow

## Objective
Learn MLflow on Databricks for experiment tracking, model registry, and model serving.

## What to Learn
- MLflow components: Tracking, Models, Registry, Serving
- Experiment tracking: logging parameters, metrics, artifacts
  ```python
  with mlflow.start_run():
      mlflow.log_param("n_estimators", 100)
      mlflow.log_metric("accuracy", 0.92)
      mlflow.log_artifact("confusion_matrix.png")
  ```
- Autologging: automatic tracking for sklearn, PyTorch, etc.
  - `mlflow.sklearn.autolog()` before `model.fit(...)` automatically logs estimator params, CV metrics, and the fitted model — no manual `log_param` calls needed.
- Model Registry: staging, production, archived model versions
  ```python
  mlflow.register_model("runs:/<run_id>/model", "my_model")
  client = mlflow.tracking.MlflowClient()
  client.transition_model_version_stage("my_model", version=1, stage="Production")
  ```
- Unity Catalog integration for model governance
  - Set the registry URI to Unity Catalog: `mlflow.set_registry_uri("databricks-uc")`. Model path becomes `models:/catalog.schema.model_name/version` instead of the legacy `models:/model_name/Production`.
- Model serving: real-time endpoints, batch inference
  ```python
  # Batch inference with Spark
  predict_udf = mlflow.pyfunc.spark_udf(spark, "models:/prod.ml.churn/1")
  df.withColumn("prediction", predict_udf(*feature_cols)).write.format("delta").save(...)
  ```
- MLflow vs standalone experiment tracking (W&B, Neptune)
- Feature Store basics (Databricks Feature Engineering)

## Exercises

1. **Experiment tracking**: Write code that:
   - Creates an MLflow experiment
   - Trains a simple sklearn model (e.g., RandomForest on a classification task)
   - Logs: parameters (hyperparameters), metrics (accuracy, f1, AUC), artifacts (confusion matrix plot)
   - Uses autologging as an alternative — show both approaches
   - Compares two runs with different hyperparameters

2. **Model Registry**: Write code that:
   - Registers the best model from exercise 1
   - Transitions it through stages: None -> Staging -> Production
   - Loads the production model and runs inference
   - Uses Unity Catalog model registry path (`models:/catalog.schema.model_name/version`)

3. **Batch inference pipeline**: Write a function that:
   - Loads the production model from the registry
   - Applies it to a Spark DataFrame using `mlflow.pyfunc.spark_udf`
   - Writes predictions to a Delta table
