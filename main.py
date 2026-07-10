import telebot
from config import TOKEN
from handlers import register_handlers
from log import logger

bot = telebot.TeleBot(TOKEN)
register_handlers(bot)
print("Telegram agent started successfully.")
logger.info("bot started")
bot.infinity_polling()
