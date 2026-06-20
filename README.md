# agentsTelegram-

Bot Telegram đơn giản để chạy các tệp Python từ xa và trả về kết quả đầu ra hoặc thông báo lỗi.

[english](README_EN.md)

## Tính năng

* Chạy các tệp Python từ xa thông qua Telegram.
* Nhận kết quả đầu ra của chương trình trực tiếp trên Telegram.
* Nhận thông báo lỗi nếu quá trình thực thi thất bại.
* Giới hạn quyền truy cập vào một tài khoản Telegram cụ thể bằng admin ID.
* Cấu hình dễ dàng bằng cách sử dụng các biến môi trường.

## Các lệnh

Bot hỗ trợ các lệnh sau (hầu hết các hành động chỉ giới hạn cho `TELEGRAM_ADMIN_ID` đã được cấu hình):

* `/start` - Hiển thị tin nhắn chào mừng và danh sách các lệnh khả dụng (Chỉ dành cho Admin).
* `/ping` - Kiểm tra xem bot có trực tuyến không (phản hồi bằng "online", mở cho tất cả mọi người).
* `/run <file_name.py>` - Thực thi một tệp Python trong thư mục dự án và trả về kết quả đầu ra hoặc lỗi (Chỉ dành cho Admin).
* `/log` - Hiển thị 20 dòng cuối cùng của log bot (Chỉ dành cho Admin).

## Yêu cầu hệ thống

* Python 3.10 trở lên
* Tài khoản Telegram
* Telegram Bot Token

## Cách lấy Telegram Bot Token

1. Mở Telegram.
2. Tìm kiếm **@BotFather**.
3. Gửi lệnh:

```text
/newbot
```

4. Làm theo hướng dẫn:

   * Nhập tên cho bot.
   * Nhập một username duy nhất kết thúc bằng `bot`.

Ví dụ:

```text
My Python Agent
my_python_agent_bot
```

5. BotFather sẽ gửi cho bạn một token tương tự như:

```text
1234567890:AAExampleTokenHere
```

Hãy sao chép token này. Bạn sẽ cần nó sau.

## Cách lấy Telegram Chat ID của bạn

### Cách 1: Sử dụng @userinfobot

1. Tìm kiếm **@userinfobot** trên Telegram.
2. Nhấn Start.
3. Bot sẽ hiển thị thông tin bao gồm ID của bạn.

Ví dụ:

```text
Id: 123456789
```

Sử dụng con số này làm admin ID của bạn.

## Cấu hình các biến môi trường

### Windows CMD

```cmd
set TELEGRAM_TOKEN=1234567890:AAExampleTokenHere
set TELEGRAM_ADMIN_ID=123456789
```

### Windows PowerShell

```powershell
$env:TELEGRAM_TOKEN="1234567890:AAExampleTokenHere"
$env:TELEGRAM_ADMIN_ID="123456789"
```

### Linux / macOS

```bash
export TELEGRAM_TOKEN="1234567890:AAExampleTokenHere"
export TELEGRAM_ADMIN_ID="123456789"
```

Quan trọng:

Tên các biến môi trường phải khớp chính xác:

```text
TELEGRAM_TOKEN
TELEGRAM_ADMIN_ID
```


## Cài đặt thư viện phụ thuộc

```bash
pip install -r requirements.txt
```

Hoặc cài đặt thủ công nếu không có tệp requirements.
```bash
pip install pyTelegramBotAPI
```

## Chạy Bot

Mở terminal trong thư mục dự án và chạy:

```bash
python main.py
```

Nếu mọi thứ được cấu hình chính xác, bot sẽ khởi động và đợi lệnh.

Ví dụ:

```text
Bot started successfully.
```

## Khắc phục sự cố

### Thiếu TELEGRAM_TOKEN

Hãy chắc chắn rằng biến môi trường tồn tại:

```cmd
echo %TELEGRAM_TOKEN%
```

### Thiếu TELEGRAM_ADMIN_ID

Kiểm tra:

```cmd
echo %TELEGRAM_ADMIN_ID%
```

### Bot không phản hồi

* Xác minh xem token đã chính xác chưa.
* Đảm bảo rằng bạn đã bắt đầu cuộc trò chuyện với bot.
* Đảm bảo rằng Telegram ID của bạn khớp với `TELEGRAM_ADMIN_ID`.
* Kiểm tra terminal để xem các thông báo lỗi.

## Lưu ý bảo mật

Không bao giờ công khai Telegram Bot Token của bạn.

Không commit token của bạn lên GitHub.

Sử dụng các biến môi trường thay vì ghi cứng các thông tin nhạy cảm vào mã nguồn.

## Giấy phép

MIT License
