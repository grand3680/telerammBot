import telebot
from telebot import types
def about_message(message, bot):
  markup = types.InlineKeyboardMarkup()
  button1 = types.InlineKeyboardButton("Me github - ", url='https://github.com/grand3680')
  button2 = types.InlineKeyboardButton("My discord - ", callback_data="DISCORD")
  button3 = types.InlineKeyboardButton("My Telegramm - ", url='https://t.me/XxGrandxX')
  markup.add(button1, button2, button3)
  bot.send_message(message.chat.id, f'Hey @{message.chat.username} this my links ', reply_markup=markup)
