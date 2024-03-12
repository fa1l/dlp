from pydantic_settings import BaseSettings


class RedisRegexpSettings(BaseSettings):
    host: str = "127.0.0.1"
    port: int = 6379
    db: int = 1

    _env_prefix = "REDIS_REGEXP_"
