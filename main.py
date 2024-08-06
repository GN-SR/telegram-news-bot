import telepot
from telepot.loop import MessageLoop
import requests
import time

# Replace with your own Telegram bot token and News API key
TELEGRAM_BOT_TOKEN = 'BOT_API_TOKEN'  # Replace with your Telegram bot token
NEWS_API_KEY = 'NEWS_API_KEY'  # Replace with your News API key
NEWS_API_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=NEWS_API_KEY' 

def fetch_latest_news():
    response = requests.get(NEWS_API_URL)
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get('articles', [])
        news_summary = "Latest News:\n\n"
        for article in articles[:5]:  # Get the top 5 news articles
            news_summary += f"{article['title']}\n{article['url']}\n\n"
        return news_summary
    else:
        return "Failed to fetch news."

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg.get('text')

    if command == '/news':
        news = fetch_latest_news()
        bot.sendMessage(chat_id, news)
    else:
        bot.sendMessage(chat_id, "Send /news to get the latest news.")

bot = telepot.Bot(TELEGRAM_BOT_TOKEN)
MessageLoop(bot, handle).run_as_thread()
print('Listening for commands...')

# Keep the program running
while True:
    time.sleep(10)
