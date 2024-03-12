from independency import Container
from fastapi import FastAPI
from .routes import router


def create_web_app(container: Container) -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    return app
