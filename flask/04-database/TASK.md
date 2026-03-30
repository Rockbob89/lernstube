# Task 4: Database

## Objective
Integrate Flask-SQLAlchemy and Flask-Migrate to add persistent storage to a Flask app.

## What to Learn
- Flask-SQLAlchemy setup and `db.init_app(app)` pattern
  ```python
  from flask_sqlalchemy import SQLAlchemy
  db = SQLAlchemy()
  app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
  db.init_app(app)
  ```
- Model definition: columns, types, relationships, `__repr__`
  ```python
  class Item(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String(100), nullable=False)
      def __repr__(self): return f"<Item {self.name}>"
  ```
- Database migrations with Flask-Migrate (`flask db init/migrate/upgrade`) — generates versioned migration scripts from model diffs
- CRUD operations via SQLAlchemy ORM (add, query, filter, delete, commit)
  ```python
  db.session.add(item); db.session.commit()          # create
  Item.query.filter_by(name="x").first()             # read
  db.session.delete(item); db.session.commit()       # delete
  ```
- One-to-many relationships
  ```python
  class Category(db.Model):
      items = db.relationship("Item", backref="category")
  class Item(db.Model):
      category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
  ```

## Exercises

### 1. Model Definition
Create an `Item` model in `app/models.py`:
- `id` (Integer, primary key)
- `name` (String(100), not nullable)
- `description` (Text, nullable)
- `created_at` (DateTime, server default)

### 2. DB Setup
Configure SQLAlchemy with SQLite (`sqlite:///app.db`). Initialize Flask-Migrate. Run:
```
flask db init
flask db migrate -m "create items table"
flask db upgrade
```

### 3. CRUD Routes
Update the API blueprint to use the database instead of the in-memory list:

```
GET    /api/items       -> all items as JSON
POST   /api/items       -> create from JSON body, return 201
GET    /api/items/<id>  -> single item or 404
PUT    /api/items/<id>  -> update item
DELETE /api/items/<id>  -> delete, return 204
```

### 4. Relationships
Add a `Category` model. Each item belongs to one category. Update the Item model with a foreign key. Create a migration and test that items can be filtered by category.

```
GET /api/categories              -> list categories
GET /api/categories/<id>/items   -> items in category
```
