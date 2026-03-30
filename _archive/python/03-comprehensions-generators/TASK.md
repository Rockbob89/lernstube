# Task 3: Comprehensions & Generators

## Objective
Write concise, Pythonic transformations using comprehensions and generators.

## What to Learn

### Comprehensions
A compact syntax for building lists, dicts, or sets from loops.

```python
# List comprehension
[x * 2 for x in range(5)]           # → [0, 2, 4, 6, 8]

# With condition (filter)
[x for x in range(10) if x % 3 == 0]  # → [0, 3, 6, 9]

# Dict comprehension
{k: len(k) for k in ["hi", "bye"]}  # → {"hi": 2, "bye": 3}

# Set comprehension
{x % 3 for x in range(10)}          # → {0, 1, 2}

# Nested — outer loop first, inner loop second
[c for word in ["ab", "cd"] for c in word]  # → ["a", "b", "c", "d"]
```

### Generators
Like comprehensions, but lazy — they yield values one at a time instead of building the whole list in memory.

```python
# Generator expression (parentheses instead of brackets)
g = (x * 2 for x in range(5))
next(g)  # → 0
next(g)  # → 2

# Generator function (uses yield)
def countdown(n):
    while n > 0:
        yield n
        n -= 1

list(countdown(3))  # → [3, 2, 1]
```

`yield` pauses the function and returns a value. Next call resumes where it left off.

## Exercise

Create `solution.py` with the following:

### 1. `flatten(nested: list) -> list`
Flatten a list of lists into a single list using a comprehension.

```python
flatten([[1, 2], [3, 4], [5]])
# → [1, 2, 3, 4, 5]
```

### 2. `word_lengths(sentence: str) -> dict`
Return a dict mapping each word to its length. One comprehension.

```python
word_lengths("the quick brown fox")
# → {"the": 3, "quick": 5, "brown": 5, "fox": 3}  
```

### 3. `evens_squared(numbers: list) -> list`
Return squares of even numbers only. One comprehension.

```python
evens_squared([1, 2, 3, 4, 5, 6])
# → [4, 16, 36]
```

### 4. `matrix_transpose(matrix: list) -> list`
Transpose a matrix (list of lists) using a nested comprehension.

```python
matrix_transpose([[1, 2, 3], [4, 5, 6]])
# → [[1, 4], [2, 5], [3, 6]]
```

### 5. `log_reader(lines: list)` (generator)
A generator that takes a list of log lines and yields only the ones containing "ERROR", stripped of whitespace.

Imagine the list is a stand-in for a massive file you don't want to load entirely.

```python
logs = [
    "  INFO: started  ",
    "  ERROR: disk full  ",
    "  INFO: retrying  ",
    "  ERROR: timeout  ",
]
list(log_reader(logs))
# → ["ERROR: disk full", "ERROR: timeout"]
```

### 6. `chunk(iterable, size: int)` (generator)
Yield successive chunks of `size` from any iterable. Last chunk may be shorter.

```python
list(chunk(range(10), 3))
# → [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
```
