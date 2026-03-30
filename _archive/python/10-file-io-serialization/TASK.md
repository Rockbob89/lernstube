# Task 10: File I/O & Serialization

## Objective
Read and write files, work with common data formats.

## What to Learn
- `open()`, read/write modes, encoding
- `pathlib.Path` — modern file path handling; replaces `os.path`; supports `/` for joining
  ```python
  from pathlib import Path
  p = Path("/tmp") / "data" / "file.txt"
  p.suffix          # '.txt'
  p.parent          # Path('/tmp/data')
  p.read_text()     # open + read + close in one call
  list(p.parent.glob("*.txt"))  # recursive with rglob
  ```
- `json` module — loads, dumps, custom serialization
- `csv` module — reader, writer, DictReader, DictWriter

## Exercise

Create `solution.py` with the following:

### 1. `word_frequency(filepath: Path) -> dict`
Read a text file, return a dict of `{word: count}` (lowercase, strip punctuation).

### 2. `merge_csv_files(filepaths: list[Path], output: Path)`
Read multiple CSV files (all with the same columns), merge them into one output CSV. Deduplicate rows.

### 3. `json_transform(input_path: Path, output_path: Path, transform_fn)`
Read a JSON file, apply `transform_fn` to each item (assumes top-level list), write the result.

```python
# If input.json contains [{"name": "alice"}, {"name": "bob"}]
json_transform(
    Path("input.json"),
    Path("output.json"),
    lambda item: {**item, "name": item["name"].upper()}
)
# output.json → [{"name": "ALICE"}, {"name": "BOB"}]
```

### 4. `find_files(directory: Path, pattern: str) -> list[Path]`
Recursively find all files matching a glob pattern. Return sorted list of paths.

```python
find_files(Path("."), "*.py")
# → [Path("a.py"), Path("sub/b.py")]
```

Create sample test files to verify your functions work.
