from aiogram import types
from proj2.bot_app.app import dp
from proj2.bot_app.services.BotService import BotService


@dp.message_handler(commands='read_one', state="*")
async def read_one(message: types.Message):
    response = BotService.get_random()
    await message.reply(response)
