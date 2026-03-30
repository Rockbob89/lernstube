# Task 9: Error Handling

## Objective
Handle errors properly and define custom exceptions.

## What to Learn
- `try/except/else/finally` — what runs when
- Catching specific exceptions
- `raise` and `raise ... from ...` (exception chaining) — attaches a cause; sets `__cause__` on the new exception
  ```python
  try:
      data["key"]
  except KeyError as e:
      raise ValueError("missing required field") from e
  # traceback shows both exceptions; e.__cause__ is the KeyError
  ```
- Custom exception classes
- When NOT to catch exceptions

## Exercise

Create `solution.py` with the following:

### 1. Custom exception hierarchy

```python
class AppError(Exception): ...
class ValidationError(AppError): ...
class NotFoundError(AppError): ...
```

`ValidationError` should accept a `field` and `message`. `NotFoundError` should accept a `resource` and `id`.

```python
raise ValidationError("email", "must contain @")
# str(e) → "Validation error on 'email': must contain @"

raise NotFoundError("User", 42)
# str(e) → "User with id=42 not found"
```

### 2. `safe_divide(a, b) -> dict`
Return `{"result": value}` on success, `{"error": "division by zero"}` if b is 0, `{"error": "invalid type"}` if inputs aren't numbers. Use `try/except/else`.

### 3. `parse_config(data: dict, required_keys: list) -> dict`
Validate that all `required_keys` exist in `data` and are non-empty strings. Raise `ValidationError` for the first failing key. If a key is missing entirely, chain it from `KeyError`.

```python
parse_config({"host": "localhost"}, ["host", "port"])
# → raises ValidationError("port", "missing") with __cause__ = KeyError("port")
```
