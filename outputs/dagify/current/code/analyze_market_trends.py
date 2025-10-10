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


class AnalyzeMarketTrendsOutput(BaseModel):
    """Pydantic model for analyze_market_trends node outputs."""
    trend_predictions: List[str] = (
        Field(..., description="Predictions of future market trends.")
    )
    trend_confidence: List[float] = (
        Field(..., description="Confidence levels in trend predictions.")
    )


def analyze_market_trends(gather_market_data_input: GatherMarketDataOutput, **kwargs) -> AnalyzeMarketTrendsOutput:
    """
    Analyze historical market data to predict future trends and their confidence
    levels.

    Parameters
    ----------
    stock_prices : List[float]
        Historical prices of relevant stocks.
    trading_volumes : List[int]
        Historical trading volumes of relevant stocks.
    market_metrics : List[str]
        Other relevant historical market metrics.

    Returns
    -------
    Tuple[List[str], List[float]]
        A tuple containing a list of trend predictions and a list of their
        corresponding confidence levels.

    Raises
    ------
    ValueError
        If the input lists are of different lengths or if the data is
        inconsistent.

    Examples
    --------
    >>> stock_prices = [100.0, 120.0, 110.0]
    >>> trading_volumes = [1000, 1200, 1100]
    >>> market_metrics = ['metric1', 'metric2', 'metric3']
    >>> trend_predictions, trend_confidence =
    analyze_market_trends(stock_prices, trading_volumes, market_metrics)
    (['uptrend', 'downtrend'], [0.8, 0.7])

    >>> stock_prices = [90.0, 100.0, 95.0]
    >>> trading_volumes = [900, 1000, 950]
    >>> market_metrics = ['metric4', 'metric5', 'metric6']
    >>> trend_predictions, trend_confidence =
    analyze_market_trends(stock_prices, trading_volumes, market_metrics)
    (['uptrend', 'downtrend'], [0.85, 0.75])

    """
    return AnalyzeMarketTrendsOutput(
        trend_predictions=[],
        trend_confidence=[],
    )