from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

items_db: dict[int, dict] = {}
next_id = 1


class ItemCreate(BaseModel):
    pass


class ItemResponse(BaseModel):
    pass


class ItemUpdate(BaseModel):
    pass


class Category(BaseModel):
    pass


@app.post("/items", response_model=ItemResponse)
def create_item(item: ItemCreate):
    pass


@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    pass


@app.patch("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemUpdate):
    pass


@app.get("/categories/{name}", response_model=Category)
def get_category(name: str):
    pass
