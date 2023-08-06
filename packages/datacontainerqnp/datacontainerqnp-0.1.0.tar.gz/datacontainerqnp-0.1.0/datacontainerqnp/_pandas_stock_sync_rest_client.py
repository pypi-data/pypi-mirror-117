import pandas as pd
from typing import List, Dict
from .types import Bar
import logging
from ._polygon_sync_rest_client import PolygonSyncRestClient
from ._pandas_stock_adapter import PandasStockAdapter

LOGGER = logging.getLogger(__name__)


class PandasStockSyncRestClient:

    def __init__(self, polygon_sync_rest_client: PolygonSyncRestClient) -> None:
        self.polygon_sync_rest_client = polygon_sync_rest_client

    def daily_bars(self, *symbols: str, start_date: str, end_date: str = None) -> pd.DataFrame:
        if len(symbols) == 1:
            bars = self.polygon_sync_rest_client.daily_stock_bars(symbols[0], start_date=start_date, end_date=end_date)
            return PandasStockAdapter.convert_bars_to_dataframe(bars, scope='day')
        elif len(symbols) > 1:
            _symbols = symbols
            symbol2bars: Dict[str, List[Bar]] = {}
            for symbol in _symbols:
                symbol2bars[symbol] = self.polygon_sync_rest_client.daily_stock_bars(symbol, start_date=start_date,
                                                                                     end_date=end_date)
            return PandasStockAdapter.convert_multi_symbols_bars_to_dataframe(symbol2bars, scope='day')

        else:
            raise ValueError("input doesn't have any symbol")

    def minute_bars(self, *symbols: str, date: str = None, aggr_minutes: int = 1, market_hours_only: bool = True,
                    start_date: str = None, end_date: str = None) -> pd.DataFrame:

        if len(symbols) == 1:
            bars = self.polygon_sync_rest_client.intraday_stock_bars(symbols[0],
                                                                     date=date,
                                                                     aggr_minutes=aggr_minutes,
                                                                     market_hours_only=market_hours_only,
                                                                     start_date=start_date,
                                                                     end_date=end_date)

            return PandasStockAdapter.convert_bars_to_dataframe(bars, scope='minute')
        elif len(symbols) > 1:
            _symbols = symbols
            symbol2bars: Dict[str, List[Bar]] = {}
            for symbol in _symbols:
                symbol2bars[symbol] = self.polygon_sync_rest_client \
                    .intraday_stock_bars(symbol,
                                         date=date,
                                         aggr_minutes=aggr_minutes,
                                         market_hours_only=market_hours_only,
                                         start_date=start_date,
                                         end_date=end_date)

            return PandasStockAdapter.convert_multi_symbols_bars_to_dataframe(symbol2bars, scope='minute')

        else:
            raise ValueError("input doesn't have any symbol")
