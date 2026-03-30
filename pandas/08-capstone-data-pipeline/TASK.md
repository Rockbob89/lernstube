# Task 08: Capstone — Data Pipeline

## Objective
Build an end-to-end data pipeline that loads, cleans, transforms, analyzes, and exports a messy dataset. Demonstrate mastery of all Pandas skills.

## Requirements

Create `pipeline.py` with a full data processing pipeline.

### Dataset
Use a publicly available messy dataset. Suggestions:
- [NYC 311 Service Requests](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9) (sample)
- Any CSV with dates, categories, numeric columns, and missing data
- Or generate a synthetic messy dataset with `generate_data.py`

### Pipeline Steps

1. **Load** — Read from CSV with proper dtypes, parse dates, handle encoding.
2. **Profile** — Print summary stats: shape, dtypes, null counts, unique counts per column.
3. **Clean** — Handle missing values (different strategies per column), fix dtypes, remove duplicates, standardize strings.
4. **Transform** — Add derived columns (e.g., extract date parts, categorize numeric ranges, compute running totals).
5. **Analyze** — GroupBy summaries, pivot tables, time-based aggregations. Print key findings.
6. **Export** — Save clean data as parquet, summary stats as JSON, and a brief report as CSV.

### Deliverables
- `pipeline.py` — Main pipeline script, runnable with `python pipeline.py <input.csv>`
- `generate_data.py` (optional) — Script to generate a synthetic messy dataset for testing
- Output files written to `output/` directory

### Evaluation Criteria
- Pipeline runs end-to-end without errors
- Each step is a clean function
- Proper use of method chaining where appropriate
- No unnecessary copies of large DataFrames
- Handles edge cases (empty groups, all-null columns, etc.)
- Code is production-quality: logging, error handling, docstrings
