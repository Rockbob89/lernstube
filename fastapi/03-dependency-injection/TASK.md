# Task 3: Dependency Injection

## Objective
FastAPI's DI system via `Depends()` is how you share logic across endpoints: database sessions, auth checks, pagination, etc. Think of it as middleware you can inject per-endpoint.

## What to Learn
- `Depends()` — declaring dependencies
  ```python
  from fastapi import Depends
  def get_token(token: str = Header(...)):
      return token

  @app.get("/secure")
  def secure(tok: str = Depends(get_token)): ...
  ```
- Callable dependencies (functions and classes) — any callable works; class instances are resolved by calling `__init__`
- Dependency chaining — dependencies that have dependencies
  ```python
  def get_user(db=Depends(get_db), token=Depends(get_token)):
      ...
  ```
- `yield` dependencies — setup/teardown (like context managers); code after `yield` runs after the response is sent
- Overriding dependencies for testing
  ```python
  app.dependency_overrides[get_db] = lambda: fake_db
  ```

## Exercises

### 1. Simple Dependency
Create a `common_params` function that extracts `skip: int = 0` and `limit: int = 100` from query params. Use it in two endpoints via `Depends()`.

```python
# GET /items?skip=5&limit=10     -> {"skip": 5, "limit": 10, "items": [...]}
# GET /users?skip=0&limit=50     -> {"skip": 0, "limit": 50, "users": [...]}
```

### 2. Class-Based Dependency
Convert `common_params` to a class with `__init__` that takes the same params. Access them as attributes.

```python
class CommonParams:
    def __init__(self, skip: int = 0, limit: int = 100):
        self.skip = skip
        self.limit = limit
```

### 3. Dependency Chain
Create a `get_db` dependency that yields a fake DB dict. Create a `get_current_user` dependency that depends on a header `X-User` and uses `get_db` to look up the user. Use `get_current_user` in a protected endpoint.

```python
# GET /me  (X-User: alice)  -> {"username": "alice", "role": "admin"}
# GET /me  (no header)      -> 401
```

### 4. Yield Dependencies
Create a `get_db_session` dependency using `yield` that prints "opening session" before and "closing session" after. Verify teardown happens even on errors.

```python
def get_db_session():
    print("opening session")
    db = {"connection": "active"}
    try:
        yield db
    finally:
        print("closing session")
```
