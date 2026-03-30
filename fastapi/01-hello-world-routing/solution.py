from fastapi import Body, FastAPI

app = FastAPI()

items = []


@app.get("/")
def root():
    pass


@app.get("/items/latest")
def get_latest_item():
    pass


@app.get("/items/{item_id}")
def get_item(item_id: int):
    pass


@app.get("/items")
def list_items(skip: int = 0, limit: int = 10):
    pass


@app.post("/items")
def create_item(name: str = Body(), price: float = Body()):
    pass


# Run: uvicorn solution:app --reload
