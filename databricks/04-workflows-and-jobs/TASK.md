# Task 4: Workflows & Jobs

## Objective
Learn to orchestrate multi-step data pipelines using Databricks Workflows, including scheduling, parameters, and error handling.

## What to Learn
- Databricks Jobs: single-task vs multi-task workflows
- Task types: notebook, Python script, SQL, dbt, JAR
- Task dependencies: linear, fan-out, fan-in
  - Defined in the job JSON via `depends_on: [{task_key: "ingest"}]`. Fan-out = one task feeds multiple; fan-in = multiple tasks must complete before one runs.
- Job parameters and task values (passing data between tasks)
  ```python
  # Task A — write a value
  dbutils.jobs.taskValues.set(key="row_count", value=df.count())
  # Task B — read it
  count = dbutils.jobs.taskValues.get(taskKey="task_a", key="row_count")
  ```
- Scheduling: cron expressions, continuous jobs
  - Cron format: `"0 2 * * *"` = daily at 02:00 UTC. Continuous jobs restart immediately after each run completes — used for near-real-time polling.
- Cluster policies: job clusters vs shared clusters for tasks
- Error handling: retries, timeouts, conditional tasks
  - Per-task retry: `"max_retries": 3, "retry_on_timeout": true`. Conditional tasks use `"run_if": "ALL_SUCCESS"` or `"AT_LEAST_ONE_FAILED"`.
- Monitoring: job runs, alerts, email notifications
- Databricks Workflows vs Airflow/Prefect: when to use which

## Exercises

1. **Design a multi-task workflow** (as a JSON job definition): An ETL pipeline with these steps:
   - `ingest`: reads from S3, writes raw to Delta (bronze)
   - `validate`: data quality checks on bronze table (null checks, range checks)
   - `transform`: cleans and enriches data, writes to silver table
   - `aggregate`: builds summary tables (gold)
   - `notify`: sends success/failure notification

   Define task dependencies, cluster config, and error handling (retry ingest 3x, skip notify on success if all tasks pass).

2. **Task value passing**: Write the Python code for two notebook tasks:
   - Task A: counts rows in a table, passes the count to Task B via `dbutils.jobs.taskValues`
   - Task B: reads the count from Task A, fails if count < 1000

3. **Workflow comparison**: Compare Databricks Workflows vs Apache Airflow for orchestrating the ETL pipeline above. When would you choose each? Consider: managed vs self-hosted, DAG complexity, data-awareness, cost.
