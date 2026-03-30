# Task 2: Request & Response Models

## Objective
FastAPI's superpower is Pydantic integration. Learn to define request/response schemas, get automatic validation, serialization, and OpenAPI documentation for free.

## What to Learn
- `BaseModel` — Pydantic model definition
  ```python
  from pydantic import BaseModel
  class Item(BaseModel):
      name: str
      price: float
  ```
- `Field()` — constraints, defaults, descriptions
  ```python
  from pydantic import Field
  price: float = Field(gt=0, description="Must be positive")
  ```
- Request body parsing — automatic JSON deserialization; declare a `BaseModel` as a parameter and FastAPI handles the rest
- `response_model` — control what gets returned
  ```python
  @app.post("/items", response_model=ItemResponse)
  def create_item(item: ItemCreate): ...
  ```
- `model_dump()` / `model_validate()` — serialization
  ```python
  item.model_dump()                    # -> dict
  Item.model_validate({"name": "x", "price": 1.0})  # -> Item
  ```
- Optional fields, nested models, lists of models
  ```python
  description: str | None = None
  tags: list[str] = []
  ```

## Exercises

### 1. Basic Request Model
Define a `ItemCreate` model with `name: str`, `price: float` (gt=0), and `description: str | None = None`. Use it as a POST body. Return the validated data.

```python
# POST /items  {"name": "widget", "price": -1}
# -> 422 (price must be > 0)

# POST /items  {"name": "widget", "price": 9.99}
# -> {"name": "widget", "price": 9.99, "description": null}
```

### 2. Response Model
Define `ItemResponse` that adds `id: int` to the fields. Use `response_model=ItemResponse` on the endpoint. Store items and return with generated id.

```python
# POST /items  {"name": "widget", "price": 9.99}
# -> {"id": 1, "name": "widget", "price": 9.99, "description": null}
```

### 3. Nested Models
Define a `Category` model with `name: str` and `items: list[ItemResponse]`. Add `GET /categories/{name}` that returns a category with its items.

```python
# GET /categories/electronics
# -> {"name": "electronics", "items": [{"id": 1, ...}, ...]}
```

### 4. Update with Partial Data
Define `ItemUpdate` where all fields are optional. Add `PATCH /items/{item_id}` that updates only the provided fields using `model_dump(exclude_unset=True)`.

```python
# PATCH /items/1  {"price": 19.99}
# -> {"id": 1, "name": "widget", "price": 19.99, "description": null}
```
