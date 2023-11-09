import secrets
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )
    DB_HOST: str
    DB_USER: str
    DB_PORT: int
    DB_URL: str
    DB_PASS: str
    DB_NAME: str

    SECRECT_KEY: str = secrets.token_hex(32)

    @property
    def get_db(self) -> str:
        return self.DB_URL.format(
            DB_USER=self.DB_USER,
            DB_PASS=self.DB_PASS,
            DB_HOST=self.DB_HOST,
            DB_PORT=self.DB_PORT,
            DB_NAME=self.DB_NAME,
        )


@lru_cache(typed=True)
def load_settings() -> Settings:
    return Settings()
