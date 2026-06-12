Tạo command Telegram mới.



Yêu cầu:



\-Chỉ ADMIN\_ID được sử dụng.

\- Ghi log đầy đủ.

\-Có xử lý lỗi.

\-Trả lời bằng tiếng Việt.

* Thêm các comment trong code bằng tiếng việt.
* Viết code dễ đọc, dễ hiểu.
* không sửa các file khác khi không cần.
* 

Ví dụ:



@bot.message\_handler(commands=\['ping'])

def ping(message):

&#x20;   if message.chat.id != ADMIN\_ID:

&#x20;       return



&#x20;   logger.info("Ping command")



&#x20;   bot.reply\_to(message, "Pong!")

