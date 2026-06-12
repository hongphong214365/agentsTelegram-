# Copilot instructions for agentsTelegram-

## Quick commands
- Install deps: pip install -r requirements.txt
- Run bot: python main.py
- Run a single file (manual test): python <filename>.py

Notes: There are no test/CI or lint configs in the repo (no pytest, tox, pyproject.toml, setup.py, or flake8/mypy/black configs). If you add tests, include how to run a single test here.

## High-level architecture (big picture)
- main.py: entrypoint. Creates TeleBot using TOKEN and listens for commands (/ping, /run). Replies to user and polls forever.
- config.py: reads environment variables TELEGRAM_TOKEN and TELEGRAM_ADMIN_ID. ADMIN_ID is parsed to int.
- runner.py: small wrapper around subprocess.run used to execute arbitrary python files with a 30s timeout. Returns (stdout, stderr).
- log.py: central logging setup and a helper to read last log lines. Logs write to temp/agent.log.
- temp/ and Backup/: runtime directories used for logs and backups.

Flow: main -> config (env) -> TeleBot handlers -> runner.run_python executes requested file -> replies with stdout/stderr -> logger records events.

## Key conventions and repo-specific patterns
- Secrets must come from environment variables. Use TELEGRAM_TOKEN and TELEGRAM_ADMIN_ID (exact names).
- ADMIN_ID must be an integer. Code assumes int(os.getenv(...)). Validate env prior to running to avoid crashes.
- The bot restricts actions to the configured ADMIN_ID; all command handlers check message.chat.id.
- runner.run_python uses subprocess.run with timeout=30. Keep long-running tasks out of /run or increase timeout intentionally.
- Files are executed from repo root current working directory; file name matching is exact (case sensitive on some systems). Use file_exists_exact style checks if adding handlers.
- Logging writes to temp/agent.log. Ensure temp/ exists and is writable before running the bot.
- Do not hard-code tokens, admin IDs, or absolute paths.

## Existing AI/agent guidance to incorporate
There is an AI_RULES.md (project-owned assistant guidance). Important points to keep:
- Prefer replies and explanations in Vietnamese when the assistant is asked to help.
- Act as a Senior Python Developer familiar with Python 3.14, Telegram bots, logging, configuration, and Windows deployment.
- Follow the project's principles: small, readable changes; do not rename files/functions/classes without explicit approval; ask for confirmation before large structural changes.
- Before making edits, produce a short plan that lists files and lines to change and a brief rationale.

## Gotchas and suggested checks for Copilot sessions
- Validate env vars early and provide clear error messages if TELEGRAM_TOKEN or TELEGRAM_ADMIN_ID are missing or malformed.
- runner.run_python executes arbitrary Python code. When suggesting code changes, avoid injecting untrusted inputs into the execution path and recommend sandboxing if adding features.
- log.py contains code that may raise exceptions (e.g., using log_file.exists without calling it). Verify logging helper functions before using them.

## If you (or Copilot) add tests or linters
- Add pytest and a minimal pyproject.toml or setup.cfg so instructions can include: pytest tests/test_x.py::test_name
- Add pre-commit or a flake8/black config and update this file with their run commands.

---

If this file should be expanded with test/lint commands or MCP server configuration, say which tools to integrate (pytest, Playwright, etc.) and a small sample config will be added.

# Phần bổ sung.
Đọc PROJECT_CONTEXT.md trước khi thực hiện bất kỳ thay đổi nào.

PROJECT_CONTEXT.md là nguồn thông tin chính của dự án.

Nếu có mâu thuẫn giữa yêu cầu hiện tại và PROJECT_CONTEXT.md:
- Hỏi lại người dùng.
- Không tự quyết định.