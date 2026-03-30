# Task 01: Stream vs Batch

## Objective
Understand Flink's unified stream-batch model and when to choose Flink over alternatives.

## What to Learn
- Flink's "stream-first" philosophy: batch as a special case of streaming. A bounded stream (finite input) is processed the same way as an unbounded stream — Flink just knows it will end.
- Bounded vs unbounded streams: bounded = a file or a time-limited dataset with a known end; unbounded = a Kafka topic or event log that never ends.
- Flink vs Kafka Streams: Kafka Streams runs embedded in your app (no cluster), ideal for simple per-topic transformations. Flink requires a standalone/K8s cluster but handles complex stateful logic, joins across streams, and much larger state.
- Flink vs Spark Streaming: Spark Streaming is micro-batch (collects events for N seconds, then processes). Flink processes each event individually (true streaming), giving sub-second latency. For batch-like analytics with 1-minute SLAs, both work; for fraud detection or real-time alerts, Flink wins.
- Flink's architecture: **JobManager** (master — coordinates, schedules, checkpoints), **TaskManagers** (workers — execute tasks in slots). Parallelism = how many parallel copies of each operator run. One slot = one thread on a TaskManager.
- DataStream API vs Table API vs SQL: DataStream = full control, Java/Python, low-level; Table API = relational, type-safe; SQL = ad-hoc queries or DDL. All three can interop within one job.

## Exercises

1. **Architecture diagram**: Draw Flink's runtime architecture showing JobManager, TaskManagers, task slots, and how a job is submitted. Show where checkpointing fits.

2. **Comparison table**: Create a comparison of Flink, Kafka Streams, and Spark Streaming across:
   - Deployment model (standalone vs embedded vs cluster)
   - Processing guarantee (at-least-once, exactly-once)
   - State management
   - Latency characteristics
   - When to pick each

3. **Scenario matching**: For each scenario, pick the best tool (Flink, Kafka Streams, Spark Streaming, or plain Kafka) and justify:
   - Real-time fraud detection with complex event patterns and large state
   - Simple message transformation between Kafka topics in a microservice
   - Hourly aggregation of clickstream data already in S3
   - Sessionization of user events with irregular gaps

4. **PyFlink setup**: Install PyFlink locally and run the hello-world: read a list of strings, count word occurrences, print results. Confirm it works.

Write conceptual answers (exercises 1-3) in `solution.md`. Write PyFlink code (exercise 4) in `solution.py`.
