# Task 5: Macros & Jinja

## Objective
Write reusable SQL logic using Jinja templating and dbt macros. Understand packages.

## What to Learn
- Jinja basics in dbt: `{{ }}` renders a value, `{% %}` is a statement (no output), `{# #}` is a comment.
- Control flow:
  ```sql
  {% set statuses = ['pending', 'completed'] %}
  {% if var('filter_status', none) %}
  WHERE status = '{{ var("filter_status") }}'
  {% endif %}
  {% for s in statuses %} '{{ s }}'{% if not loop.last %},{% endif %}{% endfor %}
  ```
- Macros: reusable SQL snippets defined in `macros/*.sql`, callable from any model or other macro.
  ```sql
  -- macros/safe_divide.sql
  {% macro safe_divide(numerator, denominator) %}
    CASE WHEN {{ denominator }} = 0 THEN NULL ELSE {{ numerator }} / {{ denominator }} END
  {% endmacro %}

  -- usage in a model:
  SELECT {{ safe_divide('revenue', 'order_count') }} as avg_order_value FROM {{ ref('fct_orders') }}
  ```
- Calling macros: `{{ my_macro(arg) }}` — evaluated at compile time, not runtime.
- `dbt compile` writes rendered SQL to `target/compiled/` without executing. Use this to verify macro output.
- dbt packages: list in `packages.yml`, install with `dbt deps`. Package macros are called as `{{ package_name.macro_name() }}`.

## Exercises

1. **Jinja warm-up**: Create a model `models/staging/stg_orders_enriched.sql` that uses:
   - A `{% set %}` to define a list of valid statuses
   - A `{% if %}` to conditionally add a `WHERE` clause based on a dbt variable (`var('filter_status', none)`)
   - Run with and without: `dbt run --vars '{filter_status: completed}'`

2. **Custom macro**: Create `macros/cents_to_dollars.sql`:
   - A macro that takes a column name and returns `({{ column }} / 100.0)` (assume amounts are stored in cents)
   - Use it in a model: `{{ cents_to_dollars('amount') }} as amount_dollars`

3. **Generate macro**: Create `macros/generate_surrogate_key.sql`:
   - A macro that takes a list of column names and returns an MD5 hash of their concatenation
   - Use it in `stg_orders` to generate a surrogate key from `order_id` and `order_date`
   - Compare your implementation to `dbt_utils.generate_surrogate_key`

4. **Inspect compiled SQL**: Run `dbt compile` and examine the output in `target/compiled/`. Verify your macros expanded correctly.

Write your SQL and macro files as the solution.
