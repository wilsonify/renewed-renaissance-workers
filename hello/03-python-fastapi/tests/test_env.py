import pytest
from fastapi import Request
from unittest.mock import AsyncMock

from routes.env import env_inner


@pytest.mark.asyncio
async def test_env_inner():
    """Test the env_inner function."""
    # Mock the request object
    mock_request = AsyncMock(Request)
    mock_request.scope = {
        "env": type("Env", (), {"MESSAGE": "Hello, World!"})()  # Mocked environment variable
    }

    # Call the function
    response = await env_inner(mock_request)

    # Assertions
    assert response == {
        "message": "Here is an example of getting an environment variable: Hello, World!"
    }
