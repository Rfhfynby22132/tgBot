from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
#ReplyKeyboardMarkup - эта которая снизу гве водишь сообщение
#KeyboardButton - это под сообщение когда бот отвечает


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог 🛍️')],
                                     [KeyboardButton(text='Компания 🏢')],
                                     [KeyboardButton(text='О на 👤'),
                                      KeyboardButton(text='Сайт 🌐')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню')

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Футболка',callback_data='t-shirt')],
    [InlineKeyboardButton(text='Кроссовки',callback_data='sneakers')]])



















