import logging
import asyncio
from TZ1_TZ2.handlers import register_handlers
from TZ1_TZ2.bot import bot, dp

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    try:
        register_handlers(dp)
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Ошибка запуска: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logger.error(f"Не запустился: {e}")
