import asyncio
import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from routers.router import api_router
from services.socket_service import crypto_websocket

load_dotenv()
app = FastAPI()
app.include_router(api_router)


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(crypto_websocket())


if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("HOST"), port=int(os.getenv("PORT")))
