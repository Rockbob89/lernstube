# Task 5: Basic Decorators

## Objective
Write a simple decorator that wraps a no-argument function.

## What to Learn

A **decorator** is a function that takes a function as input and returns a new function that wraps it. The `@decorator` syntax is shorthand for `fn = decorator(fn)`.

Why use decorators? They let you add behavior (logging, timing, caching) to functions without modifying the function itself.

```python
def shout(fn):
    def wrapper():
        result = fn()
        return result.upper()
    return wrapper

@shout
def whisper():
    return "hello"

print(whisper())        # → HELLO
print(whisper.__name__) # → wrapper  (uh oh)
```

Notice the problem: `whisper.__name__` is now `"wrapper"`, not `"whisper"`. That breaks debugging and introspection. Fix it with `functools.wraps`:

```python
from functools import wraps

def shout(fn):
    @wraps(fn)
    def wrapper():
        result = fn()
        return result.upper()
    return wrapper

@shout
def whisper():
    return "hello"

print(whisper.__name__)  # → whisper (correct)
```

`@wraps(fn)` copies `__name__`, `__doc__`, and other attributes from the original function onto the wrapper. Always use it.

## Exercise

### 1. `@timer`
A decorator that prints how long a no-argument function took to execute. Format: `"{name} took {seconds:.2f}s"`. Use `time.time()` to measure elapsed time. The decorator must preserve the original function's name.

```python
import time

@timer
def slow():
    time.sleep(0.1)
    return "done"

slow()
# prints: slow took 0.10s
# returns: "done"
```
