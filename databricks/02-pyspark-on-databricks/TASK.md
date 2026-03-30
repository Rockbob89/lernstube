# Task 2: PySpark on Databricks

## Objective
Write PySpark code for data transformations on Databricks. Understand DataFrames, transformations vs actions, and how to use the Spark UI.

## What to Learn
- SparkSession on Databricks (auto-configured, no boilerplate)
  - In a Databricks notebook `spark` is already available. No `SparkSession.builder...getOrCreate()` needed.
- DataFrames: creation, schema, column types
  ```python
  df = spark.read.parquet("dbfs:/data/events/")
  df.printSchema()  # inspect inferred types
  ```
- Transformations (lazy): `select`, `filter`, `withColumn`, `groupBy`, `join`, `agg`, `window`
  - Nothing executes until an action is called. Spark builds a logical plan and optimises it at action time.
  ```python
  from pyspark.sql import functions as F
  result = (df.filter(F.col("status") == 200)
              .withColumn("duration_s", F.col("duration_ms") / 1000)
              .groupBy("country").agg(F.avg("duration_s").alias("avg_dur")))
  ```
- Actions (trigger execution): `show`, `count`, `collect`, `write`
  - `result.show(10)` triggers the full plan above. `collect()` pulls all rows to the driver — avoid on large data.
- UDFs: when to use them (rarely) and why they're slow
  - UDFs bypass Catalyst optimiser and Photon; each row crosses the Python/JVM boundary. Prefer built-in `F.*` functions. Use UDFs only for logic that has no native equivalent.
- Spark UI: stages, tasks, shuffle, spill — reading execution plans
- Common performance issues: skew, small files, unnecessary shuffles, cartesian joins

## Exercises

1. **Transformation pipeline**: Given a DataFrame of taxi rides with columns `pickup_time, dropoff_time, pickup_zone, dropoff_zone, fare, tip, total, passenger_count`:
   - Add a `duration_min` column (dropoff - pickup in minutes)
   - Filter rides longer than 2 minutes and shorter than 120 minutes
   - Add a `tip_pct` column (tip / fare * 100, handle division by zero)
   - Group by `pickup_zone` and compute: avg fare, avg duration, total rides, avg tip_pct
   - Sort by total rides descending

2. **Window functions**: Using the same data:
   - Rank zones by total revenue (fare + tip) per hour
   - Compute a 7-day rolling average of daily ride count
   - Find the busiest hour for each zone

3. **Join and performance**: You have a `zones` DataFrame with `zone_id, borough, zone_name`. Join it to the rides data on pickup_zone. Write the join two ways — one that will cause a broadcast join and one that won't. Explain when each is appropriate.
