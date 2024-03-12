from pydantic_settings import BaseSettings


class RedisRegexpSettings(BaseSettings):
    host: str
    port: int
    db: int

    class Config:
        env_prefix = "REDIS_REGEXP_"
