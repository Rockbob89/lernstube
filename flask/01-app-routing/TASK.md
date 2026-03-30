# Task 1: App & Routing

## Objective
Create a Flask application with multiple routes, HTTP methods, and request/response handling.

## What to Learn
- Flask application object and dev server
  ```python
  from flask import Flask
  app = Flask(__name__)
  app.run(debug=True)          # or: flask --app main run
  ```
- Route decorators, URL rules, variable rules (`<int:id>`, `<string:name>`)
  ```python
  @app.route("/items/<int:id>")
  def get_item(id): ...
  ```
- HTTP methods (GET, POST, PUT, DELETE) via `methods=` parameter
  ```python
  @app.route("/items", methods=["GET", "POST"])
  def items(): ...
  ```
- `request` object: args, form, json, headers
  ```python
  from flask import request
  q = request.args.get("q")        # query param
  data = request.get_json()        # JSON body
  ```
- `Response`, `jsonify`, `make_response`, status codes
  ```python
  return jsonify({"id": 1}), 201
  resp = make_response(jsonify(...), 204)
  ```
- `url_for` for reverse URL building
  ```python
  from flask import url_for
  url_for("get_item", id=1)   # -> "/items/1"
  ```
- Error handlers (`@app.errorhandler`)
  ```python
  @app.errorhandler(404)
  def not_found(e):
      return jsonify({"error": "not found"}), 404
  ```

## Exercises

### 1. Hello App
Create a minimal Flask app with a `/` route returning `"Hello, Flask!"`.

```
GET / -> "Hello, Flask!"
```

### 2. Route Parameters
Create routes that accept variable URL segments.

```
GET /greet/sergio       -> "Hello, sergio!"
GET /square/5           -> "25"
GET /square/notanumber  -> 404
```

### 3. JSON API Routes
Build a simple in-memory item store (list of dicts). Implement CRUD routes returning JSON.

```
GET    /api/items          -> [{"id": 1, "name": "..."}, ...]
POST   /api/items           -> creates item from JSON body, returns 201
GET    /api/items/<id>      -> single item or 404
DELETE /api/items/<id>      -> 204 or 404
```

### 4. Request Inspection
Create a `/debug` route that returns a JSON object with: method, all query params, all headers, and the raw body (if any).

```
GET /debug?foo=bar -> {"method": "GET", "args": {"foo": "bar"}, "headers": {...}, "body": ""}
```

### 5. Error Handlers
Register custom error handlers for 404 and 500 that return JSON responses instead of HTML.

```
GET /nonexistent -> {"error": "not found"}, 404
```
