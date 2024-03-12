from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class DBSettings(BaseSettings):
    url: PostgresDsn

    _env_prefix = "DB_"
