import telebot
import os
from runner import run_python
import time
TOKEN = os.getenv("TELEGRAM_TOKEN")
admin_id =8701726368
bot = telebot.TeleBot(TOKEN)
last_run = 0
def file_exists_exact(filename):
    files = os.listdir(".")
    return filename in files
@bot.message_handler(commands=['run'])
def run_file(message):
    if message.chat.id != admin_id:
       return

    global last_run
    if time.time() - last_run < 15:
        bot.reply_to(message, "Từ từ bìn tĩnh chờ một tí")
        return
    last_run = time.time()
    try:
        file_name = message.text.split()[1]
        out, err = run_python(file_name)

        if not file_name.endswith(".py"):
            bot.reply_to(message,"File không hợp lệ, chỉ file .py mới được chạy thôi")
        if not file_exists_exact(file_name):
            bot.reply_to(message, "File không tồn  tại, kiểm  tra chữ hoa chữ thường đi")
            return
        if err:

            bot.reply_to(message, err[-3000:])

        else:
            bot.reply_to(message, out[-3000:])
    except Exception as e:
        bot.reply_to(message, str(e))

print("bot đang chạy...")
bot.infinity_polling()