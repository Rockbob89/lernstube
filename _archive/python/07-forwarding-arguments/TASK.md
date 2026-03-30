# Task 7: Forwarding Arguments in Decorators

## Objective
Write decorators that work with functions that take arguments.

## What to Learn

So far, our decorated functions took no arguments, so the wrapper didn't need any either. When the decorated function takes arguments, the wrapper must accept and forward them using `*args, **kwargs`.

```python
from functools import wraps

def log_call(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"Calling {fn.__name__}")
        return fn(*args, **kwargs)
    return wrapper

@log_call
def add(a, b):
    return a + b

add(2, 3)
# prints: Calling add
# returns: 5
```

`*args` collects positional arguments as a tuple, `**kwargs` collects keyword arguments as a dict. `fn(*args, **kwargs)` unpacks them back into the original call. This pattern makes the decorator work with *any* function signature.

You can also **inspect** `kwargs` inside the wrapper. Since `kwargs` is a regular dict, you can check keys and values before forwarding:

```python
from functools import wraps

def clamp(**limits):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for param, max_val in limits.items():
                if param in kwargs and kwargs[param] > max_val:
                    raise ValueError(f"{param} exceeds {max_val}")
            return fn(*args, **kwargs)
        return wrapper
    return decorator

@clamp(volume=100)
def play(track, volume):
    return f"Playing {track} at {volume}"

play(track="song.mp3", volume=80)   # → "Playing song.mp3 at 80"
play(track="song.mp3", volume=120)  # → ValueError: volume exceeds 100
```

## Exercise

### 1. `@validate_types(**type_kwargs)`
A decorator with arguments that checks keyword argument types at call time. For each kwarg passed to the decorated function, if a type was specified for it in `type_kwargs`, use `isinstance` to check. Raise `TypeError` with a message like `"Expected name to be <class 'str'>, got <class 'int'>"` if a kwarg doesn't match.

```python
@validate_types(name=str, age=int)
def register(name, age):
    return f"{name} is {age}"

register(name="Alice", age=30)        # → "Alice is 30"
register(name="Alice", age="thirty")  # → TypeError: Expected age to be <class 'int'>, got <class 'str'>
```
