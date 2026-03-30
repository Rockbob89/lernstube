import asyncio
import time

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()


class ItemNotFoundError(Exception):
    def __init__(self, item_id: int):
        self.item_id = item_id


@app.exception_handler(ItemNotFoundError)
async def item_not_found_handler(request: Request, exc: ItemNotFoundError):
    pass


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    pass


@app.get("/async-demo")
async def async_demo():
    pass


@app.get("/sync-demo")
def sync_demo():
    pass


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    pass
