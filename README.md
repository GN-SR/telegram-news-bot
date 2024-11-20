
# Telegram News Bot

This is a Telegram bot that fetches the latest news and sends it directly to your chat. It is designed to keep you updated with real-time news from various sources, delivered straight to your Telegram app.

## Features

- Fetches the latest news from popular APIs (e.g., NewsAPI, RSS feeds, etc.).
- Supports customizable news categories (e.g., technology, sports, politics, entertainment).
- Simple and user-friendly commands to get the news directly.
- Sends news summaries with headlines, descriptions, and links for full articles.

## Prerequisites

Before running the bot, ensure you have the following:

- Python 3.8 or higher installed.
- A Telegram account and a bot token from [BotFather](https://core.telegram.org/bots#botfather).
- An API key from a news provider (e.g., [NewsAPI](https://newsapi.org/)).

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/telegram-news-bot.git
    cd telegram-news-bot
    ```

2. Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure your bot by creating a `.env` file in the project directory and adding the following:

    ```env
    BOT_TOKEN=your_telegram_bot_token
    NEWS_API_KEY=your_news_api_key
    ```

4. Run the bot:

    ```bash
    python bot.py
    ```

## Usage

- Start the bot by searching for it in Telegram and clicking "Start."
- Use the following commands to interact with the bot:
    - `/start` - Get a welcome message and available commands.
    - `/news [category]` - Fetch news in the specified category (e.g., `/news technology`).
    - `/help` - Display the help message.

## Project Structure

```
telegram-news-bot/
│
├── bot.py                # Main script to run the bot
├── requirements.txt      # Python dependencies
├── .env                  # Configuration file (not included in the repo)
└── README.md             # Project documentation
```


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Telegram Bot API](https://core.telegram.org/bots/api)
- [NewsAPI](https://newsapi.org/)
- Python community for the amazing libraries and tools.

---

Happy coding! 🎉
