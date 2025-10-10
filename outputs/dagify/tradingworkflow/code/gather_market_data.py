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
    return GatherMarketDataOutput(
        stock_prices=[],
        trading_volumes=[],
        market_metrics=[],
    )