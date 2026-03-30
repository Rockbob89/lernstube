"""
Task 02: Writing DAGs
Write your DAG definitions here.
Define DAGs as top-level objects (Airflow discovers them at module level).
"""
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator


# Exercise 1: Basic DAG — define 'etl_basic' DAG here


# Exercise 2: Parallel tasks — define 'parallel_checks' DAG here


# Exercise 3: Trigger rules — define 'parallel_checks_with_triggers' DAG here


if __name__ == "__main__":
    print("Import this file in your Airflow DAGs folder or run: airflow dags test <dag_id> 2026-03-30")
