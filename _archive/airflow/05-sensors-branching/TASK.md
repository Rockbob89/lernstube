# Task 05: Sensors & Branching

## Objective
Use sensors to wait for conditions and branching operators to build conditional workflows.

## What to Learn
- Sensor base class: `poke_interval` (how often to check), `timeout` (fail after N seconds), `mode` (`poke` holds a worker slot; `reschedule` releases it between checks).
  ```python
  from airflow.sensors.filesystem import FileSensor
  wait = FileSensor(task_id="wait_for_file", filepath="/tmp/ready.txt",
                    poke_interval=30, timeout=300, mode="reschedule")
  ```
- `FileSensor`, `ExternalTaskSensor`, `HttpSensor`: all follow the same pattern — override `poke()` to return True when the condition is met.
- Poke mode vs reschedule mode: poke holds a worker slot for the full wait duration. With many concurrent sensors, this starves the pool. Reschedule releases the slot and reschedules the task — use it for long waits.
- `BranchPythonOperator` and `@task.branch`: return the `task_id` of the next task to execute. All other branches get the `skipped` state.
- Skipped task states and how they propagate: a skipped task propagates `skipped` downstream unless the downstream task uses `trigger_rule="none_failed"` or `"all_done"`.
- `ShortCircuitOperator` for conditional pipeline termination: if the callable returns `False`, all downstream tasks are skipped. Simpler than branching when there's no alternate path.
  ```python
  from airflow.operators.python import ShortCircuitOperator
  guard = ShortCircuitOperator(task_id="check", python_callable=lambda: Path("/data").exists())
  ```

## Exercises

1. **File sensor**: Write a DAG `file_watcher` that:
   - Waits for `/tmp/airflow_trigger.txt` to appear (use `FileSensor`, reschedule mode, 30s poke, 5min timeout)
   - Then runs a `process` task that prints "File found, processing..."
   - Then runs a `cleanup` task

2. **Branching**: Write a DAG `branch_demo` that:
   - Has a `check_day` task using `@task.branch` that returns `"weekday_task"` on weekdays and `"weekend_task"` on weekends
   - Has `weekday_task` and `weekend_task` PythonOperators
   - Has a `report` task that runs regardless of which branch was taken (think about what trigger rule you need)

3. **Short circuit**: Write a DAG `short_circuit_demo` where:
   - `check_data_exists` returns True/False
   - If False, the rest of the pipeline is skipped
   - Pipeline: check_data_exists >> transform >> load >> notify

```python
# Test: airflow dags test branch_demo 2026-03-30
```
