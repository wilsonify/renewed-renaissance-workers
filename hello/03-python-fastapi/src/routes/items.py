from fastapi import FastAPI, Request

from app import app
from Item import Item

@app.post("/items/")
async def create_item(item: Item):
    return item


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}