import asyncio
from aiogram import Bot,Dispatcher
from app_1.handlers import router
from app.ff import TOKEN




async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
