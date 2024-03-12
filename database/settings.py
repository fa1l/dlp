from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class DBSettings(BaseSettings):
    url: PostgresDsn = "postgresql://postgres:postgres@localhost:5432/dlp"

    _env_prefix = "DB_"
