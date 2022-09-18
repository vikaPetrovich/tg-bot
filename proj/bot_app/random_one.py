from aiogram.dispatcher import FSMContext
from aiogram import types
from .app import dp
from .data_fetcher import get_random
from .states import GameStates


@dp.message_handler(commands='read_one', state="*")
async def read_one(message: types.Message, state: FSMContext):
    await GameStates.random_one.set()
    res = await get_random()
    async with state.proxy() as data:
        data['step'] = 1
        data['text'] = res.get('text')

        await message.reply(f"{data['text']}")
