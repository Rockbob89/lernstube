# Task 1: Data Lake vs Warehouse vs Lakehouse

## Objective
Understand the architectural differences, tradeoffs, and use cases for data lakes, data warehouses, and data lakehouses.

## What to Learn
- Data lake: schema-on-read, raw storage, object store backends (S3, GCS, ADLS). Files land as-is; schema is inferred at query time — so a corrupt CSV causes a runtime error, not an ingest error.
- Data warehouse: schema-on-write, columnar storage, query engines (BigQuery, Redshift, Snowflake). Schema is enforced on load; queries are fast but flexibility is limited.
- Data lakehouse: combining both — open formats (Parquet/ORC) on object storage with warehouse-grade query semantics and ACID transactions via a table format layer (Delta Lake, Iceberg).
- ACID transactions on lakes — why they matter: without them, a failed write leaves partial files; concurrent readers can see half-written data. Delta Lake solves this with a transaction log.
- Cost and performance tradeoffs across architectures
- When each architecture is the right choice (and when it's not)

## Exercises

1. **Comparison table**: Create a markdown table comparing data lake, warehouse, and lakehouse across these dimensions: schema enforcement, storage format, ACID support, typical cost model, query performance, data types supported, governance capabilities.

2. **Scenario analysis**: For each scenario below, state which architecture you'd recommend and why (2-3 sentences each):
   - A fintech startup needs real-time fraud detection on streaming transaction data plus monthly compliance reports.
   - A media company stores petabytes of video files and needs ML pipelines for content recommendation.
   - A retail chain needs a single source of truth for inventory, sales, and supply chain data with strict SLAs on dashboards.

3. **Anti-pattern identification**: List 3 common failure modes when teams try to use a data lake as a warehouse (the "data swamp" problem). For each, explain the root cause and what a lakehouse solves.

Write your answers in `solution.md` in this folder.
