from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class DBSettings(BaseSettings):
    url: PostgresDsn

    class Config:
        env_prefix = "DB_"
