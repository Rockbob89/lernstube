# Task 03: TaskFlow API

## Objective
Use the TaskFlow API (@task decorator) for cleaner DAG definitions, understand XComs, and use dynamic task mapping.

## What to Learn
- The `@task` decorator and how it replaces PythonOperator boilerplate. Return values are automatically pushed as XComs; passing them as arguments pulls automatically.
  ```python
  from airflow.decorators import dag, task
  @dag(start_date=datetime(2026, 1, 1), schedule="@daily", catchup=False)
  def my_pipeline():
      @task
      def extract(): return {"rows": 42}
      @task
      def load(data): print(data["rows"])
      load(extract())
  my_pipeline()
  ```
- XComs: how data passes between tasks. Implicit: return value from `@task` is stored; argument injection pulls it. Explicit: `ti.xcom_push(key="k", value=v)` / `ti.xcom_pull(task_ids="t", key="k")`.
- XCom size limitations: XComs are stored in the metadata DB. Keep them under ~1 KB. For larger payloads, write to S3/GCS and pass only the path.
- `@task.branch` for branching logic: return the `task_id` (string) of the branch to execute; all other branches are skipped.
  ```python
  @task.branch
  def route(value): return "high_path" if value > 100 else "low_path"
  ```
- Dynamic task mapping with `.expand()`: generate N task instances at runtime from a list.
  ```python
  @task
  def process(filename): print(filename)
  process.expand(filename=["a.csv", "b.csv", "c.csv"])  # creates 3 task instances
  ```

## Exercises

1. **TaskFlow rewrite**: Rewrite the `etl_basic` DAG from Task 02 using the TaskFlow API. The `extract` task should return data that `transform` receives as input, and `transform` should return data that `load` receives.

2. **XCom inspection**: Write a DAG `xcom_demo` with two tasks:
   - `produce`: returns `{"items": ["a", "b", "c"], "count": 3}`
   - `consume`: receives the output of `produce` and prints each item
   - Use the TaskFlow API.

3. **Dynamic task mapping**: Write a DAG `dynamic_processing` where:
   - `get_files` returns a list of filenames: `["file1.csv", "file2.csv", "file3.csv"]`
   - `process_file` is dynamically mapped over the list, printing the filename it receives

```python
# Test: airflow dags test xcom_demo 2026-03-30
```
