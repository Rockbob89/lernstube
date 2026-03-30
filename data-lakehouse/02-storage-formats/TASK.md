# Task 2: Storage Formats

## Objective
Understand the major storage formats used in data lakehouses, what problems each solves, and when to choose one over another.

## What to Learn
- Row-oriented vs columnar storage and why it matters for analytics: row stores read entire rows (good for OLTP); columnar stores read only queried columns (good for aggregations over large datasets).
- Parquet: columnar, compressed, predicate pushdown, schema in footer. Predicate pushdown means the engine skips row groups where min/max stats prove no rows match your `WHERE` clause.
- ORC: columnar alternative, Hive ecosystem, built-in indexes. Preferred in older Hive/Spark-on-HDFS stacks.
- Avro: row-based, schema evolution, serialization for streaming. Schema is embedded in each file as JSON; Kafka producers/consumers use Avro + Schema Registry.
- Delta Lake: Parquet + transaction log (`_delta_log/`), time travel, MERGE support. The log records every commit atomically; time travel queries a prior snapshot.
  ```python
  df.write.format("delta").save("/data/events")
  spark.read.format("delta").option("versionAsOf", 0).load("/data/events")
  ```
- Apache Iceberg: table format, hidden partitioning, schema evolution, catalog-level management. Hidden partitioning means you never write `WHERE year=2024` — Iceberg translates predicates automatically.
- Apache Hudi: upserts, incremental processing, Copy-on-Write vs Merge-on-Read. CoW rewrites full Parquet files on every upsert (fast reads); MoR appends deltas and merges at read time (fast writes).

## Exercises

1. **Format decision matrix**: Create a table mapping each format (Parquet, ORC, Avro, Delta Lake, Iceberg, Hudi) to: storage model (row/columnar), ACID support, schema evolution support, primary use case, ecosystem affinity.

2. **Code exercise**: Write a PySpark script that:
   - Creates a simple DataFrame (10+ rows, at least 3 columns including a timestamp)
   - Writes it in Parquet format
   - Writes it in Delta format
   - Reads both back and shows schemas
   - Demonstrates that Delta supports time travel by overwriting the Delta table and querying the previous version

3. **Short answer**: In 2-3 sentences each:
   - Why would you choose Iceberg over Delta Lake?
   - When is Avro a better choice than Parquet?
   - What does "hidden partitioning" in Iceberg mean and why does it matter?

Write conceptual answers in `solution.md`. Write code in `solution.py`.
