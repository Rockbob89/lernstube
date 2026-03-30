# Task 7: Incremental Models & Snapshots

## Objective
Build incremental models that process only new/changed data, and snapshots that track historical changes (SCD Type 2).

## What to Learn
- Incremental materialization: only processes new/changed rows instead of rebuilding the whole table. Requires a filter to identify "new" rows.
  ```sql
  {{ config(materialized='incremental', unique_key='order_id') }}
  SELECT * FROM {{ source('raw', 'orders') }}
  {% if is_incremental() %}
    WHERE order_date > (SELECT MAX(order_date) FROM {{ this }})
  {% endif %}
  ```
- `is_incremental()` macro: returns `True` only when the target table already exists and `--full-refresh` was not passed. `{{ this }}` refers to the current model's table.
- Incremental strategies: `append` (just inserts), `merge` (upsert on `unique_key`), `delete+insert` (deletes matching rows then re-inserts — useful when `merge` isn't available).
- `unique_key` for deduplication: with `merge` strategy, dbt matches on this key and updates existing rows instead of duplicating them.
- `--full-refresh` flag: drops and rebuilds the table as if it were a `table` materialization. Use when schema changes.
- Snapshots: implement SCD Type 2 — track historical changes to a slowly-changing source table. dbt adds `dbt_valid_from`, `dbt_valid_to`, `dbt_scd_id`.
  ```sql
  -- snapshots/orders_snapshot.sql
  {% snapshot orders_snapshot %}
  {{ config(target_schema='snapshots', unique_key='order_id', strategy='check', check_cols=['status']) }}
  SELECT * FROM {{ ref('stg_orders') }}
  {% endsnapshot %}
  ```
- Snapshot meta columns: `dbt_valid_from` (when this version became active), `dbt_valid_to` (NULL = current row), `dbt_updated_at` (last seen timestamp).

## Exercises

1. **Incremental model**: Convert `stg_orders` (or create a new `fct_orders`) to an incremental model:
   - Use `order_date` to filter new records: `WHERE order_date > (SELECT max(order_date) FROM {{ this }})`
   - Set `unique_key = 'order_id'`
   - Run it twice: once to create, once to incrementally add new seed rows
   - Run with `--full-refresh` and explain what changed

2. **Snapshot**: Create `snapshots/orders_snapshot.sql`:
   - Snapshot `stg_orders` using `strategy='check'` and `check_cols=['status']`
   - Run `dbt snapshot`
   - Change an order's status in your seed data, re-seed, re-snapshot
   - Query the snapshot table and show that both the old and new versions exist with correct `dbt_valid_from` / `dbt_valid_to`
   - Note: `strategy='timestamp'` requires an `updated_at` column that changes on every row modification. Since seed data lacks a true `updated_at`, `check` strategy is the right fit here.

3. **Short answer** (2-3 sentences each):
   - What happens if your incremental model's `unique_key` has duplicates in the source?
   - When would you use `delete+insert` strategy instead of `merge`?
   - What is the risk of using `check` strategy for snapshots vs `timestamp`?

Write SQL files for exercises 1-2. Write short answers in `solution.md`.
