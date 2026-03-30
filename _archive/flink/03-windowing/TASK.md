# Task 03: Windowing

## Objective
Apply windowing strategies to streaming data: tumbling, sliding, session windows, and handle late data with watermarks.

## What to Learn
- Window types: **tumbling** (fixed non-overlapping buckets, e.g. 10s/10s); **sliding** (overlapping, e.g. 30s window every 10s); **session** (gap-based — a new window opens after N seconds of inactivity); **global** (one window for all time, triggers manually).
- Event time vs processing time vs ingestion time: event time = timestamp in the event payload (most accurate, handles out-of-order); processing time = wall clock when Flink processes the record (simple, but affected by lag); ingestion time = when the event entered Flink.
- Watermarks: a monotonically increasing timestamp that tells Flink "all events with timestamp ≤ W have arrived". When the watermark passes a window's end time, that window fires.
- `WatermarkStrategy`: wraps both a timestamp extractor and a watermark generator.
  ```python
  from pyflink.common.watermark_strategy import WatermarkStrategy
  from datetime import timedelta
  strategy = WatermarkStrategy \
      .for_bounded_out_of_orderness(timedelta(seconds=5)) \
      .with_timestamp_assigner(MyTimestampAssigner())
  ds.assign_timestamps_and_watermarks(strategy)
  ```
- Late data handling: `allowed_lateness` delays window cleanup so late events can still be included. Events arriving after allowed lateness can be routed to a side output instead of dropped.
- Window functions: `reduce` (incremental aggregation, memory-efficient), `aggregate` (accumulator pattern), `process` (full `WindowFunction` with access to all window elements — use only when needed, expensive).

## Exercises

1. **Tumbling window**: Write a pipeline that:
   - Reads timestamped events: `[(sensor_id, temperature, event_time_ms), ...]`
   - Assigns watermarks with 5-second bounded out-of-orderness
   - Applies a 10-second tumbling window
   - Computes average temperature per sensor per window
   - Prints `(sensor_id, avg_temp, window_start, window_end)`

2. **Sliding window**: Modify exercise 1 to use a sliding window of 30 seconds with a 10-second slide. Observe how events appear in multiple windows.

3. **Session window**: Write a pipeline that:
   - Reads user click events: `[(user_id, page, timestamp_ms), ...]`
   - Uses session windows with a 5-second gap
   - Counts clicks per user per session
   - Prints `(user_id, click_count, session_start, session_end)`

```python
# Run: python solution.py
```
