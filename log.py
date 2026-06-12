import logging
from pathlib import Path
# Đường dẫn đến tập tin log
LOG_FILE = Path("temp/agent.log")
# Số dòng log
LOG_LINES = 20

# Hàm xử lí.
def get_last_logs(lines: int = LOG_LINES) -> str:
    try:
        if not LOG_FILE.exists():
            return "Chưa có file log."
        with LOG_FILE.open("r", encoding="utf-8", errors="ignore") as f:
            data = f.readlines()
        return "".join(data[-lines:])
    except Exception as e:
        return f"Lỗi khi đọc log: {e}"

logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)