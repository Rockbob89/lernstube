# Task 08: Capstone — Data Pipeline

## Objective
Build a complete, production-style Airflow pipeline that orchestrates: ingest, validate, transform, load, and notify.

## Requirements

Build a DAG `capstone_pipeline` that simulates a daily data pipeline:

1. **Ingest** (`extract_data`): Read a JSON file from `/tmp/airflow_capstone/raw/input.json`. If the file doesn't exist, use a sensor to wait (5min timeout).

2. **Validate** (`validate_data`): Check that the data has required fields (`id`, `timestamp`, `value`). Branch: if valid, continue; if invalid, go to `notify_failure`.

3. **Transform** (`transform_data`):
   - Filter records where `value > 0`
   - Add a `processed_at` timestamp
   - Return the transformed data via XCom (or write to `/tmp/airflow_capstone/staging/`)

4. **Load** (`load_data`): Write final output to `/tmp/airflow_capstone/output/result.json`.

5. **Notify** (`notify_success` / `notify_failure`): Print success/failure message with record count. Use appropriate trigger rules.

## Constraints
- Use the TaskFlow API
- Use at least one sensor, one branch, and dynamic task mapping (map over validation checks if you want)
- DAG must be idempotent
- Include `default_args` with `retries=2` and `retry_delay=timedelta(minutes=1)`
- Write a pytest test that validates DAG structure

## Test Data
Create `/tmp/airflow_capstone/raw/input.json`:
```json
[
  {"id": 1, "timestamp": "2026-03-30T10:00:00", "value": 42},
  {"id": 2, "timestamp": "2026-03-30T10:01:00", "value": -1},
  {"id": 3, "timestamp": "2026-03-30T10:02:00", "value": 99}
]
```
