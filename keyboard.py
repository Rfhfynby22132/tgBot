from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton



main = ReplyKeyboardMarkup(keyboard=[
                           [KeyboardButton(text='👟 Каталог'),
                            KeyboardButton(text='🔎 Поиск')],
                           [KeyboardButton(text='📞 Поддержка')]],
                    resize_keyboard=True,
                    input_field_placeholder='Выберите пункт меню')

#----------------------------------------------------------------------------------------------------------------------#
# Магазин кроссовок, носков и одежд

shop = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Кроссовки'),
     KeyboardButton(text='Носки')],
    [KeyboardButton(text='Назад ⬅')]],
    resize_keyboard=True,)
#----------------------------------------------------------------------------------------------------------------------#
#Магазин кроссовок

catalog = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Nike ✅'),
         KeyboardButton(text='Adidas ☰')],
        [KeyboardButton(text='Puma 🐆'),
         KeyboardButton(text='Reebok 🔷')],
        [KeyboardButton(text='Назад ⬅️')]],
        resize_keyboard=True,)


NIKE = InlineKeyboardMarkup(inline_keyboard=[
       [InlineKeyboardButton(text='1',url='https://www.ozon.ru/category/nike-revolution/'),
       InlineKeyboardButton(text='2',url='https://www.ozon.ru/category/nike-downshifter/')],
       [InlineKeyboardButton(text='3',url='https://www.ozon.ru/category/nike-court-vision/'),
       InlineKeyboardButton(text='4',url='https://www.ozon.ru/category/krossovki-muzhskie-nike-tanjun/')]])

ADIDAS = InlineKeyboardMarkup(inline_keyboard=[
       [InlineKeyboardButton(text='1',url='https://www.ozon.ru/category/krossovki-muzhskie-adidas-runfalcon/'),
       InlineKeyboardButton(text='2',url='https://www.ozon.ru/category/adidas-duramo-sl/')],
       [InlineKeyboardButton(text='3',url='https://www.ozon.ru/category/kedy-adidas-grand-court-muzhskie/'),
       InlineKeyboardButton(text='4',url='https://www.ozon.ru/category/adidas-lite-racer/')]])


PUMA = InlineKeyboardMarkup(inline_keyboard=[
       [InlineKeyboardButton(text='1',url='https://www.ozon.ru/category/puma-rebound/'),
       InlineKeyboardButton(text='2',url='https://www.ozon.ru/category/puma-carina/')],
       [InlineKeyboardButton(text='3',url='https://www.ozon.ru/category/puma-flyer-runner-muzhskie/'),
       InlineKeyboardButton(text='4',url='https://www.ozon.ru/product/krossovki-puma-st-runner-v2-1666345031/?utm_medium=organic&utm_source=yandex_serp_products')]])


REEBOK = InlineKeyboardMarkup(inline_keyboard=[
       [InlineKeyboardButton(text='1',url='https://www.ozon.ru/category/krossovki-muzhskie-reebok-royal-glide/'),
       InlineKeyboardButton(text='2',url='https://www.ozon.ru/category/reebok-lite-plus-3-0-sef/')],
       [InlineKeyboardButton(text='3',url='https://www.ozon.ru/search/?deny_category_prediction=true&from_global=true&text=Кроссовки+Reebok+Energylux+2.0&product_id=630653030'),
       InlineKeyboardButton(text='4',url='https://www.ozon.ru/product/krossovki-reebok-rush-runner-4-0-syn-870090408/')]])

#----------------------------------------------------------------------------------------------------------------------#
#Магазин Носков

socks = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Nike ✅'),
         KeyboardButton(text='Adidas ☰')],
        [KeyboardButton(text='Puma 🐆'),
         KeyboardButton(text='Fila ⭐')],
        [KeyboardButton(text='Назад ⬅️')]],
        resize_keyboard=True,)




#Носки NIKE
soNike = InlineKeyboardMarkup(inline_keyboard=[
       [InlineKeyboardButton(text='1',url='https://funkydunky.ru/catalog/aksessuary/noski/everyday-plus-cushioned-crew-dri-fit-socks-2pr-multi-colour/?ysclid=m6th5kghb0771850409'),
       InlineKeyboardButton(text='2',url='https://www.ozon.ru/category/noski-nike-everyday-cushion-crew/')],
       [InlineKeyboardButton(text='3',url='https://www.ozon.ru/product/noski-nike-everyday-lightweight-no-show-3-pary-707332900/'),
       InlineKeyboardButton(text='4',url='https://www.ozon.ru/product/noski-nike-everyday-cushion-crew-socks-3-pary-1277245782/')]])

soAdidas = InlineKeyboardMarkup(inline_keyboard=[
       [InlineKeyboardButton(text='1',url='https://www.ozon.ru/search/?deny_category_prediction=true&from_global=true&text=Комплект+носков&product_id=178706546'),
       InlineKeyboardButton(text='2',url='https://www.ozon.ru/category/noski-adidas-originals-crew/')],
       [InlineKeyboardButton(text='3',url='https://www.adidas.com/us/quarter'),
       InlineKeyboardButton(text='4',url='https://www.ozon.ru/search/?deny_category_prediction=true&from_global=true&text=Комплект+носков&product_id=152123687')]])

soPuma = InlineKeyboardMarkup(inline_keyboard=[
       [InlineKeyboardButton(text='1',url='https://www.ozon.ru/product/komplekt-noskov-puma-puma-unisex-sneaker-plain-3p-3-pary-140494794/'),
       InlineKeyboardButton(text='2',url='https://www.ozon.ru/product/noski-puma-unisex-quarter-plain-3-pary-469075227/')],
       [InlineKeyboardButton(text='3',url='https://www.football-mania.ru/p_getry-puma-team-liga-socks-core-06/?ysclid=m6thcph0rr439712625'),
       InlineKeyboardButton(text='4',url='https://au.puma.com/au/en/pd/sneaker-invisible-socks-3-pack/887497.html')]])

soFila = InlineKeyboardMarkup(inline_keyboard=[
       [InlineKeyboardButton(text='1',url='https://usmall.ru/product/6094019-fila-unisex-3-pack-crew-socks-in-white-fila?ysclid=m6therwdqd972877517'),
       InlineKeyboardButton(text='2',url='https://www.ozon.ru/product/komplekt-noskov-fila-3-pary-840837664/')],
       [InlineKeyboardButton(text='3',url='https://www.ozon.ru/category/noski-fila-muzhskie/'),
       InlineKeyboardButton(text='4',url='https://www.ozon.ru/category/noski-fila-muzhskie/')]])













































