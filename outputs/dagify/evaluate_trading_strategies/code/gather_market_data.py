from ._gather_market_data.establish_market_data_connection import establish_market_data_connection
from ._gather_market_data.fetch_stock_prices_data import fetch_stock_prices_data
from ._gather_market_data.fetch_trading_volumes_data import fetch_trading_volumes_data
from ._gather_market_data.fetch_market_metrics_data import fetch_market_metrics_data
from ._gather_market_data.process_stock_prices import process_stock_prices
from ._gather_market_data.process_trading_volumes import process_trading_volumes
from ._gather_market_data.process_market_metrics import process_market_metrics
from ._gather_market_data.validate_market_data import validate_market_data

from pydantic import BaseModel, Field
from typing import List


class GatherMarketDataOutput(BaseModel):
    """Pydantic model for gather_market_data node outputs."""
    stock_prices: List[float] = (
        Field(..., description="Current prices of relevant stocks")
    )
    trading_volumes: List[int] = (
        Field(..., description="Current trading volumes of relevant stocks")
    )
    market_metrics: List[str] = (
        Field(..., description="Other relevant market metrics")
    )


def gather_market_data(general_input: str, **kwargs) -> GatherMarketDataOutput:
    """
    Collects current market data including stock prices, trading volumes, and
    other relevant metrics.

    Returns
    -------
    Tuple[List[float], List[int], List[str]]
        A tuple containing the current stock prices, trading volumes, and
        other market metrics.

    Raises
    ------
    ConnectionError
        If there's an issue connecting to the data source.
    ValueError
        If the collected data is invalid or incomplete.

    Examples
    --------
    >>> gather_market_data()
    ([123.45, 67.89], [1000, 2000], ['metric1', 'metric2'])

    >>> stock_prices, trading_volumes, market_metrics = gather_market_data()
    stock_prices = [123.45, 67.89]
    trading_volumes = [1000, 2000]
    market_metrics = ['metric1', 'metric2']

    """
    connection_status: bool = establish_market_data_connection()
    if not connection_status:
        raise ConnectionError("Failed to connect to market data source")
    
    raw_stock_data: dict = fetch_stock_prices_data()
    raw_volume_data: dict = fetch_trading_volumes_data()
    raw_metrics_data: dict = fetch_market_metrics_data()
    
    processed_stock_prices: List[float] = process_stock_prices(data=raw_stock_data)
    processed_trading_volumes: List[int] = process_trading_volumes(data=raw_volume_data)
    processed_market_metrics: List[str] = process_market_metrics(data=raw_metrics_data)
    
    validation_result: bool = validate_market_data(
        stock_prices=processed_stock_prices,
        trading_volumes=processed_trading_volumes,
        market_metrics=processed_market_metrics
    )
    
    if not validation_result:
        raise ValueError("Collected market data is invalid or incomplete")
    
    return GatherMarketDataOutput(
        stock_prices=processed_stock_prices,
        trading_volumes=processed_trading_volumes,
        market_metrics=processed_market_metrics
    )