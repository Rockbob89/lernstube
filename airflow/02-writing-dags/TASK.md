# Task 02: Writing DAGs

## Objective
Write functional DAGs using PythonOperator and BashOperator with proper dependencies and trigger rules.

## What to Learn
- DAG definition file structure and the DAG context manager:
  ```python
  from airflow import DAG
  from datetime import datetime
  with DAG("my_dag", start_date=datetime(2026, 1, 1), schedule="@daily", catchup=False) as dag:
      ...
  ```
- PythonOperator: `python_callable`, `op_args`, `op_kwargs`. The callable runs inside the worker process.
  ```python
  from airflow.operators.python import PythonOperator
  t = PythonOperator(task_id="greet", python_callable=lambda name: print(f"Hello {name}"), op_kwargs={"name": "World"})
  ```
- BashOperator: `bash_command`, templating. Jinja templates in `bash_command` are rendered at runtime with context variables like `{{ ds }}` (execution date string).
- Setting task dependencies with `>>` (downstream) and `<<` (upstream):
  ```python
  extract >> transform >> load
  start >> [check_a, check_b] >> merge  # fan-out / fan-in
  ```
- Trigger rules: `all_success` (default), `one_failed` (run if any upstream failed), `all_done` (run regardless of upstream status), `none_failed` (run if no failures, skips OK).
- `default_args` and DAG-level parameters: `default_args` applies to every task (e.g., `retries`, `retry_delay`); DAG-level params set `schedule`, `start_date`, `catchup`, `tags`.

## Exercises

1. **Basic DAG**: Write a DAG `etl_basic` scheduled daily that has three tasks:
   - `extract`: PythonOperator that returns a dict `{"rows": 42, "source": "api"}`
   - `transform`: BashOperator that echoes "Transforming data..."
   - `load`: PythonOperator that prints "Loading complete"
   - Dependencies: extract >> transform >> load

2. **Parallel tasks**: Write a DAG `parallel_checks` where:
   - `start` >> [`check_a`, `check_b`, `check_c`] >> `merge` >> `end`
   - Each check is a PythonOperator that prints its name

3. **Trigger rules**: Extend the parallel DAG so that `merge` runs even if one check fails (use the appropriate trigger rule). Add a `notify_failure` task that only runs if any upstream task failed.

```python
# Example call to test DAG loading:
# python solution.py
# Or: airflow dags test etl_basic 2026-03-30
```
