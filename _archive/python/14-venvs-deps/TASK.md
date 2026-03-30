# Task 14: Virtual Environments & Dependency Management

## Objective
Manage Python environments and dependencies properly.

## What to Learn
- `venv` — creating, activating, deactivating
- `pip` — install, freeze, requirements.txt
- `pyproject.toml` — modern project metadata and dependencies; replaces `setup.py`/`setup.cfg`
  ```toml
  [project]
  name = "mypackage"
  version = "0.1.0"
  requires-python = ">=3.11"
  dependencies = ["requests>=2.28"]

  [project.optional-dependencies]
  dev = ["pytest", "mypy"]

  [project.scripts]
  mycli = "mypackage.__main__:main"   # creates a shell command on install

  [build-system]
  requires = ["hatchling"]
  build-backend = "hatchling.build"
  ```
- `uv` — fast Python package manager (Rust-based pip replacement); same commands as pip but faster; `uv pip install -e .`, `uv venv`
- When to use what

## Exercise

### 1. Package `configlib`
Turn your task 9 package into a proper installable project:

```
python/11-venvs-deps/
├── pyproject.toml
├── src/
│   └── configlib/
│       ├── __init__.py
│       ├── __main__.py
│       ├── models.py
│       ├── exceptions.py
│       ├── parser.py
│       └── utils.py
└── tests/
    ├── conftest.py
    ├── test_models.py
    ├── test_parser.py
    ├── test_exceptions.py
    └── test_stack.py
```

### 2. `pyproject.toml`
- Use `hatchling` or `setuptools` as build backend
- Define project metadata (name, version, description, python version)
- Add `pytest` and `mypy` as dev dependencies
- Define a console script entry point: `configlib = configlib.__main__:main`

### 3. Install & verify
- Create a venv
- Install the package in editable mode (`pip install -e .`)
- Run `configlib '{"host":"x","port":8080}'` from anywhere
- Run `pytest` and `mypy` from the project root
- Try the same with `uv` instead of pip
