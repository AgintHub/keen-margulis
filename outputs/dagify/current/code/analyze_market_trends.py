from pydantic import BaseModel, Field
from typing import List


class GatherMarketDataOutput(BaseModel):
    """Pydantic model for gather_market_data node outputs."""
    stock_prices: List[float] = Field(..., description="Current prices of relevant stocks")
    trading_volumes: List[int] = Field(..., description="Current trading volumes of relevant stocks")
    market_metrics: List[str] = Field(..., description="Other relevant market metrics")


class AnalyzeMarketTrendsOutput(BaseModel):
    """Pydantic model for analyze_market_trends node outputs."""
    trend_identification: str = Field(..., description="Identified market trends")
    pattern_analysis: str = Field(..., description="Detailed analysis of market patterns")


def analyze_market_trends(gather_market_data_input: GatherMarketDataOutput, **kwargs) -> AnalyzeMarketTrendsOutput:
    """
    Analyze gathered market data to identify trends and patterns.

    Parameters
    ----------
    stock_prices : List[float]
        Current prices of relevant stocks gathered from the market.
    trading_volumes : List[int]
        Current trading volumes of relevant stocks.
    market_metrics : List[str]
        Other relevant market metrics.

    Returns
    -------
    {trend_identification: str, pattern_analysis: List[str]}
        A dictionary containing the identified market trends as a string and
        a detailed analysis of market patterns as a list of strings.

    Raises
    ------
    ValueError
        If any of the input lists (stock_prices, trading_volumes,
        market_metrics) are empty or not provided.

    Examples
    --------
    >>> stock_prices = [100.5, 102.1, 101.8]
    >>> trading_volumes = [1000, 1200, 1100]
    >>> market_metrics = ['metric1', 'metric2', 'metric3']
    >>> result = analyze_market_trends(stock_prices, trading_volumes,
    market_metrics)
    {'trend_identification': 'Bullish trend', 'pattern_analysis': ['Increasing
    prices', 'Stable trading volume']}

    >>> stock_prices = [90.2, 88.5, 89.1]
    >>> trading_volumes = [800, 700, 750]
    >>> market_metrics = ['metric4', 'metric5', 'metric6']
    >>> result = analyze_market_trends(stock_prices, trading_volumes,
    market_metrics)
    {'trend_identification': 'Bearish trend', 'pattern_analysis': ['Decreasing
    prices', 'Decreasing trading volume']}

    """
    return AnalyzeMarketTrendsOutput(
        trend_identification="",
        pattern_analysis="",
    )