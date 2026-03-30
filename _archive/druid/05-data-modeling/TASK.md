# Task 5: Data Modeling

## Objective
Learn to design Druid schemas — choosing dimensions, metrics, rollup strategy, and segment granularity for real-world use cases.

## What to Learn
- Dimensions vs metrics: queryable attributes vs aggregatable values
  - Dimensions: `country`, `device_type`, `status_code` — used in `WHERE`, `GROUP BY`
  - Metrics: `response_time_ms`, `revenue`, `byte_count` — used in `SUM()`, `AVG()`, `COUNT()`
  - A field cannot be both; choose based on how it will be queried.
- Rollup: pre-aggregation trade-offs (storage savings vs query flexibility)
- Segment granularity: how it affects query performance and segment count
  - `DAY` granularity = one segment file per day. Finer granularity means more files (more overhead for wide scans); coarser means larger files (more data scanned for narrow time filters).
- Multi-value dimensions
  - A single row can hold multiple values for one dimension: `tags: ["sports", "news", "tech"]`. Druid stores and filters these natively — no array unnesting needed at query time.
- Schema evolution: adding/removing columns, backfilling
  - Adding a dimension: reindex existing segments or accept `null` for historical data. Druid does not alter segments in place.
- Denormalization: why Druid prefers flat, wide tables (no joins)
  - Druid has limited join support and no referential integrity. Enrich events at ingest time (e.g., join product category from a lookup) so queries touch only one datasource.
- Common anti-patterns: too many dimensions, wrong granularity, missing rollup

## Exercises

1. **Schema design**: An e-commerce platform sends order events with these fields:
   `order_id, timestamp, user_id, product_id, product_category, quantity, price, discount, payment_method, shipping_country, device_type, referrer_url`

   Design a Druid schema. Decide:
   - Which fields are dimensions, which are metrics
   - Whether to enable rollup (and at what query granularity)
   - Segment granularity
   - Which fields to drop or transform
   Justify each decision.

2. **Schema comparison**: Design two schemas for the same order data:
   - Schema A: Optimized for "total revenue by country and category" dashboards
   - Schema B: Optimized for "per-order drill-down and fraud detection"
   Explain why they differ.

3. **Cardinality analysis**: The `referrer_url` field has 2M unique values. Explain the impact on Druid performance and propose two approaches to handle it.
