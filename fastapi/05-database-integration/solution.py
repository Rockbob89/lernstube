from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session, sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./items.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Item(Base):
    __tablename__ = "items"
    pass


Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    pass


@app.post("/items")
def create_item(db: Session = Depends(get_db)):
    pass


@app.get("/items")
def list_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    pass


@app.get("/items/{item_id}")
def get_item(item_id: int, db: Session = Depends(get_db)):
    pass


@app.put("/items/{item_id}")
def update_item(item_id: int, db: Session = Depends(get_db)):
    pass


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    pass
