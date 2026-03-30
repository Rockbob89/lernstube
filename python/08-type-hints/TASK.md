# Task 8: Type Hints & Tooling

## Objective
Add type safety to Python code using annotations and tooling.

## What to Learn
- Basic type annotations: `int`, `str`, `list[int]`, `dict[str, Any]`
- `Optional`, `Union`, `Literal` from `typing`
  ```python
  from typing import Optional, Union, Literal

  def greet(name: Optional[str] = None) -> str: ...  # Optional[X] == X | None
  def parse(val: Union[int, str]) -> str: ...         # accepts either type
  def set_mode(mode: Literal["r", "w", "a"]) -> None: ...  # only these values
  ```
- `@dataclass` — auto-generates `__init__`, `__repr__`, `__eq__` from annotated fields
  ```python
  from dataclasses import dataclass, field

  @dataclass
  class Point:
      x: float
      y: float
      tags: list[str] = field(default_factory=list)  # mutable default needs field()

  p = Point(1.0, 2.0)
  p  # Point(x=1.0, y=2.0, tags=[])
  ```
- `mypy` — static type checking
- When types help vs when they're noise

## Exercise

### 1. Refactor task 6 with dataclasses
Take your custom exceptions and `parse_config` from task 6. Create a `config.py`:

- Define a `@dataclass` called `AppConfig` with typed fields: `host: str`, `port: int`, `debug: bool = False`, `tags: list[str] = field(default_factory=list)`
- Write `load_config(data: dict) -> AppConfig` that validates and returns an `AppConfig` instance
- Use `@dataclass(frozen=True)` to make it immutable

### 2. Generic stack
Write a `Stack[T]` class using `typing.Generic`:

```python
s: Stack[int] = Stack()
s.push(1)
s.push(2)
s.peek()  # → 2
s.pop()   # → 2
s.is_empty()  # → False
```

Should pass `mypy --strict`.

### 3. Type-check everything
Run `mypy --strict` on both files. Fix all errors until it passes clean.
