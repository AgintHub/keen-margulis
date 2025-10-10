from ._collect_market_data.identify_market_data_sources import identify_market_data_sources
from ._collect_market_data.fetch_stock_prices import fetch_stock_prices
from ._collect_market_data.fetch_trading_volumes import fetch_trading_volumes
from ._collect_market_data.fetch_economic_indicators import fetch_economic_indicators
from ._collect_market_data.validate_data_collection import validate_data_collection

from pydantic import BaseModel, Field
from typing import List


class CollectMarketDataOutput(BaseModel):
    """Pydantic model for collect_market_data node outputs."""
    stock_prices: List[float] = Field(..., description="List of stock prices")
    trading_volumes: List[int] = (
        Field(..., description="List of trading volumes")
    )
    economic_indicators: List[float] = (
        Field(..., description="List of economic indicators")
    )
    data_collection_status: bool = (
        Field(..., description="Whether data collection was successful")
    )


def collect_market_data(general_input: str, **kwargs) -> CollectMarketDataOutput:
    """
    Collects and structures market data for analysis.

    Returns
    -------
    Tuple[List[float], List[int], List[float], bool]
        A tuple containing lists of stock prices, trading volumes, economic
        indicators, and a boolean indicating whether data collection was
        successful.

    Raises
    ------
    ConnectionError
        If there's a failure connecting to any data source.
    DataParsingError
        If there's an issue parsing data from any source.

    Examples
    --------
    >>> data = collect_market_data()
    ({'stock_prices': [100.5, 102.1], 'trading_volumes': [1000, 1200],
    'economic_indicators': [2.5, 2.7], 'data_collection_status': True})

    >>> stock_prices, trading_volumes, economic_indicators, status =
    collect_market_data()
    ([100.5, 102.1], [1000, 1200], [2.5, 2.7], True)

    """
    data_sources: List[str] = identify_market_data_sources(input_params=general_input)
    
    stock_data: List[float] = fetch_stock_prices(sources=data_sources)
    volume_data: List[int] = fetch_trading_volumes(sources=data_sources)
    economic_data: List[float] = fetch_economic_indicators(sources=data_sources)
    
    collection_success: bool = validate_data_collection(stock_prices=stock_data, volumes=volume_data, indicators=economic_data)
    
    return CollectMarketDataOutput(
        stock_prices=stock_data,
        trading_volumes=volume_data,
        economic_indicators=economic_data,
        data_collection_status=collection_success
    )