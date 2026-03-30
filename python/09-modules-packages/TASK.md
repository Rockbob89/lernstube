# Task 9: Modules & Packages

## Objective
Structure Python code into proper packages and modules.

## What to Learn
- Modules vs packages — a module is a `.py` file; a package is a directory with `__init__.py`
- `__init__.py` — runs when the package is imported; use it to expose the public API
  ```python
  # mypackage/__init__.py
  from mypackage.models import AppConfig   # re-export: consumers use `from mypackage import AppConfig`
  from mypackage.parser import load_config

  __all__ = ["AppConfig", "load_config"]  # controls `from mypackage import *`
  ```
- Relative vs absolute imports — relative uses `.` prefix, only valid inside a package
  ```python
  from mypackage.models import AppConfig   # absolute — works anywhere
  from .models import AppConfig            # relative — only inside mypackage/
  ```
- `if __name__ == "__main__"` — code that only runs when the file is executed directly, not when imported
- Entry points and `__main__.py` — `python -m mypackage` runs `mypackage/__main__.py`

## Exercise

Restructure the code from tasks 6 and 8 into a proper package:

```
python/09-modules-packages/
└── configlib/
    ├── __init__.py        # exports public API
    ├── __main__.py        # python -m configlib '{"host":"x","port":8080}'
    ├── models.py          # AppConfig dataclass
    ├── exceptions.py      # AppError, ValidationError, NotFoundError
    ├── parser.py          # load_config, parse_config
    └── utils.py           # Stack[T] from task 8
```

Requirements:
- `from configlib import AppConfig, load_config` must work
- `python -m configlib '{"host":"localhost","port":8080}'` prints the loaded config
- All imports use absolute imports within the package
- `__init__.py` only exposes the public API, not internals
