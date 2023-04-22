import random
def random_message(message, bot):
  if random.randint(0, 1) == 0:
    b = "tails"
    tailsArr = [
      "https://dic.academic.ru/pictures/wiki/files/82/Russian_Empire-1899-Coin-5-Obverse.jpg",
      "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Mariatheresientaler.jpg/119px-Mariatheresientaler.jpg",
      "https://upload.wikimedia.org/wikipedia/commons/d/db/Russian_Empire-1899-Coin-5-Reverse.jpg"
    ]
    img = tailsArr[random.randint(0, len(tailsArr) - 1)]
  else:
    b = "eagle"
    eagleArr = [
      "https://img1.goodfon.ru/wallpaper/nbig/9/62/orel-gory-kraski.jpg",
      "https://naturae.ru/foto/orel.jpg",
      "https://s9.travelask.ru/uploads/post/000/034/459/main_image/full-3c7614e1b0065e025a2a314fa06089a2.jpg"
    ]
    img = eagleArr[random.randint(0, len(eagleArr) - 1)]

  bot.send_photo(message.chat.id, img)
  bot.send_message(message.chat.id, f'hi @{message.chat.username} you drope it -  {b}')
  bot.send_message(message.chat.id, f'_______________________________')

  if message.chat.username != "XxGrandxX":
    myId = 1792123982
    bot.send_photo(myId, img)
    bot.send_message(myId, f'human fell out @{message.chat.username} -  {b}')

