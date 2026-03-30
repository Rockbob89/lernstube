# Task 5: SQL Warehouses

## Objective
Learn Databricks SQL for analytics workloads — SQL warehouses, dashboards, and query optimization.

## What to Learn
- SQL Warehouses: serverless vs classic, sizing (T-shirt sizes), auto-stop
  - Serverless: compute managed by Databricks, starts in seconds, billed per query second. Classic: you control the cluster nodes, billed while running regardless of query load.
- Databricks SQL vs Spark SQL: same engine, different interface
  - Same Spark/Photon execution engine; Databricks SQL adds a dedicated query editor, dashboards, and alerts layered on top of SQL Warehouses.
- Photon engine: vectorized query execution, when it helps
  - Photon processes data in columnar batches using SIMD CPU instructions rather than row-by-row. Biggest gains on scans, aggregations, and joins over Delta tables. No benefit for Python UDFs.
- Query optimization: predicate pushdown, partition pruning, file pruning with Z-ORDER
  - Predicate pushdown: filter applied at file read, before data reaches Spark. Partition pruning: skips entire partition directories. Z-ORDER file pruning: Delta's min/max stats per file let the engine skip files that can't contain matching values.
- Materialized views and streaming tables
  - Materialized view: `CREATE MATERIALIZED VIEW daily_revenue AS SELECT date, SUM(amount) FROM orders GROUP BY date` — result is pre-computed and refreshed on schedule.
  - Streaming table: continuously ingests from a stream source and writes incrementally to Delta.
- Dashboards: building, scheduling, alerts
- Query profiling: reading query plans, identifying bottlenecks
- Cost control: warehouse sizing, auto-stop, query queuing

## Exercises

1. **SQL analytics queries**: Write Databricks SQL for a `sales` table (order_id, order_date, customer_id, product_id, category, quantity, unit_price, discount, region):
   - Year-over-year revenue growth by region
   - Running total of daily revenue (window function)
   - Top 5 products by revenue in each category (QUALIFY with ROW_NUMBER)
   - Customer cohort analysis: revenue by signup month cohort over time
   - Moving 30-day average order value

2. **Query optimization**: Given a slow query that scans a 10TB `events` table filtered by `event_date` and `country`, write:
   - The slow version (full scan)
   - An optimized version using partitioning, Z-ORDER, or predicate pushdown
   - EXPLAIN output interpretation (describe what you'd look for)

3. **Warehouse sizing**: For each workload, recommend a warehouse size and type (serverless/classic) with justification:
   - Ad-hoc analyst queries (5 concurrent users, interactive)
   - Nightly dashboard refresh (20 dashboards, non-interactive)
   - Real-time operational dashboard (continuous, low-latency)
