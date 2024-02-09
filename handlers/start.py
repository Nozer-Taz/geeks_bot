from aiogram import types, Dispatcher
from config import bot
from database import bot_db
from keyboards import start_inline_buttons


async def start_button(message: types.Message):
    print(message)
    db = bot_db.Database()
    db.sql_insert_user(
        tg_id=message.from_user.id,

    )

    await bot.send_message(
        chat_id=message.from_user.id,
        text=f'Hello {message.from_user.first_name}'
    )


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(
        start_button,
        commands=['start', ]
    )