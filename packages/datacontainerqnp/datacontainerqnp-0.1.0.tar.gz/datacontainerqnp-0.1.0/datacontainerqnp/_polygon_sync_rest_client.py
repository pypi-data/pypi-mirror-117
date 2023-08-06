import requests
import logging
from typing import Dict, List, Any
from ._polygon_rest_utils import PolygonRequestGenerator, PolygonResponseProcessor
from .constants import POLYGON_REST_DOMAIN
from .types import Bar


LOGGER = logging.getLogger(__name__)


class PolygonSyncRestClient:

    def __init__(self, auth_key: str, timeout: int = None):
        self.auth_key = auth_key
        self.domain = POLYGON_REST_DOMAIN
        self._session = requests.Session()
        self._session.params["apiKey"] = self.auth_key
        self.timeout = timeout

    def _handle_response(self, endpoint: str, params: Dict[str, str]) -> Dict[str, Any]:
        LOGGER.debug("sending request to {}".format(endpoint))
        resp: requests.Response = self._session.get(endpoint, params=params, timeout=self.timeout)
        if resp.status_code == 200:
            return resp.json()
        else:
            resp.raise_for_status()

    def intraday_stock_bars(self, symbol, *, date: str = None, aggr_minutes: int = 1, market_hours_only: bool = True,
                            start_date: str = None, end_date: str = None) -> List[Bar]:

        endpoint, params = PolygonRequestGenerator.intraday_stock_bars(symbol, date=date, aggr_minutes=aggr_minutes,
                                                                       start_date=start_date, end_date=end_date)

        endpoint = f"{self.domain}/{endpoint}"
        resp = self._handle_response(endpoint, params)

        results = resp.get('results')
        if isinstance(results, list):
            if market_hours_only:
                return PolygonResponseProcessor.market_hours_filter(results)
            return results
        return []

    def daily_stock_bars(self, symbol, *, start_date: str, end_date=None, aggr_days=1) -> List[Bar]:

        endpoint, params = PolygonRequestGenerator.daily_stock_bars(symbol,  start_date=start_date, end_date=end_date,
                                                                    aggr_days=aggr_days)

        endpoint = f"{self.domain}/{endpoint}"
        resp = self._handle_response(endpoint, params)

        results = resp.get('results')

        if isinstance(results, list):
            return results
        return []
