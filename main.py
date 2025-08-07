from aiogram import Bot, Dispatcher
from app.handlers import router
import asyncio
from app.database.models import async_main

import os


# Создаём бота
bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()


# Запуск бота
async def main():
    await async_main()
    dp.include_router(router)
    await dp.start_polling(bot)




if __name__ == "__main__":
    asyncio.run(main())
