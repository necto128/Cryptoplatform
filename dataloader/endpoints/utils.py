from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/ping")
def ping():
    return JSONResponse(content={"message": "ok"}, status_code=200)
