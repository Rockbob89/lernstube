# Task 06: Connectors

## Objective
Connect Flink to external systems: Kafka, JDBC databases, and filesystems.

## What to Learn
- Kafka source and sink connectors: defined via DDL in the Table API. The connector JAR must be on the classpath (added via `t_env.get_config().set("pipeline.jars", "file:///path/to/flink-sql-connector-kafka.jar")`).
  ```sql
  CREATE TABLE kafka_source (
    event_id STRING, user_id STRING, ts TIMESTAMP(3),
    WATERMARK FOR ts AS ts - INTERVAL '5' SECOND
  ) WITH (
    'connector' = 'kafka', 'topic' = 'events',
    'properties.bootstrap.servers' = 'localhost:9092',
    'properties.group.id' = 'flink-consumer',
    'format' = 'json'
  );
  ```
- JDBC connector: reads/writes relational tables. Requires the JDBC driver JAR and the Flink JDBC connector JAR. Not suitable for high-throughput streaming sinks — batch intervals apply.
- FileSystem connector: reads bounded datasets from a directory; writes using rolling files (by time or size).
  ```sql
  CREATE TABLE csv_source (id INT, name STRING) WITH (
    'connector' = 'filesystem', 'path' = '/data/input/',
    'format' = 'csv'
  );
  ```
- Connector discovery: Flink discovers connectors from JARs on the classpath. In PyFlink, add them via `env.add_jars("file:///path/to/connector.jar")` or via `pipeline.jars` config.
- Delivery guarantees per connector type: Kafka source + sink supports exactly-once when combined with Flink checkpointing and `EXACTLY_ONCE` delivery semantic. FileSystem sink supports exactly-once via atomic file commits. JDBC sink is at-least-once by default.
- Schema registries and Avro/JSON schema evolution: with a Schema Registry, producers and consumers share a schema ID in each message header. Flink's Avro format can fetch schemas from Confluent Schema Registry to handle evolution.

## Exercises

1. **Kafka source (Table API)**: Write a DDL statement (`CREATE TABLE`) that:
   - Reads from Kafka topic `events`
   - Uses JSON format
   - Schema: `(event_id STRING, user_id STRING, action STRING, ts TIMESTAMP(3), WATERMARK FOR ts AS ts - INTERVAL '5' SECOND)`
   - Kafka broker: `localhost:9092`, consumer group: `flink-consumer`

2. **Kafka sink**: Write a DDL statement for a Kafka sink table `processed_events` that:
   - Writes to topic `processed`
   - Uses JSON format
   - Schema: `(user_id STRING, action_count BIGINT, window_end TIMESTAMP(3))`

3. **End-to-end SQL pipeline**: Combine exercises 1 and 2 with a SQL INSERT that:
   - Reads from `events`
   - Groups by `user_id` in 1-minute tumbling windows
   - Counts actions per user per window
   - Writes results to `processed_events`

4. **FileSystem connector**: Write a DDL for a filesystem source that reads CSV files from `/data/input/` with schema `(id INT, name STRING, value DOUBLE)`.

```python
# Run: python solution.py
# Note: Kafka/JDBC exercises need running infrastructure. Focus on writing correct DDL/config.
```
