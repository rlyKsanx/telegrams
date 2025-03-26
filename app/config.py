from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent


class ConfigTelegram(BaseModel):
    token: str = "TOKEN"
    admin_id: int = 123456789


class Settings(BaseSettings):
    db_url: str = "sqlite+aiosqlite:///./db.sqlite3"
    telegram: ConfigTelegram = ConfigTelegram()

    model_config = SettingsConfigDict(
        env_file_encoding="utf-8",
        env_file=ROOT_DIR / ".env",
        env_nested_delimiter="_",
        env_prefix="config_",
        case_sensitive=True,
    )


settings = Settings()
