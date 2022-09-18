from aiogram import types
from proj2.bot_app import messages
from proj2.bot_app.app import dp


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(messages.WELCOME_MESSAGE)
