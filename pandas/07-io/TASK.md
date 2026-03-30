# Task 07: I/O

## Objective
Read and write data in various formats with proper options.

## What to Learn
- `read_csv` / `to_csv`: encoding, dtypes, parse_dates, na_values, chunking
- `read_json` / `to_json`: orient options — `orient` controls the JSON structure; `"records"` is `[{col:val,...},...]`; `"split"` separates columns/index/data; `"index"` keys by index label
  ```python
  df.to_json(orient="records")   # '[{"a":1,"b":2},{"a":3,"b":4}]'
  df.to_json(orient="split")     # '{"columns":["a","b"],"index":[0,1],"data":[[1,2],[3,4]]}'
  ```
- `read_parquet` / `to_parquet`: column selection, compression — Parquet is columnar; reading only needed columns is much faster than CSV
  ```python
  pd.read_parquet("data.parquet", columns=["id", "value"])  # skip unused columns
  df.to_parquet("out.parquet", compression="snappy")
  ```
- `read_excel` (awareness, not deep focus)
- Chunked reading for large files — `read_csv` with `chunksize` returns an iterator of DataFrames instead of loading all at once
  ```python
  for chunk in pd.read_csv("big.csv", chunksize=10_000):
      process(chunk)  # each chunk is a normal DataFrame
  ```
- `read_clipboard`, `read_sql` (awareness)

## Exercises

Implement the functions in `solution.py`.

### 1. `smart_read_csv(path, **kwargs) -> pd.DataFrame`
Read a CSV with auto-detection of: separator (`,`, `;`, `\t`, `|`), encoding (try utf-8 then latin-1), and date columns (any column with "date" or "time" in the name). Pass through additional kwargs.
```python
df = smart_read_csv("data.csv")  # auto-detects sep, encoding, dates
```

### 2. `chunked_filter(path, column, value, chunksize=10000) -> pd.DataFrame`
Read a large CSV in chunks, filter rows where `column == value`, and return the combined result. Memory-efficient.
```python
result = chunked_filter("big_file.csv", "status", "active", chunksize=5000)
```

### 3. `convert_format(input_path, output_path) -> None`
Convert between formats based on file extension. Support: csv, json, parquet. Preserve dtypes where possible.
```python
convert_format("data.csv", "data.parquet")
convert_format("data.json", "output.csv")
```

### 4. `df_to_json_records(df) -> str`
Serialize DataFrame to JSON string in records orientation, handling datetime and NaN properly (NaN -> null, datetime -> ISO string).
```python
df = pd.DataFrame({"a": [1, None], "date": pd.to_datetime(["2024-01-01", "2024-06-15"])})
df_to_json_records(df)
# '[{"a":1.0,"date":"2024-01-01T00:00:00"},{"a":null,"date":"2024-06-15T00:00:00"}]'
```
