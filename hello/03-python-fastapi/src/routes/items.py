from Item import Item


async def create_item_inner(item: Item) -> Item:
    return item


async def update_item_inner(item_id: str, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result


async def read_item_inner(item_id: str):
    return {"item_id": item_id}


CREATE_ITEM_SUCCESS_RESPONSE = {
    "description": "Item successfully created",
    "content": {
        "application/json": {
            "example": {
                "name": "item01-name",
                "price": 32.00,
                "description": "This is the first item",
                "tax": 2.00,
            }
        }
    },
}
ERROR_RESPONSES = {
    400: {
        "description": "Bad Request",
        "content": {
            "application/json": {"example": {"detail": "Invalid input"}}
        },
    },
    500: {
        "description": "Internal Server Error",
        "content": {
            "application/json": {"example": {"detail": "Unexpected error"}}
        },
    },
}
