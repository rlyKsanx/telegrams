from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def kb_menu():
    menu = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Profile", callback_data="profile")],
            [InlineKeyboardButton(text="Shop", callback_data="shop")],
            [InlineKeyboardButton(text="About", callback_data="about")],
        ]
    )
    return menu
