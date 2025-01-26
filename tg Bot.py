import telebot
import random,os
import time
from telebot import types


bot = telebot.TeleBot("7771898758:AAGi0cU60t1LhGyb8Cpm3uUke5Sfg6Q5vKw")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Привет!Веди команду /help")

@bot.message_handler(commands=["help"])
def send_welcome(message):
    bot.reply_to(message,"Привет вот мои списки что я умею:"
                         "\n1)/hello,hi - говорит привет "
                         "\n2)/mem - присылает рандомный мем")
@bot.message_handler(commands=["hello","hi"])
def send_welcome(message):
    bot.reply_to(message,"Привет солнце")

#будет генерировать рандомный мем
@bot.message_handler(commands=["mem"])
def send_mem(message):
    name = random.choice(os.listdir("images"))
    with open(f"images/{name}","rb")as f:
        bot.send_photo(message.chat.id,f)

@bot.message_handler(commands=["me"])
def send_me(message):
    an = random.choice(os.listdir("pr.txt"))
    with open(f"pr.txt/{an}","rb")as f:
        bot.send_photo(message.chat.id,f)

@bot.message_handler(commands=["button"]) #button кнопка
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    name_1 = types.KeyboardButton("Кнопка")
    markup.add(name_1)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Кнопка":
        bot.send_message(message.chat.id, "https://habr.com/ru/users/lubaznatel/")

bot.infinity_polling()

















