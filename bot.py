import asyncio
import logging
from aiogram import Bot, Dispatcher
from TZ1_TZ2.settings import settings
from TZ1_TZ2.handlers import register_handlers

bot = Bot(settings.BOT_TOKEN)
dp = Dispatcher()

async def main():
    try:
        register_handlers(dp)
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Ошибка запуска: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logging.error(f"Ошибка при старте бота: {e}")
