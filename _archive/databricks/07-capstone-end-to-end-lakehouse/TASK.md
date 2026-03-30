# Task 7: Capstone — End-to-End Lakehouse

## Objective
Build a complete lakehouse pipeline on Databricks: ingest raw data, transform through medallion layers, train an ML model, and create a dashboard.

## Scenario
You are building a data platform for an online retailer. Data sources:
- **Orders**: `order_id, order_date, customer_id, product_id, quantity, unit_price, discount, status` (CSV from S3, daily batch)
- **Products**: `product_id, name, category, subcategory, brand, cost_price` (slowly changing dimension)
- **Customers**: `customer_id, name, email, signup_date, country, segment` (slowly changing dimension)
- **Clickstream**: `event_id, timestamp, session_id, customer_id, page, action, device_type` (streaming from Kafka)

Volume: 1M orders/day, 50M clickstream events/day.

## Deliverables

1. **Architecture document** (`architecture.md`): Diagram (text-based) showing:
   - Data sources -> Bronze -> Silver -> Gold layer flow
   - Which tools handle each step (Auto Loader, Delta Live Tables, SQL, MLflow)
   - Unity Catalog structure (catalog, schemas, tables)

2. **Bronze layer** (`bronze.py`): Ingestion code for:
   - Auto Loader for CSV orders from S3
   - Kafka structured streaming for clickstream
   - Raw Delta tables with metadata columns (_ingested_at, _source_file)

3. **Silver layer** (`silver.py`):
   - Clean and validate orders (handle nulls, type casting, dedup)
   - SCD Type 2 for customers and products
   - Sessionize clickstream data (group events into sessions with 30-min timeout)

4. **Gold layer** (`gold.sql`):
   - Daily revenue summary by category and region
   - Customer lifetime value (CLV) table
   - Product performance metrics (revenue, return rate, avg rating)
   - Funnel analysis from clickstream (page views -> add to cart -> purchase)

5. **ML pipeline** (`ml_pipeline.py`):
   - Train a churn prediction model using gold-layer features
   - Log with MLflow, register in Unity Catalog
   - Batch inference: score all customers, write predictions to a Delta table

6. **Workflow definition** (`workflow.json`):
   - Orchestrate: bronze -> silver -> gold -> ML inference
   - Schedule: daily at 02:00 UTC
   - Error handling: retries, notifications

## No solution stubs for this task. Build it from scratch.
