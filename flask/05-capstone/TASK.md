# Task 5: Capstone — Web App

## Objective
Build a small, complete Flask web application. Focus on what Flask does well that FastAPI doesn't: server-rendered HTML, session-based auth, form handling.

## What to Learn
- When to choose Flask over FastAPI (and vice versa)
- Full request lifecycle in a production Flask app
- Bringing together: factory, blueprints, templates, database, forms

## Project: Bookmark Manager

Build a multi-user bookmark manager with:

1. **Auth** — Register/login/logout using Flask-Login and password hashing (werkzeug.security). Session-based, not JWT.
2. **Bookmarks** — CRUD for bookmarks (url, title, optional description, tags). Each user sees only their own.
3. **Tags** — Many-to-many relationship. Filter bookmarks by tag.
4. **Templates** — Server-rendered pages using Jinja2 with template inheritance. No JS framework.
5. **Search** — Simple search by title or URL substring.
6. **Structure** — Application factory, blueprints (`auth`, `bookmarks`), config classes, Flask-Migrate.

### Requirements
- SQLite backend
- At least 3 blueprints (auth, bookmarks, main)
- Flash messages for user feedback
- Custom 404 page
- Runs with `python run.py`

### Evaluation Criteria
- Clean project structure (factory, blueprints, models separated)
- Correct use of sessions and Flask-Login
- Working migrations
- Templates with inheritance, no logic duplication
- Explain in a comment at the top of `run.py`: one paragraph on when you'd pick Flask over FastAPI
