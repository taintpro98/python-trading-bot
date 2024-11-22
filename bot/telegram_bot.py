from telegram import Bot
from bot.config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

class TelegramBot:
    def __init__(self):
        self.bot = Bot(token=TELEGRAM_BOT_TOKEN)

    def send_message(self, message):
        """
        Send a message to the configured Telegram chat.
        """
        self.bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
