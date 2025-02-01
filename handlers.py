import os
from aiogram import F, Router  #"F"-ЭТО фильтр
from aiogram.types import Message,CallbackQuery
from aiogram.filters import CommandStart,Command
from app.fff import Starts,Helps,Pomos,Products,Companys
import app.keyboard as kb



router = Router() #Router - нужно всегда указывать с (), без него не что не будет работа
#Нужна для того чтобы можно было писать дальше, так как Dispatcher только один
#ADMIN_ID = '5548530334'



@router.message(CommandStart())# CommandStart - мы только обрабатываем только команду старт
async def cmd_start(message:Message):
    #await message.answer_sticker('айди стикера')
    #answer_sticker - Добовляет стикер,нужен только айди стикера
    await message.answer_photo('https://static6.tgcnt.ru/posts/_0/0c/0c06bebd740b51820fc1ab68e86e4fb3.jpg')
    await message.answer(f"{message.from_user.first_name} , добро пожаловать в наш магазин “Сток-центре”")
    await message.answer(text=Starts,reply_markup=kb.main) # Отвечает без окна.----reply_markup=kb.main-Открыть когда я напишу Start
    #if message.from_user.id == os.getenv('ADMIN_ID'):
        #await message.answer(f'Вы попали ', reply_markup=admin.as_markup(resize_keyboard=True))
        #await message.reply(text=Starts)# Отвечает с окно


@router.message(Command('help'))
async def cmd_help(message:Message):
    await message.answer(text=Helps)

@router.message(F.text == 'Привет')
async def nice(message: Message):
    await message.answer_sticker('CAACAgIAAxkBAAEMArhnmPBsCNHWJTaO_B5es63DAYhTDAACVjEAAhGu0UmP8PtLlKOLsDYE')
    await message.answer_photo('https://static6.tgcnt.ru/posts/_0/0c/0c06bebd740b51820fc1ab68e86e4fb3.jpg')
    await message.answer(text=Pomos)

@router.message(Command('product'))
async  def cmd_help(message:Message):
    await message.answer(text=Products)




#----------------------------------------------------------------------------------------------------------------------#
#Если человек пишет в чат какую-то беребельду пример(ррвавапвап), то наш бот ответит ему "Я вас не понимаю!"

#@router.message(F.text == 'Админ-панель')
#async  def cmd_help(message:Message):
    #await message.answer(f'Вы вошли в админ-панель', reply_markup=admin_panel)

#----------------------------------------------------------------------------------------------------------------------#

# Каталог где у нас хранится про одежду
@router.message(F.text == 'Каталог 🛍️')
async def catalog(message: Message):
    await message.answer('Выберите из нашего каталога',reply_markup=kb.catalog)

@router.message(F.text == 'Компания 🏢')
async def catalog(message: Message):
    await message.answer(text=Companys)
    await message.answer(f'покупка у него @killerpri')

@router.message(F.text == 'Арсонтемент ')
async def catalog(message: Message):
    await message.answer(f'красаво')
    await message.answer(f'покупка у него @killerpri')

#----------------------------------------------------------------------------------------------------------------------#

@router.callback_query(F.data == 't-shirt')
async  def t_shirt(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию футболки', show_alert=True)
    await callback.message.answer('Вы выбрали категорию футболки')
@router.callback_query(F.data == 'sneakers')
async  def sneakers(callback: CallbackQuery):
    await callback.message.answer('Вы выбрали категорию кроссовки')














