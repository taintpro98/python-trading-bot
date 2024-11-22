import pandas as pd
from binance.client import Client
from bot.config import BINANCE_API_KEY, BINANCE_API_SECRET, SYMBOL, INTERVAL

class PriceChecker:
    def __init__(self):
        self.client = Client(api_key=BINANCE_API_KEY, api_secret=BINANCE_API_SECRET)

    def fetch_15m_candles(self, limit=20):
        """
        Fetch the latest 15-minute candles and calculate the MA20.
        """
        candles = self.client.get_klines(symbol=SYMBOL, interval=Client.KLINE_INTERVAL_15MINUTE, limit=limit)
        df = pd.DataFrame(candles, columns=[
            'timestamp', 'open', 'high', 'low', 'close', 'volume',
            'close_time', 'quote_asset_volume', 'number_of_trades',
            'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
        ])
        df['close'] = df['close'].astype(float)
        ma20 = df['close'].rolling(window=20).mean().iloc[-1]
        current_price = df['close'].iloc[-1]
        return current_price, ma20
