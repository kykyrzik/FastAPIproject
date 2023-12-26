from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


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
    DB_URL: str

    @property
    def db_url(self) -> str:
        return self.DB_URL.format(
            db_user=self.DB_USER,
            db_pass=self.DB_PASS,
            db_host=self.DB_HOST,
            db_port=self.DB_PORT,
            db_name=self.DB_NAME,
        )


class AuthJWT(BaseSettings):
    private_key_path: Path = Path(__file__).parent.parent.parent / "certs" / "private-key.pem"
    public_key_path: Path = Path(__file__).parent.parent.parent / "certs" / "public-key.pem"
    ALGORITHM: str = "RS256"


@lru_cache(typed=True)
def load_settings() -> Settings:
    return Settings()


@lru_cache(typed=True)
def load_auth_jwt() -> AuthJWT:
    return AuthJWT()
