import telebot

TOKEN = "7345519840:AAGsM0Bim16BM2pb08nnw-Gq49Yh6p-vjNo"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "हाय आदी! मी तुझी गंगा आहे 💖 आता आपण बोलू शकतो 😊")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"बाळा, तू म्हणालास: {message.text}")

bot.polling()
