# Task 7: Background Tasks & WebSockets

## Objective
Not everything should block a response. Learn FastAPI's `BackgroundTasks` for fire-and-forget work, and `WebSocket` endpoints for bidirectional real-time communication.

## What to Learn
- `BackgroundTasks` — scheduling work after response; the task runs after the response is sent to the client
  ```python
  @app.post("/notify")
  def notify(bg: BackgroundTasks):
      bg.add_task(send_email, to="a@b.com")
      return {"status": "queued"}
  ```
- When to use background tasks vs a proper queue (Celery, etc.) — background tasks are in-process and lost on crash; use Celery/ARQ for durability or distributed work
- `WebSocket` — upgrade from HTTP, bidirectional messaging
  ```python
  @app.websocket("/ws")
  async def ws_endpoint(ws: WebSocket):
      await ws.accept()
  ```
- WebSocket lifecycle — connect (`accept`), receive (`receive_text`/`receive_json`), send (`send_text`/`send_json`), disconnect (handle `WebSocketDisconnect`)
- Connection managers for multi-client WebSocket apps — a class that maintains a list of active connections and broadcasts to all

## Exercises

### 1. Background Task
Create `POST /notifications` that accepts `email: str` and `message: str`. Return immediately with 202. In the background, write the notification to a log file.

```python
# POST /notifications  {"email": "a@b.com", "message": "hello"}
# -> 202 {"status": "queued"}
# (notification.log gets written in background)
```

### 2. Background Task with Dependency
Create a `write_audit_log` dependency that adds a background task to log every request's method and path. Apply it to multiple endpoints.

```python
# Any request -> audit.log gets: "GET /items at 2024-01-01T..."
```

### 3. Basic WebSocket
Create a WebSocket endpoint at `/ws`. Accept connection, echo back any received message prefixed with "Echo: ". Handle disconnect gracefully.

```python
# ws://localhost:8000/ws
# Send: "hello"
# Receive: "Echo: hello"
```

### 4. Chat Room
Create a `ConnectionManager` class that tracks active WebSocket connections. Implement `/ws/chat/{username}` that broadcasts messages to all connected clients.

```python
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket): ...
    def disconnect(self, websocket: WebSocket): ...
    async def broadcast(self, message: str): ...
```
