from pydantic import BaseModel, Field
from typing import List


class GatherMarketDataOutput(BaseModel):
    """Pydantic model for gather_market_data node outputs."""
    stock_prices: List[float] = Field(..., description="Current prices of relevant stocks")
    trading_volumes: List[int] = Field(..., description="Current trading volumes of relevant stocks")
    market_metrics: List[str] = Field(..., description="Other relevant market metrics")


def gather_market_data(general_input: str, **kwargs) -> GatherMarketDataOutput:
    """
    Gathers current market data from multiple sources and returns stock prices,
    trading volumes, and other market metrics.

    Returns
    -------
    dict
        A dictionary containing lists of stock prices, trading volumes, and
        market metrics.

    Raises
    ------
    ConnectionError
        If there's a failure connecting to data sources.
    DataParsingError
        If there's an issue parsing the gathered data.

    Examples
    --------
    >>> gather_market_data()
    {'stock_prices': [100.5, 200.2], 'trading_volumes': [1000, 2000],
    'market_metrics': ['metric1', 'metric2']}

    """
    return GatherMarketDataOutput(
        stock_prices=[],
        trading_volumes=[],
        market_metrics=[],
    )