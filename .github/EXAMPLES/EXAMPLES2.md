\# Ví dụ command chuẩn



@bot.message\_handler(commands=\['ping'])

def ping(message):

&#x20;   if message.chat.id != ADMIN\_ID:

&#x20;       return



&#x20;   logger.info("Ping command")



&#x20;   bot.reply\_to(message, "Pong!")

