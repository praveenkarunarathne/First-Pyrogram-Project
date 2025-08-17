# First Pyrogram Project

A minimal Telegram bot built with [Pyrogram](https://docs.pyrogram.org/). This repository contains a simple, ready-to-run bot script along with deployment files for platforms that support Procfile-based apps (e.g., Heroku).

## Features

- Pyrogram-powered Telegram bot
- Simple, single-file entry point (`bot.py`)
- Easy local run and Procfile-based deployment
- Requirements pinned via `requirements.txt`

> Note: This is a starter project. Extend `bot.py` with your own handlers and logic.

## Getting Started

### Prerequisites

- Python 3.8+ installed
- A Telegram Bot Token from [@BotFather](https://t.me/BotFather)
- Telegram API credentials (API_ID and API_HASH) from https://my.telegram.org/apps

### Clone and set up

```bash
git clone https://github.com/praveenkarunarathne/First-Pyrogram-Project.git
cd First-Pyrogram-Project
python -m venv .venv
# Activate the venv:
#   Windows: .venv\Scripts\activate
#   macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file (or set variables in your shell/hosting platform):

```bash
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
# Optional:
# BOT_OWNER_ID=123456789
```

If you prefer not to use a `.env` file, ensure these variables are present in your environment before running the bot.

## Run locally

```bash
python bot.py
```

## Deploy (Procfile-based)

This repository includes:
- `Procfile` (typically `worker: python bot.py`)
- `runtime.txt` (Python runtime version)

For Heroku-like platforms:
1. Create the app.
2. Set the Config Vars (API_ID, API_HASH, BOT_TOKEN, etc.).
3. Deploy the repository.
4. Scale the worker process if needed (e.g., `heroku ps:scale worker=1`).

## Project structure

```
.
├─ bot.py             # Main bot entry point
├─ requirements.txt   # Python dependencies
├─ Procfile           # Process type for deployment platforms
└─ runtime.txt        # Python runtime version for deployment platforms
```

## Customize

- Add more handlers, middleware, and logic in `bot.py`.
- Split code into modules as the project grows.
- Pin dependency versions in `requirements.txt` for reproducible builds.

## Troubleshooting

- Ensure API_ID, API_HASH, and BOT_TOKEN are correctly set.
- Double-check that your bot is started and not blocked by the chat/user.
- Review logs from your hosting platform (e.g., `heroku logs --tail`) for runtime errors.

## License

No license specified yet. Consider adding one (e.g., MIT, Apache-2.0) to clarify usage.

## Acknowledgements

- [Pyrogram](https://docs.pyrogram.org/)
- Telegram Bot API
