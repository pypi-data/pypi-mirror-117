from typing import List, Union, Dict, Tuple
from datetime import datetime, date
from .types import Bar
from stockutilitiesqnp import timing
import pandas as pd


class PandasStockAdapter:
    """PandasStockAdapter

    Provide utilities function to convert polygon bars and trades to pandas dataframe.

    """

    @staticmethod
    def convert_bars_to_dataframe(bars: List[Bar], scope: str = "minute") -> pd.DataFrame:
        index = PandasStockAdapter._timestamps_to_datetime_index([bar['t'] for bar in bars], scope)
        return pd.DataFrame(bars, columns=["o", "h", "l", "c", "v"], index=index)

    @staticmethod
    def convert_multi_symbols_bars_to_dataframe(symbol2bars: Dict[str, List[Bar]], scope: str = "minute") \
            -> pd.DataFrame:

        def mount_bar(target: Dict[str, Union[int, float]], _symbol: str, _bar: Bar):
            target[f"{_symbol}_o"] = _bar['o']
            target[f"{_symbol}_h"] = _bar['h']
            target[f"{_symbol}_l"] = _bar['l']
            target[f"{_symbol}_c"] = _bar['c']
            target[f"{_symbol}_v"] = _bar['v']
            pass

        # merge bars
        # get all timestamp
        timestamp2bars: Dict[int, Dict[str, Union[int, float]]] = {}
        for symbol, bars in symbol2bars.items():
            for bar in bars:
                if bar['t'] not in timestamp2bars:
                    timestamp2bars[bar['t']] = {}
                mount_bar(timestamp2bars[bar['t']], symbol, bar)

        timestamp2bars_list: List[Tuple[int, Dict[str, Union[int, float]]]] = []

        for timestamp, merged_bars in timestamp2bars.items():
            timestamp2bars_list.append((timestamp, merged_bars))

        timestamp2bars_list.sort(key=lambda item: item[0])

        index = PandasStockAdapter._timestamps_to_datetime_index([item[0] for item in timestamp2bars_list], scope)
        return pd.DataFrame([item[1] for item in timestamp2bars_list], index=index)


    @staticmethod
    def _timestamps_to_datetime_index(timestamps: List[int], scope: str = "minute") -> pd.DatetimeIndex:
        if scope == "minute":
            # by using timing.datetime_ny, it will automatically add timezone info
            return pd.DatetimeIndex([timing.datetime_ny(timestamp) for timestamp in timestamps])
        elif scope == "day":
            return pd.DatetimeIndex([timing.date_ny(timestamp) for timestamp in timestamps])
        else:
            raise ValueError(f"scope must be either minute or day, {scope} is invalid.")
