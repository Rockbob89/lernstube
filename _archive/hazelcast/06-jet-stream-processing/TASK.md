# Task 06: Jet (Stream Processing)

## Objective
Understand Hazelcast Jet for stream and batch processing — pipelines, sources, sinks, and windowing.

## What to Learn
- Jet as Hazelcast's stream processing engine (merged into Platform)
- Pipeline API: sources -> transforms -> sinks
  ```python
  # Conceptual — Jet API is Java; Python interacts via IMap journal or Kafka
  # source → filter → map → aggregate → sink
  # Each stage runs in parallel on all cluster members
  ```
- Sources: IMap journal, Kafka, files, custom
  ```
  IMap journal: change stream of all put/remove events on an IMap — like a CDC log
  ```
- Sinks: IMap, Kafka, files, logging, custom
- Stateless transforms: map, filter, flatMap
- Stateful transforms: aggregate, window
- Windowing: tumbling, sliding, session windows
  ```
  tumbling(5s):  [0-5) [5-10) [10-15) — non-overlapping fixed windows
  sliding(5s,1s):[0-5) [1-6)  [2-7)   — overlapping, step=1s
  session(gap=30s): window closes after 30s of inactivity
  ```
- Watermarks and event-time processing
- Fault tolerance: snapshots

## Exercises

1. **Pipeline builder**: Build a stream pipeline simulator. Create a `JetPipeline` class with a fluent API: `read_from(source)`, `map()`, `filter()`, `group_by()`, `aggregate()`, `write_to(sink)`. Execute it against sample data.

2. **Windowing engine**: Implement tumbling and sliding window logic. Given a stream of timestamped events, group them into windows, and apply an aggregate function per window.

3. **Event-time processor**: Build a simplified event-time processor that handles out-of-order events using watermarks. Events arriving after the watermark should be counted as late and optionally dropped or sent to a side output.
