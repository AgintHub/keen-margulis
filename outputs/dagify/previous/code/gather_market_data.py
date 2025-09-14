from pydantic import BaseModel, Field
from typing import List


class GatherMarketDataOutput(BaseModel):
    """Pydantic model for gather_market_data node outputs."""
    current_prices: List[float] = Field(..., description="Current prices of relevant assets")
    historical_prices: List[float] = Field(..., description="Historical price data for relevant assets")
    market_volumes: List[float] = Field(..., description="Current trading volumes of relevant assets")


def gather_market_data(general_input: str, **kwargs) -> GatherMarketDataOutput:
    """
    Gathers market data including current prices, historical prices, and trading
    volumes.

    Parameters
    ----------
    data_sources : List[str]
        List of financial data sources (e.g., exchanges, APIs, databases) to
        gather data from.
    assets : List[str]
        List of assets (e.g., stocks, cryptocurrencies) for which to gather
        market data.

    Returns
    -------
    Dict[str, List[float]]
        A dictionary containing current prices, historical prices, and
        market volumes for the specified assets.

    Raises
    ------
    ConnectionError
        If there's an issue connecting to any of the specified data sources.
    ValueError
        If the list of assets or data sources is empty or invalid.

    Examples
    --------
    >>> gather_market_data(data_sources=['exchange1', 'api2'], assets=['BTC',
    'ETH'])
    {'current_prices': [35000.0, 2500.0], 'historical_prices': [[34000.0,
    34500.0, 35000.0], [2400.0, 2450.0, 2500.0]], 'market_volumes': [1000.0,
    500.0]}

    >>> gather_market_data(data_sources=['database3'], assets=['AAPL', 'GOOGL'])
    {'current_prices': [150.0, 2800.0], 'historical_prices': [[145.0, 147.0,
    150.0], [2750.0, 2780.0, 2800.0]], 'market_volumes': [2000.0, 300.0]}

    """
    return GatherMarketDataOutput(
        current_prices=[],
        historical_prices=[],
        market_volumes=[],
    )