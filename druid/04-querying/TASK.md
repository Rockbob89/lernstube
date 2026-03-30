# Task 4: Querying

## Objective
Learn to query Druid using both native JSON queries and Druid SQL. Understand aggregations, filters, and performance characteristics.

## What to Learn
- Druid SQL: the SQL layer over native queries — what it supports and what it doesn't
- Native query types: `timeseries`, `topN`, `groupBy`, `scan`
- When to use which: timeseries (no grouping), topN (single dimension, top-K), groupBy (multi-dimension), scan (raw rows)
  ```json
  { "queryType": "timeseries", "dataSource": "web_logs",
    "granularity": "hour", "intervals": ["2024-01-01/2024-01-08"],
    "aggregations": [{"type": "count", "name": "requests"}] }
  ```
- Aggregators: `count`, `longSum`, `doubleSum`, `hyperUnique`, `thetaSketch`, `quantilesDoublesSketch` (DataSketches for approximate quantiles — `APPROX_QUANTILE_DS` in SQL)
  - `hyperUnique` and `thetaSketch` give approximate distinct counts with a fraction of the memory of exact `COUNT(DISTINCT ...)`.
  - In SQL: `SELECT APPROX_COUNT_DISTINCT_DS_THETA(user_id) FROM web_logs WHERE ...`
- Post-aggregators: computed columns from aggregation results
  ```json
  { "type": "arithmetic", "name": "error_rate", "fn": "/",
    "fields": [{"type": "fieldAccess", "fieldName": "errors"},
               {"type": "fieldAccess", "fieldName": "requests"}] }
  ```
- Filters: selector, bound, in, regex, interval
  - `{"type": "selector", "dimension": "status_code", "value": "500"}` — exact match
  - `{"type": "bound", "dimension": "response_time_ms", "lower": "1000", "lowerStrict": true}` — range
- Query context parameters: `timeout`, `priority`, `useCache`
  - `{"timeout": 5000, "priority": 0, "useCache": true}` — passed as the `context` key in the query JSON
- Druid SQL limitations vs native queries

## Exercises

1. **Write Druid SQL queries** for the web access log datasource:
   - Count of requests per HTTP method in the last 24 hours
   - Top 10 paths by average response time
   - p95 response time per status code (use APPROX_QUANTILE_DS)
   - Request count per minute with a filter on status_code >= 500

2. **Write equivalent native queries** (as Python dicts) for:
   - A timeseries query: total request count and avg response time, HOUR granularity, last 7 days
   - A topN query: top 5 client IPs by request count
   - A groupBy query: request count grouped by method and status_code

3. **Query optimization**: Given a slow groupBy query that groups by `path` (high cardinality, 500K unique values) with a 30-second timeout, list three strategies to make it faster.
