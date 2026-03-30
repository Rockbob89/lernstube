# Task 6: Decorators with Arguments

## Objective
Write a decorator that accepts configuration parameters.

## What to Learn

When a decorator itself needs configuration, you add an extra layer of nesting: a function that accepts the config and returns the actual decorator. Three levels total:

1. **Outer function** — takes the configuration
2. **Middle function** (the decorator) — takes the function being decorated
3. **Inner function** (the wrapper) — runs at call time

```python
from functools import wraps

def repeat(n):                # outer: takes config
    def decorator(fn):        # middle: takes the function
        @wraps(fn)
        def wrapper():        # inner: runs at call time
            for _ in range(n):
                fn()
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("hi")

say_hi()  # prints "hi" three times
```

What happens when Python sees `@repeat(3)`? It calls `repeat(3)`, which returns `decorator`. Then it applies `decorator` to `say_hi` — same as `say_hi = repeat(3)(say_hi)`.

The key insight: `repeat` is not a decorator. It's a **decorator factory** — a function that builds and returns a decorator.

## Exercise

### 1. `@retry(max_attempts=3)`
A decorator that retries a no-argument function up to `max_attempts` times if it raises an exception. If the function succeeds, return its result immediately. If all attempts fail, re-raise the last exception.

```python
attempts = 0

@retry(max_attempts=3)
def flaky():
    global attempts
    attempts += 1
    if attempts < 3:
        raise ValueError("not yet")
    return "ok"

flaky()  # → "ok" (failed twice, succeeded on third attempt)
```
