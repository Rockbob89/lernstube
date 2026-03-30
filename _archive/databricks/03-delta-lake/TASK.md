# Task 3: Delta Lake

## Objective
Understand Delta Lake as the storage layer for the Lakehouse. Learn ACID transactions, time travel, and table maintenance operations.

## What to Learn
- Delta Lake: open-source storage layer adding ACID to Parquet
- Transaction log (`_delta_log/`): how commits work, optimistic concurrency
  - Every write appends a JSON entry to `_delta_log/`. Concurrent writers use optimistic locking — if two writes conflict on the same file range, one retries. The log is the authoritative source; Parquet files are just data.
- Time travel: query previous versions, restore tables
  ```sql
  SELECT * FROM orders VERSION AS OF 5;
  SELECT * FROM orders TIMESTAMP AS OF '2024-03-01';
  ```
- MERGE (upsert): the key operation for CDC and slowly changing dimensions
  ```python
  from delta.tables import DeltaTable
  target = DeltaTable.forName(spark, "users")
  target.alias("t").merge(updates.alias("s"), "t.user_id = s.user_id") \
      .whenMatchedUpdateAll() \
      .whenNotMatchedInsertAll() \
      .execute()
  ```
- Table maintenance: OPTIMIZE (file compaction), VACUUM (cleanup old files), Z-ORDER (co-locate data)
  ```sql
  OPTIMIZE orders ZORDER BY (order_date, region);  -- compact + co-locate
  VACUUM orders RETAIN 168 HOURS;                  -- delete files older than 7 days
  ```
- Schema enforcement vs schema evolution
  - Enforcement (default): writing a column not in the schema raises an error.
  - Evolution: `spark.conf.set("spark.databricks.delta.schema.autoMerge.enabled", "true")` — new columns are added automatically.
- Change Data Feed (CDF): track row-level changes
  - Enable with `ALTER TABLE t SET TBLPROPERTIES ('delta.enableChangeDataFeed' = 'true')`, then read changes with `spark.read.format("delta").option("readChangeFeed", "true").option("startingVersion", 5).table("t")`.
- Liquid clustering (replacing partitioning + Z-ORDER)
  - `CREATE TABLE t (...) CLUSTER BY (region, order_date)` — Databricks automatically manages clustering as data grows, without fixed partition directories.

## Exercises

1. **MERGE operations**: Write PySpark code for these scenarios:
   - Upsert: incoming batch of user profiles — insert new users, update existing ones
   - SCD Type 2: track historical changes to user addresses (add effective_date, end_date, is_current)
   - Delete with audit: soft-delete users by marking them inactive, never physically deleting

2. **Time travel and recovery**: Write code to:
   - Query a Delta table as of 24 hours ago
   - Query a specific version number
   - Restore a table to a previous version after a bad write
   - Show the table's history

3. **Table maintenance**: Write a maintenance routine that:
   - Runs OPTIMIZE on a table with Z-ORDER on commonly filtered columns
   - Runs VACUUM with a 7-day retention
   - Checks table stats (file count, size) before and after
   - Explain when to use liquid clustering instead of partition + Z-ORDER
