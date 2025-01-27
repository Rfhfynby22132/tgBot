import asyncio
from aiogram import Bot,Dispatcher
from app.handlers import router
from app.database.medels import async_main

async def main():
    bot = Bot("7771898758:AAGi0cU60t1LhGyb8Cpm3uUke5Sfg6Q5vKw")
    dp = Dispatcher()
    dp.include_router(router)# добавляем router в Dispatcher чтобы он мог знать
    await dp.start_polling(bot)
    await async_main()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')