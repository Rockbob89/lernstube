# Task 2: Project Setup & Models

## Objective
Initialize a dbt project, write models with different materializations, and understand the ref() dependency graph.

## What to Learn
- `dbt init` and project structure (`dbt_project.yml`, `models/`, `tests/`, `macros/`)
- `profiles.yml` and target configuration: maps a profile name to a warehouse connection. `dbt_project.yml` references the profile name; `profiles.yml` lives in `~/.dbt/` by default.
- Writing models as SELECT statements in `.sql` files. dbt wraps your SELECT in a `CREATE TABLE/VIEW AS` — you only write the query body.
- Materializations: `view` (default, recreated each run), `table` (dropped and rebuilt), `ephemeral` (inlined as CTE, not persisted), `incremental` (appends/merges new rows only).
- `ref()` for model-to-model dependencies: `{{ ref('stg_orders') }}` resolves to the correct schema+table name and tells dbt to run `stg_orders` first.
  ```sql
  SELECT c.name, o.amount FROM {{ ref('stg_customers') }} c
  JOIN {{ ref('stg_orders') }} o ON c.customer_id = o.customer_id
  ```
- Model configuration via `dbt_project.yml` (applies to whole folders) and in-file `{{ config() }}` (overrides for a single model):
  ```sql
  {{ config(materialized='table', schema='marts') }}
  SELECT ...
  ```
- `dbt run` executes all models; `dbt compile` renders Jinja to raw SQL without executing — useful for debugging.

## Exercises

1. **Project init**: Set up a dbt project using DuckDB as the adapter (lightweight, no external DB needed). Write the `profiles.yml` targeting a local DuckDB file.

2. **Staging models**: Create 2 staging models under `models/staging/`:
   - `stg_customers.sql` — SELECT from a raw customers source (you'll seed this in task 3, for now hardcode a CTE with 5 rows: `customer_id, name, email, signup_date`)
   - `stg_orders.sql` — SELECT from a raw orders source (hardcode a CTE with 10 rows: `order_id, customer_id, amount, order_date, status`)

3. **Mart model**: Create `models/marts/customer_orders.sql` that:
   - Uses `ref()` to join `stg_customers` and `stg_orders`
   - Aggregates: `customer_id, name, order_count, total_amount, first_order_date, last_order_date`
   - Configure it as a `table` materialization

4. **Run it**: Run `dbt run` and verify all models build. Paste the output.

Write your SQL files as the solution. Place them in the correct dbt project structure within this folder.
