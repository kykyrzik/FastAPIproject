from typing import Any
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator, Field


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file="./.env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )
    DB_HOST: str
    DB_USER: str
    DB_PORT: int
    DB_PASS: str
    DB_NAME: str
    DB_URL: str = Field(...)

    @field_validator('DB_URL')
    @classmethod
    def assemble_db_url(cls, v: str, values: Any) -> str:
        return v.format(DB_USER=values.data.get('DB_USER'),
                        DB_PASS=values.data.get('DB_PASS'),
                        DB_HOST=values.data.get('DB_HOST'),
                        DB_PORT=values.data.get('DB_PORT'),
                        DB_NAME=values.data.get('DB_NAME'))


@lru_cache(typed=True)
def load_settings() -> Settings:
    return Settings()  # type: ignore
