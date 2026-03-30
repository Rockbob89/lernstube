# Task 02: DataStream API

## Objective
Build streaming pipelines with PyFlink's DataStream API: sources, transformations, sinks.

## What to Learn
- `StreamExecutionEnvironment` setup and configuration: the entry point for every Flink DataStream job.
  ```python
  from pyflink.datastream import StreamExecutionEnvironment
  env = StreamExecutionEnvironment.get_execution_environment()
  env.set_parallelism(1)
  ```
- Sources: `from_collection` creates a bounded stream from a Python list. `from_source` connects to external systems (Kafka, filesystem) via the Source API.
  ```python
  ds = env.from_collection([("sensor_1", 23.5), ("sensor_2", 18.1)],
                            type_info=Types.TUPLE([Types.STRING(), Types.DOUBLE()]))
  ```
- Transformations: `map` (1-to-1), `flat_map` (1-to-N), `filter` (drop records), `key_by` (partition by key for stateful ops), `reduce` (aggregate within a key).
  ```python
  ds.filter(lambda x: x[1] > 20.0).map(lambda x: (x[0], x[1], "HIGH" if x[1] > 24 else "NORMAL"))
  ds.key_by(lambda x: x[0]).reduce(lambda a, b: (a[0], a[1] + b[1]))
  ```
- Sinks: `print()` writes to stdout. `add_sink(...)` connects to external sinks. `execute_and_collect()` returns results to the driver (for small bounded jobs).
- Type system: `Types.ROW`, `Types.STRING`, `Types.FLOAT`, etc. — PyFlink needs explicit type info for serialization across network boundaries.
- Parallelism: set globally with `env.set_parallelism(N)` or per-operator with `.set_parallelism(N)` after a transformation. More parallelism = more task slots consumed.

## Exercises

1. **Basic pipeline**: Write a pipeline that:
   - Reads from a list of tuples: `[("sensor_1", 23.5), ("sensor_2", 18.1), ("sensor_1", 25.0), ("sensor_2", 19.3), ("sensor_1", 22.8)]`
   - Filters readings above 20.0
   - Maps to add a status field: `(sensor_id, temp, "HIGH" if temp > 24 else "NORMAL")`
   - Prints the output

2. **Key-by and reduce**: Write a pipeline that:
   - Reads events: `[("user_a", 1), ("user_b", 3), ("user_a", 2), ("user_b", 1), ("user_a", 4)]`
   - Groups by user (key_by)
   - Reduces to compute running sum per user
   - Prints results

3. **FlatMap**: Write a pipeline that:
   - Reads sentences: `["hello world", "flink is great", "hello flink"]`
   - FlatMaps to individual words
   - Filters out words shorter than 4 characters
   - Prints results

```python
# Run: python solution.py
```
