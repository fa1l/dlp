from .celery_app import app
from .web import fastapi_app

__all__ = ("app",)
