from quantedge.data.market_data import MarketData
from datetime import datetime, timezone
import pytz
import MetaTrader5 as mt5

CONFIG = {
    'symbol': 'XAUUSD',
    'timeframe': {
        '1min': mt5.TIMEFRAME_M1,
        '5min': mt5.TIMEFRAME_M5,
        '15min': mt5.TIMEFRAME_M15,
        '30min': mt5.TIMEFRAME_M30,
        '1hr': mt5.TIMEFRAME_H1,
        '4hr': mt5.TIMEFRAME_H4,
    },
    'start_date': datetime(2026, 6, 1, tzinfo=pytz.timezone("Etc/UTC")),
    'end_date': datetime.now(timezone.utc)
}


def get_data(CONFIG):
    mkt_data = MarketData()
    mkt_data.set_symbol(CONFIG['symbol'])
    mkt_data.set_timeframe(CONFIG['timeframe']['5min'])
    mkt_data.set_start_date(CONFIG['start_date'])
    mkt_data.set_end_date(CONFIG['end_date'])

    return mkt_data.fetch_data()


def main():
    return get_data(CONFIG)

