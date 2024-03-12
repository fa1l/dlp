from pydantic import RedisDsn
from pydantic_settings import BaseSettings


class CelerySettings(BaseSettings):
    broker_url: RedisDsn
    result_backend: RedisDsn

    class Config:
        env_prefix = "CELERY_"
