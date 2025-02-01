import asyncio
from aiogram import Bot,Dispatcher
from app.handlers import router



async def main():
    bot = Bot(ТОКЕН ВАШ)
    dp = Dispatcher()
    dp.include_router(router)# добавляем router в Dispatcher чтобы он мог знать
    await dp.start_polling(bot)



if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
