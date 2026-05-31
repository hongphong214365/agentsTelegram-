
# agentsTelegram-

Simple Telegram bot to run Python files remotely and return output or errors.

## Features

* Run Python files remotely through Telegram.
* Receive program output directly in Telegram.
* Receive error messages if execution fails.
* Restrict access to a specific Telegram account using an admin ID.
* Easy configuration using environment variables.

## Requirements

* Python 3.10 or newer
* Telegram account
* Telegram Bot Token

## Getting a Telegram Bot Token

1. Open Telegram.
2. Search for **@BotFather**.
3. Send the command:

```text
/newbot
```

4. Follow the instructions:

   * Enter a bot name.
   * Enter a unique username ending with `bot`.

Example:

```text
My Python Agent
my_python_agent_bot
```

5. BotFather will send you a token similar to:

```text
1234567890:AAExampleTokenHere
```

Copy this token. You will need it later.

## Getting Your Telegram Chat ID

### Method 1: Using @userinfobot

1. Search for **@userinfobot** on Telegram.
2. Press Start.
3. The bot will display information including your ID.

Example:

```text
Id: 123456789
```

Use this number as your admin ID.

## Configure Environment Variables

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

Important:

The variable names must match exactly:

```text
TELEGRAM_TOKEN
TELEGRAM_ADMIN_ID
```

If your code reads these names, users only need to create the variables with the same names and the bot will work without editing the source code.

## Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually if no requirements file is provided.
```bash
pip install pyTelegramBotAPI
```

## Running the Bot

Open a terminal in the project folder and run:

```bash
python main.py
```

If everything is configured correctly, the bot should start and wait for commands.

Example:

```text
Bot started successfully.
Waiting for Telegram messages...
```

## Troubleshooting

### TELEGRAM_TOKEN is missing

Make sure the environment variable exists:

```cmd
echo %TELEGRAM_TOKEN%
```

### TELEGRAM_ADMIN_ID is missing

Check:

```cmd
echo %TELEGRAM_ADMIN_ID%
```

### Bot does not respond

* Verify the token is correct.
* Make sure you started a chat with the bot.
* Make sure your Telegram ID matches `TELEGRAM_ADMIN_ID`.
* Check the terminal for error messages.

## Security Notes

Never publish your Telegram Bot Token.

Do not commit your token to GitHub.

Use environment variables instead of hardcoding secrets into the source code.

## License

MIT License
