from fastapi import FastAPI

from app.api import router as api_router
from app.core.config import settings
from app.utils.logger import get_logger

logger = get_logger(__name__)


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name, debug=settings.debug)
    app.include_router(api_router)

    @app.on_event("startup")
    async def on_startup() -> None:
        logger.info("Starting %s", settings.app_name)

    @app.on_event("shutdown")
    async def on_shutdown() -> None:
        logger.info("Shutting down %s", settings.app_name)

    @app.get("/", tags=["Health"])
    async def root() -> dict[str, str]:
        return {"status": "ok", "app": settings.app_name}

    return app


app = create_app()
