import os
from functools import lru_cache

from pydantic import BaseModel


class Settings(BaseModel):
    app_env: str = os.getenv("APP_ENV", "production")
    database_url: str = os.getenv(
        "DATABASE_URL", "postgresql+asyncpg://app:app@db:5432/app_db"
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
