from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from aiogram import Bot, Dispatcher


ROOT_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMIN_ID: int

    WEBHOOK_URL: str
    HOST: str
    PORT: int

    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        env_nested_delimiter="_",
    )


settings = Settings()

WEBHOOK_PATH = f"/{settings.BOT_TOKEN}"
bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()
