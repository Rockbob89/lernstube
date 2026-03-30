# Task 2: Data Structures Deep Dive

## Objective
Know Python's built-in and standard library data structures beyond lists and dicts — when to reach for each one.

## What to Learn
- `tuple` — immutable sequences, tuple unpacking, as dict keys
- `set` — unique elements, set operations (union, intersection, difference)
- `namedtuple` — lightweight immutable objects with named fields
- `defaultdict` — dicts with automatic default values
- `Counter` — counting occurrences

## Exercise

Create `solution.py` with the following functions:

### 1. `unique_words(text: str) -> set`
Return the set of unique lowercase words in a text. Strip punctuation (.,!?;:).

```python
unique_words("Hello world! Hello, Python.")
# → {"hello", "world", "python"}
```

### 2. `top_n(items: list, n: int) -> list`
Return the `n` most common items as a list of `(item, count)` tuples, most common first.

```python
top_n(["a", "b", "a", "c", "b", "a"], 2)
# → [("a", 3), ("b", 2)]
```

### 3. `group_by_length(words: list) -> dict`
Group words by their length. Use `defaultdict`. Return a regular dict.

```python
group_by_length(["hi", "hey", "go", "wow"])
# → {2: ["hi", "go"], 3: ["hey", "wow"]}
```

### 4. `make_record(fields: list, values: list)`
Create a namedtuple type called `Record` with the given field names, then return an instance with the given values.

```python
r = make_record(["name", "age"], ["Alice", 30])
r.name  # → "Alice"
r.age   # → 30
```

### 5. `set_ops(a: set, b: set) -> tuple`
Return a tuple of four sets: `(union, intersection, only_a, only_b)`.

```python
set_ops({1, 2, 3}, {2, 3, 4})
# → ({1, 2, 3, 4}, {2, 3}, {1}, {4})
```
