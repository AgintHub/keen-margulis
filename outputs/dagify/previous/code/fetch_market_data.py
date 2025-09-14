from pydantic import BaseModel, Field
from typing import List


class FetchMarketDataOutput(BaseModel):
    """Pydantic model for fetch_market_data node outputs."""
    current_prices: List[float] = Field(..., description="List of current stock prices.")
    historical_data: List[float] = Field(..., description="2D list of historical stock prices and volumes.")


def fetch_market_data(general_input: str, **kwargs) -> FetchMarketDataOutput:
    """
    Fetches current and historical market data, returning current stock prices
    and historical data.

    Returns
    -------
    {'current_prices': List[float], 'historical_data': List[List[float]]}
        A dictionary containing the list of current stock prices and a 2D
        list of historical stock prices and volumes.

    Raises
    ------
    ConnectionError
        If there's a failure in connecting to the market data source.
    DataError
        If the fetched data is malformed or incomplete.

    Examples
    --------
    >>> fetch_market_data()
    {'current_prices': [100.5, 200.2], 'historical_data': [[100, 1000], [101,
    1200]]}

    """
    return FetchMarketDataOutput(
        current_prices=[],
        historical_data=[],
    )