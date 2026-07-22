import telebot
from config import ADMIN_ID, RUN_TIMEOUT


def register_status(bot: telebot.TeleBot):
    # Hàm kiểm tra trạng thái chi tiết của bot.
    @bot.message_handler(commands=["status"])
    def status(message):
        if message.chat.id != ADMIN_ID:
            return
        bot.reply_to(
            message,
            (
                "🤖 bot đang hoạt động.\n"
                f"File sẽ timeout sau: {RUN_TIMEOUT} giây"
            ),
        )
