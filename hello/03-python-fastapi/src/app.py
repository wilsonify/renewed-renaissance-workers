from typing import Dict, Any

from fastapi import FastAPI, HTTPException, status
from fastapi import Request

from Item import Item
from routes.env import env_inner
from routes.items import create_item_inner, update_item_inner, read_item_inner, CREATE_ITEM_SUCCESS_RESPONSE, \
    ERROR_RESPONSES
from routes.root import root_inner

app = FastAPI(title="Items API", description="API for managing items", version="1.0.0")


@app.post(
    "/items/",
    response_model=Item,
    responses={200: CREATE_ITEM_SUCCESS_RESPONSE, **ERROR_RESPONSES},
    status_code=status.HTTP_201_CREATED,
)
async def create_item(item: Item) -> Item:
    """
    Create a new item.

    Args:
        item (Item): The item to create.

    Returns:
        ItemResponseModel: The created item.
    """
    try:
        created_item = await create_item_inner(item)
        return created_item
    except ValueError as e:
        raise HTTPException(status_code=400, detail="Invalid input")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Unexpected error")


@app.put("/items/{item_id}", responses=ERROR_RESPONSES)
async def update_item(item_id: str, item: Dict[str, Any]) -> Dict[str, Any]:
    """
    Update an existing item.

    Args:
        item_id (str): The ID of the item to update.
        item (Dict[str, Any]): Updated item details.

    Returns:
        Dict[str, Any]: The updated item details.
    """
    try:
        item_item = Item(**item)
        updated_item = await update_item_inner(item_id, item_item)
        return updated_item
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Unexpected error")


@app.get("/items/{item_id}", response_model=Item, responses=ERROR_RESPONSES)
async def read_item(item_id: str) -> Item:
    """
    Read an item's details.

    Args:
        item_id (str): The ID of the item to retrieve.

    Returns:
        ItemResponseModel: The item's details.
    """
    try:
        item = await read_item_inner(item_id)
        return item
    except ValueError as e:
        raise HTTPException(status_code=404, detail="Item not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Unexpected error")


@app.get("/env", responses=ERROR_RESPONSES)
async def env(req: Request) -> Dict[str, Any]:
    """
    Retrieve environment details.

    Returns:
        Dict[str, Any]: Environment details.
    """
    try:
        return await env_inner(req)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Unexpected error")


@app.get("/", responses=ERROR_RESPONSES)
async def root() -> Dict[str, Any]:
    """
    Root endpoint for the API.

    Returns:
        Dict[str, Any]: Root message or details.
    """
    try:
        return await root_inner()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Unexpected error")


if __name__ == "__main__":
    import uvicorn

    # Default host and port can be overridden by environment variables
    uvicorn.run(app, host="0.0.0.0", port=8000)
