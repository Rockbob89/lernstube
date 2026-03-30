# Task 8: Testing

## Objective
A production API needs tests. Learn FastAPI's `TestClient` (built on httpx), pytest fixtures for app setup, and how to override dependencies for isolated testing.

## What to Learn
- `TestClient` — synchronous HTTP client for testing; wraps the ASGI app, no server needed
  ```python
  from fastapi.testclient import TestClient
  client = TestClient(app)
  response = client.get("/items/1")
  ```
- `pytest` fixtures — `@pytest.fixture` for setup/teardown; `yield` fixtures run cleanup after the test
- Dependency overrides — `app.dependency_overrides` for mocking; replace any `Depends` target with a stub
  ```python
  app.dependency_overrides[get_current_user] = lambda: fake_user
  ```
- Testing different response codes and validation errors — assert `response.status_code` and inspect `response.json()`
- Testing WebSocket endpoints
  ```python
  with client.websocket_connect("/ws") as ws:
      ws.send_text("hello")
      assert ws.receive_text() == "Echo: hello"
  ```

## Exercises

### 1. Basic Endpoint Tests
Write tests for a CRUD API: test create (201), get (200), get missing (404), list with pagination. Use `TestClient`.

```python
def test_create_item():
    response = client.post("/items", json={"name": "widget", "price": 9.99})
    assert response.status_code == 201
    assert response.json()["name"] == "widget"

def test_get_missing_item():
    response = client.get("/items/999")
    assert response.status_code == 404
```

### 2. Validation Tests
Test that invalid request bodies return 422 with appropriate error details.

```python
def test_invalid_price():
    response = client.post("/items", json={"name": "widget", "price": -1})
    assert response.status_code == 422
    assert "price" in str(response.json())
```

### 3. Dependency Override
Override a `get_db` dependency to use an in-memory SQLite database. Override a `get_current_user` dependency to skip auth in tests.

```python
def override_get_db():
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
```

### 4. Test Fixtures
Create pytest fixtures for: app client, seeded database, authenticated client. Use fixture composition.

```python
@pytest.fixture
def client():
    ...

@pytest.fixture
def seeded_db(client):
    # create test data
    ...

@pytest.fixture
def auth_client(client):
    # client with auth header
    ...
```
