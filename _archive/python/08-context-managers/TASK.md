# Task 8: Context Managers

## Objective
Understand the `with` statement and write your own context managers.

## What to Learn
- What `with` does and why it exists (resource cleanup)
- `__enter__` and `__exit__` methods — `__enter__` runs on entry and its return value is bound to `as`; `__exit__` always runs on exit, even if an exception was raised
  ```python
  class Managed:
      def __enter__(self):
          return self          # bound to `as` variable
      def __exit__(self, exc_type, exc_val, tb):
          # exc_type is None if no exception occurred
          return False         # False = don't suppress exceptions
  ```
- `contextlib.contextmanager` decorator — turns a generator into a context manager; `yield` is the `with` block boundary
  ```python
  from contextlib import contextmanager

  @contextmanager
  def managed():
      print("setup")
      yield "resource"   # value bound to `as`
      print("teardown")  # runs even if exception raised inside `with`
  ```
- When to use which approach: class-based when you need state or inheritance; `@contextmanager` for simple cases

## Exercise

Create `solution.py` with the following:

### 1. `class Timer`
A context manager (class-based) that measures elapsed time.

```python
with Timer() as t:
    time.sleep(0.1)
print(t.elapsed)  # → ~0.1
```

### 2. `@contextmanager` version: `tempdir()`
Creates a temporary directory, yields its path, then deletes it on exit (even if an exception occurs).

```python
with tempdir() as path:
    print(path)  # → /tmp/xyz123
    # create files in it...
# directory is gone now
```

Use `tempfile.mkdtemp()` and `shutil.rmtree()`.

### 3. `class DatabaseConnection` (simulated)
A context manager that simulates a DB connection. Tracks state via attributes.

```python
db = DatabaseConnection("mydb")
with db:
    print(db.connected)  # → True
    db.execute("SELECT 1")
print(db.connected)  # → False
print(db.queries)  # → ["SELECT 1"]
```

If an exception occurs inside the `with` block, set `db.error` to the exception and still disconnect. Don't suppress the exception.
