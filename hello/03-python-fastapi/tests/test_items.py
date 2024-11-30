import pytest
from Item import Item
from routes.items import create_item_inner, update_item_inner, read_item_inner


@pytest.mark.asyncio
async def test_create_item_inner():
    """Test creating an item using create_item_inner."""
    item = Item(name="Test Item", price=50.0, description="A test item", tax=5.0)
    created_item = await create_item_inner(item)

    # Assertions
    assert created_item == item
    assert created_item.name == "Test Item"
    assert created_item.price == 50.0
    assert created_item.description == "A test item"
    assert created_item.tax == 5.0


@pytest.mark.asyncio
async def test_update_item_inner_without_query():
    """Test updating an item using update_item_inner without query parameters."""
    item = Item(name="Updated Item", price=100.0, description="Updated description", tax=10.0)
    item_id = 1

    updated_item = await update_item_inner(item_id, item)

    # Assertions
    assert updated_item["item_id"] == item_id
    assert updated_item["name"] == "Updated Item"
    assert updated_item["price"] == 100.0
    assert updated_item["description"] == "Updated description"
    assert updated_item["tax"] == 10.0


@pytest.mark.asyncio
async def test_update_item_inner_with_query():
    """Test updating an item using update_item_inner with query parameters."""
    item = Item(name="Updated Item", price=100.0, description="Updated description", tax=10.0)
    item_id = 1
    query = "sample-query"

    updated_item = await update_item_inner(item_id, item, query)

    # Assertions
    assert updated_item["item_id"] == item_id
    assert updated_item["name"] == "Updated Item"
    assert updated_item["price"] == 100.0
    assert updated_item["description"] == "Updated description"
    assert updated_item["tax"] == 10.0
    assert updated_item["q"] == query


@pytest.mark.asyncio
async def test_read_item_inner():
    """Test reading an item using read_item_inner."""
    item_id = 1

    item = await read_item_inner(item_id)

    # Assertions
    assert item["item_id"] == item_id
    assert isinstance(item, dict)
