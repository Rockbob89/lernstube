# Task 07: Capstone — Streaming Pipeline

## Objective
Build a real-time event processing pipeline: ingest from Kafka, window-aggregate, enrich, and write to sink with exactly-once guarantees.

## Requirements

Build a Flink pipeline for real-time user activity analytics:

1. **Source**: Read user events from Kafka topic `user_events`:
   - Schema: `{"user_id": str, "event_type": str, "page": str, "timestamp": int}`
   - Use event time with 10-second bounded out-of-orderness

2. **Sessionization**: Apply session windows (30-second gap) per user to group activity into sessions.

3. **Aggregation**: Per session, compute:
   - `session_duration_seconds`
   - `page_count` (distinct pages visited)
   - `event_count`
   - `first_event` and `last_event` timestamps

4. **Enrichment**: Join session data with a user dimension table (can be an in-memory lookup or JDBC table) to add `user_name` and `user_tier`.

5. **Sink**: Write enriched session summaries to:
   - Kafka topic `session_summaries` (JSON)
   - Optionally also to a JDBC table

6. **Fault tolerance**:
   - Exactly-once checkpointing every 30 seconds
   - RocksDB state backend

## Deliverables
- `solution.py`: The complete pipeline code
- `docker-compose.yml`: Kafka + Flink cluster (or Kafka + PyFlink local)
- `produce_events.py`: A script that generates test events to Kafka
- Brief writeup in comments: what guarantees does this pipeline provide? What happens on failure/restart?

## Constraints
- Use PyFlink (Table API or DataStream API or both)
- Pipeline must handle late data
- Pipeline must be restartable from a savepoint without data loss
