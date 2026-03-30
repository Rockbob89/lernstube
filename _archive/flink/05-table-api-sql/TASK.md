# Task 05: Table API & SQL

## Objective
Use Flink's Table API and SQL to query streams as dynamic tables.

## What to Learn
- Table environment setup and relationship to DataStream environment:
  ```python
  from pyflink.table import StreamTableEnvironment
  t_env = StreamTableEnvironment.create(env)
  ```
- Dynamic tables: a stream viewed as a table where each event is a row append. An aggregating query over a stream produces an updating (retract) table where rows change as new events arrive.
- SQL on streams: same syntax as static SQL, but runs continuously. `GROUP BY` without windowing produces an ever-updating result.
  ```python
  t_env.execute_sql("SELECT category, SUM(price) FROM products GROUP BY category").print()
  ```
- Temporal table joins: join a stream against a slowly-changing dimension table keyed by time — the lookup uses the version of the dimension valid at the event's timestamp. Used for currency rates, product catalogs.
- Time attributes: declare a column as the event time attribute in DDL, then reference it in window TVFs:
  ```sql
  CREATE TABLE events (
    id STRING, ts TIMESTAMP(3),
    WATERMARK FOR ts AS ts - INTERVAL '5' SECOND
  ) WITH (...);
  ```
- `TUMBLE`, `HOP`, `SESSION` window TVFs in SQL:
  ```sql
  SELECT window_start, window_end, SUM(amount)
  FROM TABLE(TUMBLE(TABLE sales, DESCRIPTOR(ts), INTERVAL '1' MINUTE))
  GROUP BY window_start, window_end
  ```
- Converting between DataStream and Table: `t_env.from_data_stream(ds)` and `t_env.to_data_stream(table)`. Useful to mix low-level and high-level APIs in one job.

## Exercises

1. **SQL aggregation**: Create a table from this data and run SQL to compute total value per category:
   - Data: `[("electronics", "laptop", 999), ("books", "python", 45), ("electronics", "mouse", 25), ("books", "java", 55), ("electronics", "keyboard", 75)]`
   - Schema: `(category STRING, product STRING, price INT)`
   - SQL: `SELECT category, SUM(price) as total FROM products GROUP BY category`

2. **Windowed SQL**: Given timestamped sales events, write SQL using `TUMBLE` window TVF to compute:
   - Total sales per category per 1-minute tumbling window
   - Data: `(category, amount, event_time)`
   - Output: `(category, window_start, window_end, total_amount)`

3. **Stream-Table conversion**: Write a pipeline that:
   - Creates a DataStream of `(user_id, action, timestamp)`
   - Converts it to a Table
   - Runs a SQL query to count actions per user
   - Converts the result back to a DataStream and prints it

```python
# Run: python solution.py
```
