from stockutilitiesqnp import timing, market_hours
from typing import Tuple, Dict, Any, Union, List
from .types import Bar


class PolygonRequestGenerator:

    @staticmethod
    def intraday_stock_bars(symbol, *, date: str = None, aggr_minutes: int = 1, start_date: str = None,
                            end_date: str = None) -> Tuple[str, Dict[str, Any]]:
        if not isinstance(aggr_minutes, int):
            raise ValueError("aggr_minutes must be int")

        endpoint = f'v2/aggs/ticker/{symbol}/range/{aggr_minutes}/minute'

        if isinstance(start_date, str) or isinstance(end_date, str):
            if isinstance(start_date, str) and isinstance(end_date, str):
                endpoint = f'{endpoint}/{timing.str_to_timestamp_ny(start_date, "00:00")}' \
                           f'/{timing.str_to_timestamp_ny(end_date, "23:59")}'
            else:
                raise ValueError("start_date and end_date must be valid date str")
        else:
            if not isinstance(date, str):
                date = timing.date_ny_str()
            endpoint = f'{endpoint}/{timing.str_to_timestamp_ny(date, "00:00")}' \
                       f'/{timing.str_to_timestamp_ny(date, "23:59")}'

        params = {"sort": "asc", "unadjusted": "false"}

        return endpoint, params

    @staticmethod
    def daily_stock_bars(symbol, *, start_date: str, end_date: str = None, aggr_days: int = 1) \
            -> Tuple[str, Dict[str, Any]]:
        if not isinstance(start_date, str):
            raise ValueError("start_date must be a valid date str")

        if not isinstance(aggr_days, int):
            raise ValueError("aggr_minutes must be int")

        if not isinstance(end_date, str):
            end_date = timing.date_ny_str()

        endpoint = f'v2/aggs/ticker/{symbol}/range/{aggr_days}/day/{start_date}/{end_date}'
        params = {"sort": "asc", "unadjusted": "false"}

        return endpoint, params


class PolygonResponseProcessor:

    @staticmethod
    def market_hours_filter(bars: List[Bar]) -> List[Bar]:
        # +1 to avoid the bar at market close e.g. 13:00 or 16:00
        return list(filter(lambda bar: isinstance(bar.get('t'), int) and market_hours.is_market_open(bar.get('t') + 1),
                           bars))
