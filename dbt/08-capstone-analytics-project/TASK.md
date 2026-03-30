# Task 8: Capstone — Analytics Project

## Objective
Build a complete dbt project that transforms raw data into a star schema with tests, documentation, incremental models, and lineage.

## Scenario
You are building the analytics layer for an online bookstore. Raw data arrives as CSV feeds (you'll use seeds to simulate):

- `raw_books` — `book_id, title, author, genre, price_cents, published_date`
- `raw_customers` — `customer_id, name, email, country, signup_date`
- `raw_orders` — `order_id, customer_id, order_date, status, updated_at`
- `raw_order_items` — `order_item_id, order_id, book_id, quantity`

## Deliverables

1. **Seed data**: Create realistic CSV files (20+ rows each, edge cases included).

2. **Staging layer** (`models/staging/`):
   - One staging model per source table
   - Clean, rename, cast types
   - Use `{{ source() }}` for all references

3. **Marts layer** (`models/marts/`):
   - `dim_books` — book dimension with price in dollars
   - `dim_customers` — customer dimension
   - `fct_orders` — order fact table (incremental, joined with order_items, includes `total_items`, `total_amount`)
   - `agg_daily_sales` — daily sales aggregate (revenue, order count, unique customers)
   - `agg_author_performance` — author-level metrics (books sold, revenue, unique customers)

4. **Testing**: Schema tests on every model. At least 2 singular tests. Use `dbt-utils` for at least 1 test.

5. **Snapshots**: Snapshot `stg_orders` to track status changes over time.

6. **Macros**: Use at least 1 custom macro (e.g., `cents_to_dollars`).

7. **Documentation**: Full descriptions on all models and columns. At least 1 doc block. Generate docs.

8. **Validation**: `dbt build` should pass with 0 errors. Paste the output.

This is a full project — create all files in a proper dbt project structure within this folder. No solution stubs provided.
