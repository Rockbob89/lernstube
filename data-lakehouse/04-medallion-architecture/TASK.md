# Task 4: Medallion Architecture

## Objective
Understand the Bronze/Silver/Gold layered data model, why it exists, and how to design data quality gates between layers.

## What to Learn
- Bronze layer: raw ingestion, append-only, schema-on-read, minimal transformation. Land data exactly as received — no filtering, no casting. Add only an ingestion timestamp.
  ```python
  raw_df.withColumn("_ingested_at", current_timestamp()) \
        .write.format("delta").mode("append").save("lakehouse/bronze/events")
  ```
- Silver layer: cleaned, deduplicated, conformed, business entities, schema-on-write. Apply type casting, null handling, deduplication, and join to reference data.
- Gold layer: aggregated, business-level, optimized for consumption (dashboards, ML features). Pre-aggregated tables keyed on the dimensions BI tools query most.
- Data quality enforcement at each transition: rows failing checks go to a quarantine table, not the next layer.
- Naming conventions and folder/table organization: e.g. `lakehouse/bronze/raw_orders/`, `lakehouse/silver/orders/`, `lakehouse/gold/daily_revenue/`
- How medallion maps to lakehouse storage (Delta tables, partitioned paths)

## Exercises

1. **Layer design**: You receive raw JSON events from an e-commerce platform with fields: `order_id, customer_id, product_ids (array), total_amount, currency, status, created_at, raw_payload`. Design the Bronze, Silver, and Gold tables:
   - Bronze: what do you store, what format, what partitioning?
   - Silver: what transformations happen? List the output columns and any cleaning rules.
   - Gold: design 2 aggregate tables that business analysts would query (e.g., daily revenue, customer lifetime value). Specify columns and grain.

2. **Quality gates**: For the Bronze-to-Silver transition above, define 5 concrete data quality checks you'd enforce (e.g., "reject rows where order_id is null"). For each, state: what happens to rows that fail (quarantine? drop? flag?).

3. **Code exercise**: Write a PySpark script that simulates a Bronze-to-Silver transformation:
   - Create a Bronze DataFrame with some intentionally dirty data (nulls, duplicates, invalid values)
   - Apply cleaning logic (dedup, null handling, type casting)
   - Write the Silver output as a Delta table
   - Write rejected rows to a quarantine table

Write conceptual answers in `solution.md`. Write code in `solution.py`.
