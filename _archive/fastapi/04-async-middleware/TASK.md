# Task 4: Async & Middleware

## Objective
FastAPI is async-first. Understand when to use `async def` vs `def`, how middleware works, CORS configuration, and custom exception handlers.

## What to Learn
- `async def` vs `def` — use `async def` when awaiting I/O (DB, HTTP); use `def` for CPU-bound work (FastAPI runs sync handlers in a thread pool)
- ASGI middleware stack — each middleware wraps `call_next`; runs before/after every request in registration order
- `@app.middleware("http")` — custom middleware
  ```python
  @app.middleware("http")
  async def my_middleware(request: Request, call_next):
      response = await call_next(request)
      return response
  ```
- `CORSMiddleware` — cross-origin configuration
  ```python
  from fastapi.middleware.cors import CORSMiddleware
  app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:3000"],
                     allow_credentials=True, allow_methods=["*"])
  ```
- `@app.exception_handler()` — custom error responses
  ```python
  @app.exception_handler(MyError)
  async def my_handler(request, exc):
      return JSONResponse(status_code=400, content={"detail": str(exc)})
  ```
- `HTTPException` — raising errors with status codes
  ```python
  raise HTTPException(status_code=404, detail="Not found")
  ```

## Exercises

### 1. Async Endpoint
Create an async endpoint that simulates a slow I/O call with `asyncio.sleep(0.1)`. Compare with a sync endpoint. Both return timing info.

```python
# GET /async-demo  -> {"elapsed": 0.1, "type": "async"}
# GET /sync-demo   -> {"elapsed": 0.1, "type": "sync"}
```

### 2. Timing Middleware
Add middleware that measures request processing time and adds it as an `X-Process-Time` response header.

```python
@app.middleware("http")
async def add_process_time_header(request, call_next):
    # measure time, add header
    pass
```

### 3. CORS
Configure `CORSMiddleware` to allow requests from `http://localhost:3000` only, with GET and POST methods, and credentials. Verify by checking the response headers on a preflight OPTIONS request.

```python
# OPTIONS /items with Origin: http://localhost:3000
# -> access-control-allow-origin: http://localhost:3000
# -> access-control-allow-credentials: true
```

### 4. Custom Exception Handler
Define a custom `ItemNotFoundError(Exception)`. Add an exception handler that returns a 404 with `{"detail": "Item not found", "item_id": id}`. Use it in an endpoint.

```python
# GET /items/999  -> 404 {"detail": "Item not found", "item_id": 999}
```
