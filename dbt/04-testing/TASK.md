# Task 4: Testing

## Objective
Add schema tests, custom data tests, and understand dbt's testing philosophy.

## What to Learn
- Schema tests in YAML: declared under a model's `columns` block. dbt generates the test SQL automatically.
  ```yaml
  models:
    - name: stg_orders
      columns:
        - name: order_id
          tests: [unique, not_null]
        - name: status
          tests:
            - accepted_values:
                values: ['pending', 'completed', 'cancelled']
  ```
- Custom data tests (singular tests): SQL files in `tests/` that must return 0 rows to pass. Any returned row is a test failure.
  ```sql
  -- tests/assert_order_date_not_future.sql
  SELECT * FROM {{ ref('stg_orders') }} WHERE order_date > current_date
  ```
- `dbt test` runs all tests; `dbt test --select stg_orders` runs only tests for that model; `dbt build` runs models and tests together in DAG order.
- Test severity: `warn` logs a warning but doesn't fail the run; `error` (default) fails immediately.
  ```yaml
  tests:
    - not_null:
        severity: warn
  ```
- dbt-utils package and additional tests (e.g., `expression_is_true`, `recency`): install via `packages.yml` + `dbt deps`.
- Test-driven development with dbt: write tests before models, run them against an empty or partial table, then build the model until tests pass.

## Exercises

1. **Schema tests**: Add to your `schema.yml` files:
   - `stg_customers`: `customer_id` is unique and not_null, `email` is not_null
   - `stg_orders`: `order_id` is unique and not_null, `customer_id` has a relationship to `stg_customers`, `status` has accepted_values `['pending', 'completed', 'cancelled', 'refunded']`
   - `customer_orders`: `customer_id` is unique and not_null, `order_count` > 0

2. **Singular test**: Create `tests/assert_no_negative_amounts.sql` — a query that selects orders where `amount < 0`. If it returns rows, the test fails.

3. **Failing test**: Intentionally add a row to your seed data that violates one of your tests. Run `dbt build` and observe the failure. Fix the data and re-run.

4. **dbt-utils**: Add `dbt-utils` to `packages.yml`, run `dbt deps`, and add an `expression_is_true` test to verify `total_amount >= 0` on `customer_orders`.

Write your YAML and SQL test files as the solution.
