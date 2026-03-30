# Task 06: Testing & Debugging

## Objective
Validate DAGs, test tasks in isolation, and debug common Airflow issues.

## What to Learn
- DAG validation: import errors crash the scheduler silently — always run `python dag_file.py` or `airflow dags list` to surface them. Cycle detection raises on DAG load.
- `dag.test()` for local testing without a running Airflow instance: runs all tasks in-process, in topological order, using a local executor. No webserver or metadata DB needed.
  ```python
  # at the bottom of your DAG file or a test script:
  if __name__ == "__main__":
      dag.test()
  ```
- `airflow tasks test <dag_id> <task_id> <execution_date>`: runs a single task in isolation, prints logs to stdout. Useful for debugging one task without running the full DAG.
- Writing pytest tests for DAGs: import the DAG object and assert on its structure.
  ```python
  from my_dag import dag
  def test_dag_loads(): assert dag.dag_id == "my_dag"
  def test_task_count(): assert len(dag.tasks) == 3
  ```
- Common pitfalls: top-level code (DB calls, file I/O) runs on every scheduler parse — move it inside callables. Large XComs bloat the metadata DB; write to object storage instead.
- Logging: use `self.log.info(...)` inside operators (not `print`). Log level is configurable per task. Logs are stored per task instance and surfaced in the UI.

## Exercises

1. **DAG validation test**: Write a pytest test file that:
   - Imports all DAG files from a directory
   - Asserts no import errors
   - Asserts no cycles
   - Asserts each DAG has at least one task

2. **Structure test**: Write a test for the `etl_basic` DAG that asserts:
   - It has exactly 3 tasks
   - Task ids are `extract`, `transform`, `load`
   - `load` has `transform` as upstream
   - `transform` has `extract` as upstream

3. **Debug exercise**: The following DAG has 4 bugs. Find and list them:
   ```python
   from airflow import DAG
   from airflow.operators.python import PythonOperator
   import pandas as pd  # heavy import at top level

   dag = DAG("buggy", schedule="@daily")

   def extract():
       return pd.DataFrame({"a": range(1_000_000)}).to_dict()  # huge XCom

   PythonOperator(task_id="extract", python_callable=extract, dag=dag)
   PythonOperator(task_id="load", python_callable=lambda: print("done"), dag=dag)
   ```

```python
# Run tests: pytest solution.py -v
```
