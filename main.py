import telebot
from config import TOKEN, ADMIN_ID
from runner import run_python
from log import logger, get_last_logs
import time
import os
from html import escape

bot = telebot.TeleBot(TOKEN)
last_run = 0
def file_exists_exact(filename):
    files = os.listdir(".")
    return filename in files
# Hàm ping: Kiểm tra nhanh xem bot còn chạy không.
@ bot.message_handler(commands=["ping"])
def ping(message):
    bot.reply_to(message, "online")

# Lệnh start: Chào mừng và hướng dẫn sử dụng.
@bot.message_handler(commands=["start"])
def start(message):
    if message.chat.id != ADMIN_ID:
        return
    bot.reply_to(
        message,
        "Chào mừng! Đây là Agent Bot điều khiển máy tính từ xa.\n\n"
        "Các lệnh hỗ trợ:\n"
        "/ping - Kiểm tra nhanh kết nối\n"
        "/run <tên_file.py> - Thực thi một file Python\n"
        "/start - Hiển thị hướng dẫn này\n"
        "/log - Xem 20 dòng log gần nhất"
    )
# Lệnh log, xem 20 dòng  log cuối cùng.
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
# Lệnh run: Chạy file python, hàm cốt lõi của bot.
@bot.message_handler(commands=['run'])
def run_file(message):
    # Kiểm tra ID người dùng
    if message.chat.id != ADMIN_ID:
        return
# Chống spam
    global last_run
    if time.time() - last_run < 15:
        return
    last_run = time.time()

    try:
        parts  = message.text.split()
        # Phòng lỗi truy cập phần tử hợp lệ trước khi lấy giữ liệu.
        if len(parts) < 2:
            bot.reply_to(
            message,
                "Cách sử dụng: ten-file.py. Vui lòng nhập đúng cú pháp"
            )
            return
        file_name = parts[1]
        # Kiểm tra đuôi file .py
        if not file_name.endswith(".py"):
            bot.reply_to(
                message,
                "File không hợp lệ, chỉ file .py mới được phép chạy"
            )
            return

        # Kiểm tra file tồn tại.
        if not file_exists_exact(file_name):
            bot.reply_to(
                message,
                "Không tìm thấy file. Hãy kiểm tra lại tên file và chữ hoa/chữ thường."
            )
            return

        out, err = run_python(file_name)

        if err:

            bot.reply_to(
            message,
            f"<pre>{escape(err[-3000:])}</pre>",
            parse_mode="HTML"
        )
            

        else:
            bot.reply_to(
            message,
            F"<pre>{escape(out[-3000:])}</pre>",
            parse_mode="HTML"
        )
    except Exception as e:
        logger.exception("Unexpected error")
        bot.reply_to(message, str(e))
print("Telegram agent started successfully.")
logger.info("bot started")
bot.infinity_polling()