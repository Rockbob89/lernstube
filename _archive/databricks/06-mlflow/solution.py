"""
Task 6: MLflow — Solutions

These stubs work locally with mlflow installed.
Databricks-specific features (Unity Catalog, serving) noted in comments.
"""

import mlflow
import mlflow.sklearn
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score


# --- Exercise 1: Experiment Tracking ---

def train_with_manual_logging(
    experiment_name: str,
    n_estimators: int = 100,
    max_depth: int = 10,
) -> str:
    """
    Exercise 1a: Train a model with manual MLflow logging.
    Log params, metrics, and the model artifact.
    Return the run_id.
    """
    # TODO: implement
    return ""


def train_with_autologging(experiment_name: str) -> str:
    """
    Exercise 1b: Train with MLflow autologging enabled.
    Return the run_id.
    """
    # TODO: implement
    return ""


def compare_runs(run_id_1: str, run_id_2: str) -> dict:
    """
    Exercise 1c: Compare two runs.
    Return a dict with metrics from both runs for comparison.
    """
    # TODO: implement
    return {
        "run_1_metrics": {},
        "run_2_metrics": {},
        "better_run": "",
    }


# --- Exercise 2: Model Registry ---

def register_best_model(run_id: str, model_name: str) -> str:
    """
    Exercise 2a: Register a model from a run.
    Return the model version.
    """
    # TODO: implement
    return ""


def transition_model_stage(model_name: str, version: str, stage: str) -> None:
    """
    Exercise 2b: Transition a model version to a new stage.
    Stages: "Staging", "Production", "Archived"
    """
    # TODO: implement
    pass


def load_production_model(model_name: str):
    """
    Exercise 2c: Load the production model and return it.
    Show both classic and Unity Catalog registry paths.
    """
    # TODO: implement
    return None


# --- Exercise 3: Batch Inference ---

def batch_inference(model_name: str, input_table: str, output_table: str) -> None:
    """
    Exercise 3: Load production model, apply to Spark DataFrame, write to Delta.

    - Use mlflow.pyfunc.spark_udf(spark, model_uri)
    - Apply UDF to input DataFrame
    - Write predictions to output_table as Delta
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print("=== Exercise 1: Experiment Tracking ===")
    run1 = train_with_manual_logging("test_experiment", n_estimators=50, max_depth=5)
    print("Manual logging run:", run1)
    run2 = train_with_manual_logging("test_experiment", n_estimators=200, max_depth=15)
    print("Manual logging run 2:", run2)
    run3 = train_with_autologging("test_experiment")
    print("Autologging run:", run3)

    print("\n=== Exercise 1c: Compare Runs ===")
    if run1 and run2:
        print(compare_runs(run1, run2))

    print("\n=== Exercise 2: Model Registry ===")
    print("register_best_model: implement and test")
    print("transition_model_stage: implement and test")
    print("load_production_model: implement and test")

    print("\n=== Exercise 3: Batch Inference ===")
    print("batch_inference: implement and test in Databricks notebook")
