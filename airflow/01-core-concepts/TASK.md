# Task 01: Core Concepts

## Objective
Understand Airflow's execution model, architecture, and core abstractions before writing any code.

## What to Learn
- What a DAG is and how Airflow uses directed acyclic graphs to model workflows. A DAG is a Python file defining tasks and their dependencies. It is parsed by the scheduler on every heartbeat — keep it fast and side-effect free.
- Tasks vs operators vs task instances: an **Operator** is the template (e.g., `PythonOperator`); a **Task** is an instantiated operator in a DAG; a **Task Instance** is one execution of that task for a specific DAG run.
- The scheduler, executor, metadata database, and webserver — how they interact: the scheduler reads DAG files, creates DAG runs, and submits task instances to the executor. The executor (e.g., CeleryExecutor) places tasks on workers. All state is written to the metadata DB (Postgres/MySQL). The webserver reads from the same DB.
- Execution date vs logical date vs data interval: `execution_date` is the *start* of the data interval, not when the run actually executes. For a daily DAG scheduled `@daily`, a run triggered at 2026-03-31 00:00 has `data_interval_start=2026-03-30` and `data_interval_end=2026-03-31`.
- Catchup, backfill, and idempotency: with `catchup=True`, Airflow creates all missed runs since `start_date`. Idempotency means re-running a task produces the same result — essential for safe catchup.
- When Airflow is the right tool (orchestration) vs when it is not (data processing, streaming)

## Exercises

1. **Architecture diagram**: Draw (text or image) the Airflow architecture showing scheduler, webserver, executor, metadata DB, and workers. Label the communication paths.

2. **Concept mapping**: Given this scenario, identify the Airflow concepts:
   - "Every day at 06:00, pull data from an API, validate it, transform it, and load it into Postgres."
   - What is the DAG? What are the tasks? What operators would you use? What is the schedule? What is the execution date for a run triggered at 2026-03-31 06:00?

3. **When NOT to use Airflow**: List 3 use cases where Airflow is a poor fit and name a better tool for each.

4. **Terminology quiz**: Explain in your own words the difference between:
   - Operator vs Task vs Task Instance
   - `execution_date` vs `data_interval_start` vs `data_interval_end`
   - Catchup enabled vs disabled

Write your answers in `solution.md` in this folder.
