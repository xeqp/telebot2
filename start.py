from aiogram import types, Dispatcher
from aiogram.filters import CommandStart

async def start_handler(message: types.Message):
    await message.answer("Отправь мне голосовое сообщение.")

def register_start_handler(dp: Dispatcher):
    dp.message.register(start_handler, CommandStart())
