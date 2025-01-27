from aiogram import F, Router  #"F"-ЭТО фильтр
from aiogram.types import Message,CallbackQuery
from aiogram.filters import CommandStart,Command
from app.fff import Starts,Helps,Pomos,Products,Companys
import app.keyboard as kb

router = Router() #Router - нужно всегда указывать с (), без него не что не будет работать



@router.message(CommandStart())# CommandStart - мы только обрабатываем только команду старт
async def cmd_start(message: Message):
    await message.answer(f"{message.from_user.first_name},добро пожаловать в наш магазин Сток-центре",text=Starts,reply_markup=kb.main)# Отвечает без окна.----reply_markup=kb.main-Открыть когда я напишу Start
    #await message.reply(text=Starts)# Отвечает с окном

@router.message(Command('help'))
async  def cmd_help(message:Message):
    await message.answer(text=Helps)

@router.message(F.text == 'Привет')
async def nice(message: Message):
    await message.answer(text=Pomos)

@router.message(Command('product'))
async  def cmd_help(message:Message):
    await message.answer(text=Products)


# Каталог где у нас хранится про одежду
@router.message(F.text == 'Каталог 🛍️')
async def catalog(message: Message):
    await message.answer('Выберите из нашего каталога',reply_markup=kb.catalog)

@router.message(F.text == 'Компания 🏢')
async def catalog(message: Message):
    await message.answer(text=Companys)


@router.callback_query(F.data == 't-shirt')
async  def t_shirt(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию футболки', show_alert=True)
    await callback.message.answer('Вы выбрали категорию футболки')
@router.callback_query(F.data == 'sneakers')
async  def sneakers(callback: CallbackQuery):
    await callback.message.answer('Вы выбрали категорию кроссовки')