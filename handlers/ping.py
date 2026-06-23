import telebot
def register_ping(bot: telebot.TeleBot):
    @ bot.message_handler(commands=["ping"])
    def ping(message):
        bot.reply_to(message, "online")

