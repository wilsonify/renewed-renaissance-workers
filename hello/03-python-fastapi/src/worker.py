from app import app


async def on_fetch(request, env):
    import asgi
    return await asgi.fetch(app, request, env)


@app.get("/")
async def root():
    return {"message": "Hello, World!"}
