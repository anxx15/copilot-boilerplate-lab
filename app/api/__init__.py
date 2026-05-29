from fastapi import APIRouter

from .routes import router as example_router

router = APIRouter()
router.include_router(example_router, prefix="/api", tags=["Example"])
