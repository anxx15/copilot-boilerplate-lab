from fastapi import APIRouter

from app.schemas.example import HelloResponse
from app.services.example import get_welcome_message

router = APIRouter()


@router.get("/hello", response_model=HelloResponse)
async def read_hello() -> HelloResponse:
    return {"message": get_welcome_message()}
