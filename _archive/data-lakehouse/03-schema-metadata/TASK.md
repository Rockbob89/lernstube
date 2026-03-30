# Task 3: Schema & Metadata

## Objective
Understand schema evolution, partitioning strategies, and metadata catalogs — the glue that makes a lakehouse queryable.

## What to Learn
- Schema evolution: adding/removing/renaming columns, type widening, backward/forward compatibility. In Delta Lake, adding a column requires `mergeSchema=true`; renaming is only supported in Iceberg natively.
  ```python
  df.write.option("mergeSchema", "true").format("delta").mode("append").save("/data/events")
  ```
- Partitioning: Hive-style partitioning stores data under `country=US/year=2024/` directories. Partition pruning means queries with `WHERE country='US'` skip all other directories entirely. Over-partitioning (e.g., by `user_id`) creates millions of tiny files — a classic performance killer.
- Z-ordering and data skipping: Z-ordering co-locates related values on disk so that a query on `(country, city)` skips most files. It complements partitioning but applies within a partition.
  ```sql
  OPTIMIZE events ZORDER BY (country, city)
  ```
- Metadata catalogs: Hive Metastore, AWS Glue Data Catalog, Unity Catalog. A catalog maps a table name to a storage location + schema, allowing multiple engines (Spark, Trino, Athena) to query the same table.
- What a catalog provides: table registration, schema management, access control, lineage

## Exercises

1. **Schema evolution scenarios**: For each scenario, state whether Delta Lake and Iceberg support it, and what command/config enables it:
   - Adding a new nullable column
   - Renaming a column
   - Widening INT to LONG
   - Dropping a column
   - Changing a column from required to optional

2. **Partitioning design**: Given a table `events(event_id, user_id, event_type, country, created_at)` with 500M rows/month:
   - Propose a partitioning strategy. Justify column choice and granularity.
   - Explain what happens if you partition by `user_id` (and why it's wrong).
   - Explain how Z-ordering could complement your partition strategy.

3. **Catalog comparison**: Write a brief comparison (bullet points) of Hive Metastore vs AWS Glue Data Catalog vs Databricks Unity Catalog. Cover: deployment model, multi-engine support, access control granularity, cost.

Write your answers in `solution.md`.
