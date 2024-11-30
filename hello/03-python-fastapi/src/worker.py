async def on_fetch(request, env):
    import asgi
    from app import app
    return await asgi.fetch(app, request, env)
