# import lib telegramm
import telebot
from telebot import types

# import main files
from test.test import testFun
from files.about import about_message
from files.random import random_message
testFun()

import json
with open('config.json') as f:
    templates = json.load(f)

bot = telebot.TeleBot(templates['bot_token'])

@bot.message_handler(commands=['start'])
def start_message(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  btn1 = types.KeyboardButton("❓ Random")
  btn2 = types.KeyboardButton("👋 about")
  markup.add(btn1, btn2)

  bot.send_message(message.chat.id,f"hi @{message.chat.username} Im {templates['author']} this my bot in python✌️ ", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'DISCORD':
       print('press button "DISCORD"')
    elif call.data == 'GITHUB':
       print('"press button GITHUB"')

@bot.message_handler(content_types=['text'])
def text(message):
  if message.text == "👋 about":
    about_message(message, bot)
  elif message.text == "❓ Random":
    random_message(message, bot)
  else:
    # userSpamId = 1456865918 # стас
    # bot.send_message(userSpamId, f'{message.text}')
    if message.chat.username != "XxGrandxX":
      myId = 1792123982
      bot.send_message(myId, f'@{message.chat.username} отправил -  {message.text}')

# 1456865918 стас
# 1421063125 алексей
# 5321681089 ура

bot.polling(none_stop = True, interval=0)
