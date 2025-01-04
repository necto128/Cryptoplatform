from fastapi import APIRouter

from endpoints import utils

api_router = APIRouter()
api_router.include_router(utils.router, prefix="/utils", tags=["Utilities"])
