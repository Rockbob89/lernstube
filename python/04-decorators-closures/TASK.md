# Task 4: Decorators & Closures

## Objective
Understand closures and write practical decorators.

## What to Learn
- Closures: functions that capture enclosing scope
  ```python
  def make_adder(n):
      def add(x):
          return x + n  # `n` is captured from enclosing scope
      return add
  add5 = make_adder(5)
  add5(3)  # → 8
  ```
- Decorators: functions that wrap other functions
- `@decorator` syntax
- `functools.wraps` — preserving metadata; without it, the wrapper replaces the original's `__name__` and `__doc__`
  ```python
  from functools import wraps
  def my_decorator(fn):
      @wraps(fn)       # copies __name__, __doc__ etc. from fn to wrapper
      def wrapper(*args, **kwargs):
          return fn(*args, **kwargs)
      return wrapper
  ```
- Decorators with arguments — requires an extra layer of nesting (a function that returns a decorator)
  ```python
  def repeat(n):          # outer: takes config
      def decorator(fn):  # middle: takes the function
          @wraps(fn)
          def wrapper(*args, **kwargs):  # inner: called at runtime
              for _ in range(n):
                  fn(*args, **kwargs)
          return wrapper
      return decorator

  @repeat(3)
  def hello(): print("hi")
  ```

## Exercise

Create `solution.py` with the following:

### 1. `counter()`
A closure that returns a function. Each call increments and returns a count.

```python
c = counter()
c()  # → 1
c()  # → 2
c()  # → 3
```

### 2. `@timer`
A decorator that prints how long a function took to execute.

```python
@timer
def slow():
    import time; time.sleep(0.1)
    return "done"

slow()
# prints: slow took 0.10s
# returns: "done"
```

### 3. `@retry(max_attempts=3)`
A decorator WITH arguments. Retries the function up to `max_attempts` times if it raises an exception. Re-raises the last exception if all attempts fail.

```python
attempts = 0

@retry(max_attempts=3)
def flaky():
    global attempts
    attempts += 1
    if attempts < 3:
        raise ValueError("not yet")
    return "ok"

flaky()  # → "ok" (failed twice, succeeded third time)
```

### 4. `@validate_types(**type_kwargs)`
A decorator that checks keyword argument types at call time. Raise `TypeError` if wrong.

```python
@validate_types(name=str, age=int)
def register(name, age):
    return f"{name} is {age}"

register(name="Alice", age=30)  # → "Alice is 30"
register(name="Alice", age="thirty")  # → TypeError
```
