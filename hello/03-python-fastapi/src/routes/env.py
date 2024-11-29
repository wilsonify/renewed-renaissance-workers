from fastapi import FastAPI, Request

from app import app
from Item import Item
@app.get("/env")
async def env(req: Request):
    env = req.scope["env"]
    return {
        "message": "Here is an example of getting an environment variable: "
                   + env.MESSAGE
    }