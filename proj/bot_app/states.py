from aiogram.dispatcher.filters.state import State, StatesGroup


class GameStates(StatesGroup):
    start = State()
    random_one = State()
    all_words = State()
