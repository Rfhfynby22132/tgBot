from aiogram import F,Router
from aiogram.types import Message
from aiogram.filters import CommandStart,Command
from app.fff import STARTS, HELPS
from app.ff import FOTO
import app_1.keyboard as kb


router = Router()

@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer_photo(FOTO)
    await message.answer(text=STARTS,reply_markup=kb.main)
@router.message(Command('help'))
async def cmd_help(message:Message):
    await message.answer(text=HELPS)


@router.message(F.text =='👟 Каталог')
async def catalog(message:Message):
    await message.answer('Выберите из нашего каталога',reply_markup=kb.shop)

@router.message(F.text == '📞 Поддержка')
async def sos(message:Message):
    await message.answer('Вы обратились в службу поддержки📞, чем я могу помочь из преведенных ниже проблемы\n\n'
                         '1)Не появляется ссылка на товар?\n'
                         '2)Не можете найти то,что нету в нашем магазине?\n'
                         '3)Не можете оплатить\n'
                         '4)Нужна помощь админа пишите сюда @killerpri')

#----------------------------------------------------------------------------------------------------------------------#









#----------------------------------------------------------------------------------------------------------------------#
#Кроссовки бренды: Nike ✅,Adidas ☰,Puma 🐆,Reebok 🔷 и кнопка Назад ⬅️
@router.message(F.text == 'Кроссовки')
async def catalog(message: Message):
    await message.answer('Вот все наши модели!',reply_markup=kb.catalog)

@router.message(F.text == 'Носки')
async def catalog(message: Message):
    await message.answer('Вот все наши модели!',reply_markup=kb.socks)

@router.message(F.text == 'Одежда')
async def catalog(message: Message):
    await message.answer('Вот все наши модели!')
#----------------------------------------------------------------------------------------------------------------------#
@router.message(F.text == 'Назад ⬅')
async def catalog(message:Message):
    await message.answer('Вот все наши модели!',reply_markup=kb.main)



@router.message(F.text == 'Nike ✅')
async def shop(message: Message):
    await message.answer(
'Модели:\n' 
    '1)  Nike Revolution\n'
    '2)  Nike Downshifter\n'
    '3)  Nike Court Vision\n'
    '4)  Nike Tanjun\n'
    'Выберите цифру какие вам кроссовки понравилось!',reply_markup=kb.NIKE)

@router.message(F.text == 'Adidas ☰')
async def shop(message:Message):
    await message.answer(
    'Модели:\n'
    '1) Adidas Runfalcon\n'
    '2) Adidas Duramo\n'
    '3) Adidas Grand Court\n'
    '4) Adidas Lite Racer\n'
    'Выберите цифру какие вам кроссовки понравилось!',reply_markup=kb.ADIDAS)


@router.message(F.text == 'Puma 🐆')
async def shop(message:Message):
    await message.answer(''
          'Модели:\n'
    '1) Puma Rebound\n'
    '2) Puma Carina\n'
    '3) Puma Flyer Runner\n'
    '4) Puma ST Runner\n'
    'Выберите цифру какие вам кроссовки понравилось!',reply_markup=kb.PUMA)

@router.message(F.text == 'Reebok 🔷')
async def shop(message:Message):
    await message.answer(
    'Модели:\n'
    '1) Reebok Royal Glide\n'
    '2) Reebok Lite Plus\n'
    '3) Reebok Energylux\n'
    '4) Reebok Rush Runner\n'
    'Выберите цифру какие вам кроссовки понравилось!',reply_markup=kb.REEBOK)

@router.message(F.text == 'Назад ⬅️')
async def main(message:Message):
    await message.answer('Вы находитесь в каталоге',reply_markup=kb.shop)
#----------------------------------------------------------------------------------------------------------------------#
#Магазин Носков

@router.message(F.text == 'Nike ✅')
async def socks(message:Message):
    await message.answer(
        'Модели:\n'
            '1) Nike Everyday Plus Cushioned Crew Socks'
            '2) Nike Everyday Lightweight Crew Socks'
            '3) Nike Everyday Lightweight No-Show Socks'
            '4) Nike Dri-FIT Cushion Crew Training Socks'
            'Выберите цифру какие вам носки понравилось!',reply_markup=kb.soNike)



@router.message(F.text == 'Adidas ☰')
async def socks(message:Message):
    await message.answer(
        'Модели:\n'
            '1) Adidas Cushioned Ankle Socks '
            '2) Adidas Cushioned Crew Socks '
            '3) Adidas Cushioned Quarter Socks '
            '4) Adidas Training Ankle Socks'
            'Выберите цифру какие вам носки понравилось!',reply_markup=kb.soAdidas)




@router.message(F.text == 'Puma 🐆')
async def socks(message:Message):
    await message.answer(
        'Модели:\n'
            '1) Puma Sneaker Plain 3P'
            '2) Puma Quarter Plain 3P'
            '3) Puma Liga Core Socks '
            '4) Puma Invisible Sneaker Socks '
            'Выберите цифру какие вам носки понравилось!',reply_markup=kb.soPuma)



@router.message(F.text == 'Fila ⭐')
async def socks(message:Message):
    await message.answer(
        'Модели:\n'
            '1) Fila Crew Socks'
            '2) Fila Ankle Socks'
            '3) Fila Sport Socks'
            '4) Fila Performance Socks'
            'Выберите цифру какие вам носки понравилось!',reply_markup=kb.soFila)


@router.message(F.text == 'Назад ⬅️')
async def main(message:Message):
    await message.answer('Вы находитесь в каталоге',reply_markup=kb.shop)








