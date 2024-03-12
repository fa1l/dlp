from pydantic import RedisDsn
from pydantic_settings import BaseSettings


class CelerySettings(BaseSettings):
    broker_url: RedisDsn = "redis://127.0.0.1:6379"
    result_backend: RedisDsn = "redis://127.0.0.1:6379"

    _env_prefix = "CELERY_"
