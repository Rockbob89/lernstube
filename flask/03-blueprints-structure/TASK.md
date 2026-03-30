# Task 3: Blueprints & Structure

## Objective
Refactor a Flask app into a production-style layout using blueprints, an application factory, and configuration management.

## What to Learn
- Application factory pattern (`create_app()`) — creating the app inside a function avoids circular imports and allows multiple configs
  ```python
  def create_app(config_name="dev"):
      app = Flask(__name__)
      app.config.from_object(config_map[config_name])
      return app
  ```
- `Blueprint` registration, URL prefixes, nested templates
  ```python
  api = Blueprint("api", __name__, url_prefix="/api")

  @api.route("/items")
  def list_items(): ...

  app.register_blueprint(api)
  ```
- Configuration via classes (`Config`, `DevConfig`, `ProdConfig`)
  ```python
  class Config:
      SECRET_KEY = "changeme"
  class DevConfig(Config):
      DEBUG = True
  ```
- `current_app` and `g` proxies — `current_app` is the active app; `g` is a request-scoped namespace for storing data (e.g. DB connections)
  ```python
  from flask import current_app, g
  current_app.config["SECRET_KEY"]
  g.user = load_user()
  ```
- Extension initialization pattern (init_app) — extensions accept the app later to support the factory pattern
  ```python
  db = SQLAlchemy()   # top-level, no app
  def create_app():
      app = Flask(__name__)
      db.init_app(app)  # bound here
  ```

## Exercises

### 1. Application Factory
Create a `create_app(config_name="dev")` function in `app/__init__.py`. It should:
- Create the Flask instance
- Load config from a config class based on `config_name`
- Register blueprints
- Return the app

### 2. Config Classes
Create `app/config.py` with `Config`, `DevConfig`, `ProdConfig` classes. At minimum: `SECRET_KEY`, `DEBUG`, `TESTING`.

### 3. Blueprints
Split routes into two blueprints:
- `main` (prefix `/`): index page
- `api` (prefix `/api`): JSON item CRUD from task 1

Register both in the factory.

### 4. Project Layout
Final structure should be:
```
03-blueprints-structure/
├── run.py              # entry point: from app import create_app; create_app().run()
├── app/
│   ├── __init__.py     # create_app factory
│   ├── config.py       # config classes
│   ├── main/
│   │   ├── __init__.py # main blueprint
│   │   └── routes.py
│   └── api/
│       ├── __init__.py # api blueprint
│       └── routes.py
```

Verify it runs with `python run.py`.
