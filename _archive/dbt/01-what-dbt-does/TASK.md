# Task 1: What dbt Does

## Objective
Understand where dbt fits in the modern data stack, what it does (and doesn't do), and how it differs from traditional ETL.

## What to Learn
- ELT vs ETL: why the shift happened, role of cloud warehouses. Cloud warehouses are cheap and powerful enough to do transformation in-place — no need to transform before loading.
- dbt as the "T" in ELT — transforms data already loaded into a warehouse. dbt reads from tables/views in your warehouse and writes back to it.
- dbt Core vs dbt Cloud: Core is the open-source CLI; Cloud adds a scheduler, IDE, and observability layer.
- What dbt is NOT: it doesn't extract, doesn't load, doesn't orchestrate (by itself). Airbyte/Fivetran loads; Airflow orchestrates; dbt transforms.
- How dbt compiles Jinja+SQL into raw SQL and runs it against your warehouse:
  ```sql
  -- models/staging/stg_orders.sql
  SELECT order_id, amount FROM {{ source('raw', 'orders') }} WHERE status != 'cancelled'
  -- dbt compile turns {{ source(...) }} into the actual schema-qualified table name
  ```
- The dbt project structure: models, tests, sources, macros, seeds
- Supported adapters: Postgres, BigQuery, Snowflake, Redshift, DuckDB, etc. The adapter translates dbt's SQL dialect to the target warehouse.

## Exercises

1. **Positioning diagram**: Draw (ASCII/text) a diagram showing a typical modern data stack. Label where each tool sits: extraction (Fivetran/Airbyte), loading, transformation (dbt), warehouse, BI (Looker/Metabase). Show the data flow direction.

2. **Comparison table**: Create a table comparing ETL vs ELT across: where transformation happens, compute used, schema flexibility, example tools, typical latency.

3. **Short answer** (2-3 sentences each):
   - Why does dbt use SQL instead of Python for transformations?
   - What problem does the `ref()` function solve?
   - When would you NOT use dbt? Name 2 scenarios.
   - What is a materialization in dbt terms?

Write your answers in `solution.md`.
