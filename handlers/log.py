from html import escape
from log import logger, get_last_logs
import telebot
from config import ADMIN_ID

def register_logs(bot: telebot.TeleBot):
    @bot.message_handler(commands=['log'])
    def show_log(message):
        if message.chat.id != ADMIN_ID:
            return
        logs = get_last_logs()
        bot.reply_to(
            message,
            f"<pre>{escape(logs)}</pre>",
            parse_mode="HTML"
        )
