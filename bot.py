import telebot

# 5515757831:AAHM-mnAdKkGYHEMK-6SLfMmxKd_iM-IGbQ
# bot: t.me/test_shirenina_bot

TOKEN = "5515757831:AAHM-mnAdKkGYHEMK-6SLfMmxKd_iM-IGbQ"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, как дела?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()