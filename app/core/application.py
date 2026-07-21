from fastapi import FastAPI

from app.core.constants import (
    PROJECT_NAME,
    VERSION,
    API_PREFIX,
)

from app.api.v1.endpoints.health import router as health_router


def create_app() -> FastAPI:
    """
    Cria e configura a aplicação FastAPI.
    """

    app = FastAPI(
        title=PROJECT_NAME,
        version=VERSION,
    )

    app.include_router(
        health_router,
        prefix=API_PREFIX,
    )

    @app.get(
        "/",
        tags=["Root"],
    )
    def root():
        return {
            "project": PROJECT_NAME,
            "version": VERSION,
            "status": "running",
        }

    return app