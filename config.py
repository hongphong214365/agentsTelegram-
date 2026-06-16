import os
import sys

TOKEN = os.getenv("TELEGRAM_TOKEN")
ADMIN_ID_RAW = os.getenv("TELEGRAM_ADMIN_ID")

if not TOKEN:
    sys.exit("Lỗi: Chưa cấu hình biến môi trường 'TELEGRAM_TOKEN'.")

if not ADMIN_ID_RAW:
    sys.exit("Lỗi: Chưa cấu hình biến môi trường 'TELEGRAM_ADMIN_ID'.")

try:
    ADMIN_ID = int(ADMIN_ID_RAW)
except ValueError:
    sys.exit(f"Lỗi: 'TELEGRAM_ADMIN_ID' phải là một số nguyên, nhận được: '{ADMIN_ID_RAW}'.")