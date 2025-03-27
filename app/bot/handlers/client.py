from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.keyboards.client import kb_menu

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("hello", reply_markup=kb_menu())
