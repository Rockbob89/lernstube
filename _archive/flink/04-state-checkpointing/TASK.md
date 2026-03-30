# Task 04: State & Checkpointing

## Objective
Use Flink's state primitives and configure checkpointing for fault tolerance.

## What to Learn
- Keyed state types — all scoped per key, accessed only inside `KeyedProcessFunction` or keyed operators:
  - `ValueState[T]`: single value per key. Get: `state.value()`, set: `state.update(v)`, clear: `state.clear()`.
  - `ListState[T]`: list of values per key. `state.add(v)`, `state.get()` returns an iterable.
  - `MapState[K, V]`: key-value map per key. `state.put(k, v)`, `state.get(k)`, `state.contains(k)`.
  - `ReducingState[T]`: auto-reduces on `add()` using a provided `ReduceFunction`.
- Operator state vs keyed state: operator state is partitioned per operator instance (not per key) — used for sources/sinks that don't key their stream (e.g., Kafka offset tracking).
- State backends: `HashMapStateBackend` stores state in JVM heap (fast, limited by memory); `EmbeddedRocksDBStateBackend` stores state on disk (supports TB-scale state, ~10x slower reads, required for large state).
- Checkpointing: Flink snapshots all operator state using the Chandy-Lamport algorithm — it injects barrier messages into the stream; when every operator has received a barrier, their state is snapshotted to durable storage (S3/HDFS). On failure, Flink resets to the last checkpoint.
  ```python
  env.enable_checkpointing(30_000)  # every 30 seconds
  ```
- Savepoints vs checkpoints: checkpoints are automatic and managed by Flink (deleted when superseded); savepoints are manual snapshots you take explicitly (`flink savepoint <job_id>`), used for upgrades or job migrations. Both restore to the same state.
- Exactly-once vs at-least-once checkpoint mode: exactly-once waits for all operators to align on barriers before snapshotting (higher latency, stronger guarantee); at-least-once snapshots without barrier alignment (faster, may reprocess events on recovery).
- State TTL for automatic cleanup: configure per state descriptor to expire entries after inactivity.
  ```python
  from pyflink.datastream.state import StateTtlConfig, TtlUpdateType
  from pyflink.common import Time
  ttl = StateTtlConfig.new_builder(Time.seconds(60)).set_update_type(TtlUpdateType.OnCreateAndWrite).build()
  state_desc.enable_time_to_live(ttl)
  ```

## Exercises

1. **ValueState counter**: Write a `KeyedProcessFunction` that:
   - Receives `(user_id, event_type)` events
   - Keeps a `ValueState[int]` count per user
   - Emits `(user_id, count)` after every 3rd event from the same user
   - Test data: `[("alice", "click"), ("bob", "click"), ("alice", "view"), ("alice", "click"), ("bob", "view"), ("bob", "click"), ("bob", "click")]`

2. **MapState deduplication**: Write a `KeyedProcessFunction` that:
   - Receives `(key, event_id, value)` events
   - Uses `MapState` to track seen `event_id`s per key
   - Only emits events with unseen event_ids (deduplication)
   - Uses state TTL of 60 seconds to auto-expire old entries

3. **Checkpoint configuration**: Write a function `configure_checkpointing(env)` that:
   - Enables checkpointing every 30 seconds
   - Sets exactly-once mode
   - Sets minimum pause between checkpoints to 10 seconds
   - Sets checkpoint timeout to 60 seconds
   - Configures RocksDB state backend with incremental checkpoints

```python
# Run: python solution.py
```
