# Task 1: What Druid Is

## Objective
Understand what Apache Druid is, where it fits in the data landscape, and when to pick it over alternatives.

## What to Learn
- OLAP databases vs OLTP databases — what problem space Druid targets
  - OLTP: many small reads/writes, row-oriented, e.g. `UPDATE orders SET status='shipped' WHERE id=42`
  - OLAP: few large aggregations over millions of rows, e.g. `SELECT city, SUM(revenue) FROM events GROUP BY city`
- Columnar storage: why it matters for analytical queries
  - Row store reads entire rows; columnar store reads only queried columns, enabling fast aggregations and high compression on a single column's repeated values
- Druid's sweet spot: sub-second queries on high-volume event data
- Comparison: Druid vs ClickHouse vs Elasticsearch vs traditional warehouses (BigQuery, Redshift)
- When Druid is the wrong choice (small datasets, complex joins, OLTP workloads)

## Exercises

1. **Classification exercise**: Given the following workloads, classify each as "Druid is a good fit" or "Druid is a bad fit" and explain why:
   - Real-time clickstream analytics dashboard with 1B events/day
   - E-commerce product catalog with full-text search
   - IoT sensor data with time-series aggregations, 500K events/sec ingest
   - Financial transaction ledger requiring ACID guarantees and complex joins
   - Log aggregation with free-text search and alerting
   - Ad-tech bid analytics with sub-second p99 query latency requirement

2. **Comparison table**: Build a comparison matrix (in a markdown file or code comments) covering Druid, ClickHouse, Elasticsearch, and BigQuery across these dimensions:
   - Query latency profile
   - Ingest model (batch/stream/both)
   - Join support
   - Storage model (columnar/row/inverted index)
   - Typical use case
   - Operational complexity (self-hosted)

3. **Write a short decision document** (5-10 sentences in `solution.py` as a docstring): Your team runs a Kubernetes-based platform and needs to add a real-time analytics layer for 200M events/day. The PM wants sub-second dashboard queries. Compare Druid vs ClickHouse for this scenario and make a recommendation with trade-offs.
