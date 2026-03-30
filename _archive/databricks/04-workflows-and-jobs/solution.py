"""
Task 4: Workflows & Jobs — Solutions
"""

import json


def multi_task_workflow() -> dict:
    """
    Exercise 1: Define a multi-task Databricks job as a JSON-compatible dict.

    Tasks: ingest -> validate -> transform -> aggregate -> notify
    Include: dependencies, cluster config, retry policy, scheduling.
    """
    return {
        "name": "",
        "schedule": {},
        "tasks": [
            {
                "task_key": "ingest",
                "description": "",
                "notebook_task": {"notebook_path": ""},
                "new_cluster": {},
                "retry_policy": {},
                "depends_on": [],
            },
            {
                "task_key": "validate",
                "description": "",
                "notebook_task": {"notebook_path": ""},
                "depends_on": [],
            },
            {
                "task_key": "transform",
                "description": "",
                "notebook_task": {"notebook_path": ""},
                "depends_on": [],
            },
            {
                "task_key": "aggregate",
                "description": "",
                "notebook_task": {"notebook_path": ""},
                "depends_on": [],
            },
            {
                "task_key": "notify",
                "description": "",
                "notebook_task": {"notebook_path": ""},
                "depends_on": [],
                "condition_task": {},
            },
        ],
    }


# --- Exercise 2: Task Value Passing ---

def task_a_count_rows():
    """
    Notebook code for Task A.
    Count rows in a table, pass count to Task B via dbutils.jobs.taskValues.

    Note: dbutils is available in Databricks notebooks, not locally.
    """
    # TODO: implement
    pass


def task_b_validate_count():
    """
    Notebook code for Task B.
    Read row count from Task A, fail if < 1000.
    """
    # TODO: implement
    pass


def workflow_comparison() -> dict:
    """
    Exercise 3: Databricks Workflows vs Airflow comparison.

    Return a dict with comparison dimensions and a recommendation.
    """
    return {
        "managed_vs_selfhosted": "",
        "dag_complexity": "",
        "data_awareness": "",
        "cost": "",
        "recommendation": "",
    }


if __name__ == "__main__":
    print("=== Exercise 1: Multi-Task Workflow ===")
    print(json.dumps(multi_task_workflow(), indent=2))

    print("\n=== Exercise 3: Workflow Comparison ===")
    for k, v in workflow_comparison().items():
        print(f"  {k}: {v}")
