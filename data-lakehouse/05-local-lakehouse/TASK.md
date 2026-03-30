# Task 5: Hands-On: Local Lakehouse

## Objective
Build a working mini lakehouse locally using Delta Lake + PySpark. Ingest raw data through Bronze, Silver, and Gold layers.

## What to Learn
- Setting up PySpark with Delta Lake locally (`pip install delta-spark`). The Delta JAR is downloaded automatically when configured correctly.
- SparkSession configuration for Delta:
  ```python
  from delta import configure_spark_with_delta_pip
  builder = SparkSession.builder.config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
      .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
  spark = configure_spark_with_delta_pip(builder).getOrCreate()
  ```
- End-to-end pipeline: ingest raw CSV/JSON -> Bronze -> Silver -> Gold
- Delta table operations: MERGE (upsert), UPDATE, DELETE, time travel (`versionAsOf`, `timestampAsOf`)
  ```python
  # Time travel
  spark.read.format("delta").option("versionAsOf", 0).load("lakehouse/silver")
  ```
- Reading and inspecting Delta transaction logs: `_delta_log/` contains JSON files (one per commit) and periodic Parquet checkpoints. You can read them directly to see what changed and when.

## Exercises

1. **Environment setup**: Create a `requirements.txt` with the necessary dependencies. Write a `spark_session.py` helper that creates a SparkSession configured for Delta Lake.

2. **Pipeline**: Build an end-to-end pipeline in `pipeline.py` that:
   - Reads a raw CSV file (create sample data: 100+ rows of fictional sales transactions with columns: `txn_id, customer_id, product, quantity, unit_price, txn_date, store_id`)
   - Writes to Bronze layer as Delta (append-only, add ingestion timestamp)
   - Transforms to Silver (clean, deduplicate, add `total_amount = quantity * unit_price`, cast types)
   - Aggregates to Gold: `daily_sales_by_store` (store_id, txn_date, total_revenue, txn_count)
   - All layers stored under `./lakehouse/{bronze,silver,gold}/`

3. **Delta operations**: In a separate script `delta_ops.py`, demonstrate:
   - MERGE: upsert new/updated transactions into the Silver table
   - Time travel: query Silver as of version 0
   - VACUUM: explain in a comment what it does and why you'd set a retention period

Write all code files in this folder. Include a `sample_data.csv` with your test data.
