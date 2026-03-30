# Task 3: Ingestion

## Objective
Understand how data gets into Druid — batch and streaming ingestion, ingestion specs, and Kafka integration.

## What to Learn
- Batch ingestion: native batch (parallel) vs Hadoop-based (legacy)
- Streaming ingestion: Kafka indexing service — the primary real-time path
- Ingestion spec structure: `dataSchema`, `ioConfig`, `tuningConfig`
  ```json
  {
    "dataSchema": { "dataSource": "my_ds", "timestampSpec": {}, "dimensionsSpec": {}, "metricsSpec": [], "granularitySpec": {} },
    "ioConfig":   { "type": "kafka", "consumerProperties": {}, "topic": "my_topic" },
    "tuningConfig": { "type": "kafka", "maxRowsInMemory": 100000 }
  }
  ```
- `dataSchema` details: datasource name, `timestampSpec`, `dimensionsSpec`, `metricsSpec`, `granularitySpec`
  - `timestampSpec`: `{"column": "ts", "format": "iso"}` — tells Druid which field is the event time
  - `dimensionsSpec`: `{"dimensions": ["method", "path", "status_code"]}` — queryable string/numeric attributes
  - `metricsSpec`: `[{"type": "longSum", "name": "request_count", "fieldName": "count"}]` — pre-aggregated at ingest
  - `granularitySpec`: `{"segmentGranularity": "HOUR", "queryGranularity": "MINUTE"}` — segment file size and rollup resolution
- Rollup: pre-aggregation at ingestion time — what it buys you and what it costs
  - With rollup, rows sharing the same timestamp bucket + dimensions are collapsed into one row with summed metrics. Saves storage and speeds aggregation queries; you lose the ability to retrieve individual raw events.
- Segment granularity vs query granularity
  - Segment granularity controls how many rows go into one file (e.g., `HOUR` = one file per hour). Query granularity controls the finest time bucket rollup collapses to (e.g., `MINUTE` = events within the same minute are merged).
- Common pitfalls: timestamp parsing, dimension/metric confusion, oversized segments

## Exercises

1. **Write a batch ingestion spec** (as a Python dict/JSON): Ingest a CSV file of web server access logs with fields: `timestamp`, `method`, `path`, `status_code`, `response_time_ms`, `user_agent`, `client_ip`. Choose appropriate dimensions vs metrics. Apply HOUR segment granularity.

2. **Write a Kafka ingestion spec**: Same data schema but ingesting from a Kafka topic `web-access-logs`. Configure consumer properties for a local Kafka broker.

3. **Rollup analysis**: Given the access log schema, design two versions — one with rollup enabled (choose a query granularity and aggregations) and one without. Explain the trade-off in comments.
