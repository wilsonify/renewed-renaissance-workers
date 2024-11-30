from fastapi import Request


async def env_inner(req: Request):
    env = req.scope["env"]
    return {
        "message": "Here is an example of getting an environment variable: "
                   + env.MESSAGE
    }
