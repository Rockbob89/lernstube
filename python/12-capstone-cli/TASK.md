# Task 12: Capstone — CLI Tool

## Objective
Build a complete CLI application that uses everything from tasks 1–11.

## The Project: `loggrep` — a structured log analyzer

Build a CLI tool that reads structured log files (JSON lines format) and provides filtering, aggregation, and summary output.

### Input format
Each line is a JSON object:
```json
{"timestamp": "2024-01-15T10:30:00Z", "level": "ERROR", "service": "auth", "message": "login failed", "user_id": 42}
{"timestamp": "2024-01-15T10:30:01Z", "level": "INFO", "service": "api", "message": "request completed", "duration_ms": 150}
```

### Required commands

```bash
# Filter by level
loggrep filter --level ERROR logs.jsonl

# Filter by time range
loggrep filter --after 2024-01-15T10:00:00Z --before 2024-01-15T11:00:00Z logs.jsonl

# Filter by field value
loggrep filter --where service=auth logs.jsonl

# Count by field
loggrep count --by level logs.jsonl
# ERROR: 42
# INFO: 156
# WARN: 23

# Summary stats
loggrep summary logs.jsonl
# Lines: 221
# Time range: 2024-01-15T10:00:00Z → 2024-01-15T11:00:00Z
# Levels: ERROR=42 INFO=156 WARN=23
# Services: auth, api, worker

# Combine filters
loggrep filter --level ERROR --where service=auth logs.jsonl | loggrep count --by user_id
```

### Requirements
- Use `argparse` or `click` for CLI parsing
- Proper package structure with `pyproject.toml`
- Type hints throughout, passes `mypy --strict`
- Tests with pytest (≥80% coverage on core logic)
- Custom exceptions for bad input
- Generator-based file reading (don't load entire file into memory)
- Context manager for file handling
- Decorators where they make sense (e.g., timing, error handling)
- Include a `generate_logs.py` script that creates sample test data
