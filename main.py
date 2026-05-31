import telebot
from config import TOKEN, ADMIN_ID
from runner import run_python
import time
bot = telebot.TeleBot(TOKEN)
last_run = 0
def file_exists_exact(filename):
    files = os.listdir(".")
    return filename in files
@bot.message_handler(commands=['run'])
def run_file(message):
    if message.chat.id != ADMIN_ID:
       return

    global last_run
    if time.time() - last_run < 15:
        return
    last_run = time.time()
    try:
        file_name = message.text.split()[1]
        if not file_name.endswith(".py"):
            bot.reply_to(
                message,
                "File không hợp lệ, chỉ file .py mới được phép chạy"
        )
        return
        if not file_exists_exact(file_name):
            bot.reply_to(
            message,
            "Không tìm thấy file. Hãy kiểm tra lại tên file và chữ hoa/chữ thường."
        )
        return

        out, err = run_python(file_name)

        if err:

            bot.reply_to(message, err[-3000:])

        else:
            bot.reply_to(message, out[-3000:])
    except Exception as e:
        bot.reply_to(message, str(e))
print("Telegram agent started successfully.")
bot.infinity_polling()