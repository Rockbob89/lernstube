# Task 1: Hello World & Routing

## Objective
Get a FastAPI app running. Understand path operations, path parameters, query parameters, and HTTP method decorators.

## What to Learn
- `FastAPI()` app instance
  ```python
  from fastapi import FastAPI
  app = FastAPI()
  ```
- `@app.get()`, `@app.post()`, etc. — path operation decorators
  ```python
  @app.get("/")
  def root():
      return {"message": "hello"}
  ```
- Path parameters with type hints — automatic validation
  ```python
  @app.get("/items/{item_id}")
  def get_item(item_id: int):   # 422 if non-int supplied
      return {"item_id": item_id}
  ```
- Query parameters — optional, defaults, required
  ```python
  @app.get("/search")
  def search(q: str, skip: int = 0, limit: int = 10):
      ...
  ```
- Running with `uvicorn` — the ASGI server
  ```bash
  uvicorn main:app --reload --port 8000
  ```
- Auto-generated OpenAPI docs at `/docs`

## Exercises

### 1. Hello World
Create an app with a GET `/` that returns `{"message": "hello world"}`. Run it with uvicorn on port 8000.

```python
# GET /
# -> {"message": "hello world"}
```

### 2. Path Parameters
Add `GET /items/{item_id}` that takes an `int` path param. Return `{"item_id": item_id}`. Try passing a string — observe the automatic 422 validation error.

```python
# GET /items/42    -> {"item_id": 42}
# GET /items/foo   -> 422 Unprocessable Entity
```

### 3. Query Parameters
Add `GET /items` that accepts optional query params `skip: int = 0` and `limit: int = 10`. Return them.

```python
# GET /items?skip=5&limit=20  -> {"skip": 5, "limit": 20}
# GET /items                   -> {"skip": 0, "limit": 10}
```

### 4. Multiple Methods
Add a `POST /items` that accepts a JSON body with `name: str` and `price: float`. Return the item with an auto-generated id. Store items in a module-level list.

```python
# POST /items  {"name": "widget", "price": 9.99}
# -> {"id": 1, "name": "widget", "price": 9.99}
```

### 5. Route Order
Add `GET /items/latest` that returns the last item. Place it BEFORE the `GET /items/{item_id}` route. Explain (in a comment) why order matters.

```python
# GET /items/latest -> {"id": 3, "name": "...", "price": ...}
```
