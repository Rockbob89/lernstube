# Task 9: Capstone -- REST API

## Objective
Build a complete, production-shaped REST API combining everything from tasks 1-8. This is the kind of service you'd deploy behind a reverse proxy in a Kubernetes cluster.

## Requirements

Build a **Task Manager API** (yes, a todo app -- but done properly).

### Models
- **User**: id, username, email, hashed_password, role (admin/user)
- **Task**: id, title, description, status (todo/in_progress/done), priority (low/medium/high), owner_id, created_at, updated_at

### Endpoints
- `POST /auth/register` — create user
- `POST /auth/token` — login, return JWT
- `GET /users/me` — current user profile
- `POST /tasks` — create task (authenticated)
- `GET /tasks` — list own tasks with filtering (status, priority) and pagination
- `GET /tasks/{id}` — get task (own only, or any if admin)
- `PUT /tasks/{id}` — update task (own only)
- `DELETE /tasks/{id}` — delete task (own only, or any if admin)

### Technical Requirements
1. **Pydantic models** for all request/response schemas
2. **SQLite + SQLAlchemy** for persistence
3. **JWT auth** with password hashing
4. **Dependency injection** for DB sessions and auth
5. **Background task** — log task status changes to a file
6. **Middleware** — request timing header
7. **Custom exception handlers** — consistent error responses
8. **Tests** — at least 10 tests covering CRUD, auth, permissions, validation

### Project Structure
```
09-capstone/
    main.py          # FastAPI app, middleware, exception handlers
    models.py        # SQLAlchemy models
    schemas.py       # Pydantic models
    crud.py          # Database operations
    auth.py          # JWT + password utilities
    dependencies.py  # get_db, get_current_user
    tests/
        conftest.py  # fixtures
        test_auth.py
        test_tasks.py
```

## Evaluation Criteria
- All endpoints functional
- Auth works correctly (can't access others' tasks)
- Validation returns proper 422 errors
- At least 10 passing tests
- Clean separation of concerns
- Runnable with `uvicorn main:app`
