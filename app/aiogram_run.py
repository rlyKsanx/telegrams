import logging
from aiohttp import web
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiogram.types import BotCommand, BotCommandScopeDefault

from config import bot, dp, settings, WEBHOOK_PATH
from handlers.client import router as client_router


async def set_commands():
    commands = [BotCommand(command="start", description="Старт")]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def on_startup() -> None:
    await set_commands()
    await bot.set_webhook(f"{settings.WEBHOOK_URL}{WEBHOOK_PATH}")
    await bot.send_message(chat_id=settings.ADMIN_ID, text="Бот запущен!")


async def on_shutdown() -> None:
    await bot.send_message(chat_id=settings.ADMIN_ID, text="Бот остановлен!")
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.session.close()


def main() -> None:
    logging.basicConfig(level=logging.INFO)

    dp.include_router(client_router)

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(dispatcher=dp, bot=bot)
    webhook_requests_handler.register(
        app,
        path=WEBHOOK_PATH,
    )
    setup_application(app, dp, bot=bot)
    web.run_app(app, host=settings.HOST, port=settings.PORT)


if __name__ == "__main__":
    main()
