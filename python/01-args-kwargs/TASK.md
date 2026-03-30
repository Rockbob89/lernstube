# Task 1: Args & Kwargs

## Objective
Understand how Python handles function arguments beyond simple positional parameters.

## What to Learn
- Positional vs keyword arguments
- Default values
- `*args` — capture variable positional arguments as a tuple
- `**kwargs` — capture variable keyword arguments as a dict
- Argument order: `def f(pos, /, pos_or_kw, *, kw_only, **kwargs)`
- Unpacking: calling with `*list` and `**dict`

## Exercise

Create a file `solution.py` with the following functions:

### 1. `make_tag(tag, *children, **attrs)`
Builds an HTML tag string.

```python
make_tag("div", "hello", "world", class_="container", id="main")
# → '<div class="container" id="main">hello world</div>'
```

- `tag`: the HTML tag name
- `*children`: any number of child strings, joined with a space
- `**attrs`: HTML attributes. Note: trailing underscores in keys (like `class_`) should be stripped (because `class` is a Python reserved word)
- If no children: self-closing tag → `<br class="foo" />`

### 2. `merge_configs(*configs, **overrides)`
Merges multiple config dicts left-to-right, then applies overrides.

```python
merge_configs({"a": 1}, {"b": 2, "a": 3}, c=4)
# → {"a": 3, "b": 2, "c": 4}
```

### 3. `call_with_matching_args(func, **kwargs)`
Calls `func` with only the kwargs that match its signature. Discard the rest silently.

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

call_with_matching_args(greet, name="Alice", greeting="Hi", age=30)
# → "Hi, Alice!"
```

Hint: look at `inspect.signature`.

## File Structure
```
python/01-args-kwargs/
├── TASK.md        ← you are here
└── solution.py    ← create this
```
