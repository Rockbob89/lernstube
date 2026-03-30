import pytest
from fastapi import FastAPI, Depends, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field


# --- App under test ---
app = FastAPI()


class ItemCreate(BaseModel):
    name: str
    price: float = Field(gt=0)


items_db: dict[int, dict] = {}
next_id = 1


def get_db():
    return items_db


@app.post("/items", status_code=201)
def create_item(item: ItemCreate, db=Depends(get_db)):
    pass


@app.get("/items/{item_id}")
def get_item(item_id: int, db=Depends(get_db)):
    pass


@app.get("/items")
def list_items(skip: int = 0, limit: int = 10, db=Depends(get_db)):
    pass


# --- Tests ---
client = TestClient(app)


def test_create_item():
    pass


def test_get_missing_item():
    pass


def test_invalid_price():
    pass


def test_list_items_pagination():
    pass


# Run: pytest solution.py -v
