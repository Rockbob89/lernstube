# Task 2: Templates & Static Files

## Objective
Use Jinja2 templates with inheritance and serve static assets.

## What to Learn
- `render_template` and the `templates/` directory convention
  ```python
  from flask import render_template
  return render_template("items.html", items=items)
  ```
- Jinja2 syntax: variables `{{ }}`, control `{% %}`, filters `{{ x|upper }}`
  ```jinja
  <p>{{ item.name|upper }}</p>
  {% for item in items %} ... {% endfor %}
  {% if items %} ... {% else %} No items {% endif %}
  ```
- Template inheritance: `{% block %}`, `{% extends %}`
  ```jinja
  {# base.html #}
  {% block content %}{% endblock %}

  {# child.html #}
  {% extends "base.html" %}
  {% block content %}<p>Hello</p>{% endblock %}
  ```
- Macros for reusable components
  ```jinja
  {% macro render_field(label, value) %}
  <div><strong>{{ label }}:</strong> {{ value }}</div>
  {% endmacro %}
  ```
- `static/` directory, `url_for('static', filename=...)` — Flask serves everything in `static/` at `/static/`
  ```jinja
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
  ```
- Flash messages with `flash()` and `get_flashed_messages()`
  ```python
  flash("Item created!")           # in the view
  ```
  ```jinja
  {% for msg in get_flashed_messages() %}<p>{{ msg }}</p>{% endfor %}
  ```

## Exercises

### 1. Base Template
Create a `templates/base.html` with a proper HTML skeleton, a `{% block title %}` and `{% block content %}`. Include a link to a CSS file via `url_for('static', ...)`.

### 2. Item List Page
Create a route `GET /items` that renders `templates/items.html` (extends base). Pass a list of dicts and render them in a `<ul>`. Show a message if the list is empty.

```
GET /items -> HTML page listing items
```

### 3. Item Form
Create `GET /items/new` rendering a form and `POST /items` handling submission. Use `flash()` to show a success message after creation. Redirect back to `/items`.

```
GET  /items/new  -> HTML form
POST /items      -> create item, flash message, redirect to /items
```

### 4. Template Macro
Create a macro in `templates/macros.html` called `render_field(label, value)` that outputs a styled `<div>` with a label and value. Use it in a detail page `GET /items/<id>`.

### 5. Static Assets
Add a `static/style.css` that styles the pages. Verify it loads correctly via the browser dev tools.
