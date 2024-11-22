import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bot.telegram_bot import TelegramBot
from bot.price_checker import PriceChecker

def main():
    telegram_bot = TelegramBot()
    price_checker = PriceChecker()
    last_price_above = None

    while True:
        try:
            current_price, ma20 = price_checker.fetch_15m_candles()
            print(f"Current Price: {current_price}, MA20: {ma20}")
            price_above = current_price > ma20

            if last_price_above is not None and price_above != last_price_above:
                direction = "above" if price_above else "below"
                telegram_bot.send_message(
                    f"Bitcoin price is now {direction} the MA20 line.\n"
                    f"Price: {current_price}, MA20: {ma20}"
                )

            last_price_above = price_above
            time.sleep(60)  # Check every minute
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)

if __name__ == "__main__":
    main()
