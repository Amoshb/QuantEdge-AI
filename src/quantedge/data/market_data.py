import MetaTrader5 as mt5
import pandas as pd


class MarketData:
    def __init__(self):
        self.symbol = None
        self.timeframe = None
        self.start_date = None
        self.end_date = None

    def fetch_symbols(self, pattern="*XA*"):
        symbols = mt5.symbols_get(pattern)
        if symbols is None:
            raise RuntimeError(f"Failed to fetch symbols: {mt5.last_error()}")

        return [symbol.name for symbol in symbols]

    def fetch_data(self):
        rates = mt5.copy_rates_range(
            self.symbol,
            self.timeframe,
            self.start_date,
            self.end_date,
        )

        if rates is None:
            raise RuntimeError(f"Failed to fetch rates: {mt5.last_error()}")

        df = pd.DataFrame(rates)

        if df.empty:
            raise ValueError("No data returned from MT5.")

        df["time"] = pd.to_datetime(df["time"], unit="s")

        return df

    def set_symbol(self, symbol):
        self.symbol = symbol

    def set_timeframe(self, timeframe):
        self.timeframe = timeframe

    def set_start_date(self, start_date):
        self.start_date = start_date

    def set_end_date(self, end_date):
        self.end_date = end_date