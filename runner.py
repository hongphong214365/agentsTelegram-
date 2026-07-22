import subprocess
import os
from config import RUN_TIMEOUT


def run_python(file_name):
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONUTF8"] = "1"
    result = subprocess.run(
        ["python", file_name],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        env=env,
        timeout=run_timeout,
    )
    return result.stdout, result.stderr
