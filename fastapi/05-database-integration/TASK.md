# Task 5: Database Integration

## Objective
Connect FastAPI to a real database. Learn SQLAlchemy (or SQLModel) for ORM, session management via dependencies, and Alembic for schema migrations.

## What to Learn
- SQLAlchemy ORM — models, engine, sessionmaker
  ```python
  from sqlalchemy import create_engine, Column, Integer, String
  from sqlalchemy.orm import DeclarativeBase, sessionmaker

  engine = create_engine("sqlite:///./app.db")
  SessionLocal = sessionmaker(bind=engine)

  class Base(DeclarativeBase): pass
  class Item(Base):
      __tablename__ = "items"
      id = Column(Integer, primary_key=True)
      name = Column(String, nullable=False)
  ```
- SQLModel (optional) — Pydantic + SQLAlchemy fusion; one class serves as both ORM model and Pydantic schema
- Session dependency with `yield` — one session per request
  ```python
  def get_db():
      db = SessionLocal()
      try:
          yield db
      finally:
          db.close()
  ```
- Alembic — `init`, `revision --autogenerate`, `upgrade`; autogenerate compares your models to the current DB schema and writes migration scripts
- CRUD operations — Create, Read, Update, Delete patterns
  ```python
  db.add(item); db.commit(); db.refresh(item)   # create
  db.get(Item, id)                               # read by PK
  db.query(Item).filter(Item.name == x).first()  # filter
  db.delete(item); db.commit()                   # delete
  ```

## Exercises

### 1. Database Setup
Create a SQLite database with SQLAlchemy. Define an `Item` model with `id`, `name`, `price`, `description`. Create a `get_db` dependency that yields a session.

```python
# database.py — engine, SessionLocal, Base
# models.py — Item model
# dependencies.py — get_db
```

### 2. CRUD Functions
Write `create_item()`, `get_item()`, `get_items()`, `update_item()`, `delete_item()` in a `crud.py` module. Each takes a `Session` and appropriate params.

```python
# crud.create_item(db, name="widget", price=9.99)  -> Item
# crud.get_items(db, skip=0, limit=10)              -> list[Item]
```

### 3. Wire to Endpoints
Create endpoints that use the CRUD functions with the DB session dependency. Full CRUD:
- `POST /items` — create
- `GET /items` — list with pagination
- `GET /items/{id}` — get one (404 if missing)
- `PUT /items/{id}` — update
- `DELETE /items/{id}` — delete (204 No Content)

### 4. Alembic Setup
Initialize Alembic. Generate an initial migration. Add a `category` column to `Item`. Generate a second migration. Apply both.

```bash
alembic init alembic
alembic revision --autogenerate -m "create items table"
# add category column to model
alembic revision --autogenerate -m "add category to items"
alembic upgrade head
```
