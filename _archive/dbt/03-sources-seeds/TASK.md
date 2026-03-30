# Task 3: Sources & Seeds

## Objective
Replace hardcoded CTEs with proper dbt sources and seed files. Understand freshness checks.

## What to Learn
- Seeds: CSV files in `seeds/` loaded into the warehouse via `dbt seed`. Use for small, rarely-changing reference data (country codes, status mappings). Not for raw event data.
- Sources: declaring external tables in `schema.yml`, using `{{ source() }}`. This lets dbt know about tables it didn't create, enables lineage, and unlocks freshness checks.
  ```yaml
  # models/staging/schema.yml
  sources:
    - name: raw
      tables:
        - name: orders
  ```
  ```sql
  SELECT * FROM {{ source('raw', 'orders') }}
  ```
- Source freshness: declare `loaded_at_field` so dbt can check when data last arrived:
  ```yaml
  - name: orders
    loaded_at_field: order_date
    freshness:
      warn_after: {count: 24, period: hour}
      error_after: {count: 48, period: hour}
  ```
- `dbt seed` loads CSVs; `dbt source freshness` checks all sources with a `loaded_at_field` and reports age.
- When to use seeds vs sources (seeds = small reference data, sources = external tables loaded by another tool)

## Exercises

1. **Seed data**: Create seed CSV files under `seeds/`:
   - `raw_customers.csv` — 10 rows: `customer_id,name,email,signup_date`
   - `raw_orders.csv` — 20 rows: `order_id,customer_id,amount,order_date,status`
   - Use realistic-looking data. Include some edge cases (null emails, future dates, duplicate customer references).

2. **Source declaration**: Create `models/staging/schema.yml` that:
   - Declares the seed tables as sources (source name: `raw`)
   - Adds descriptions for each source table and column
   - Configures freshness on `raw_orders` using `order_date` as `loaded_at_field` with `warn_after: {count: 24, period: hour}`

3. **Refactor staging models**: Update `stg_customers.sql` and `stg_orders.sql` to use `{{ source('raw', 'raw_customers') }}` and `{{ source('raw', 'raw_orders') }}` instead of hardcoded CTEs.

4. **Run and verify**: Run `dbt seed && dbt run` and confirm everything builds.

Write your SQL and YAML files as the solution.
