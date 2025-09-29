from pydantic import BaseModel, Field
from typing import List


class FetchMarketDataOutput(BaseModel):
    """Pydantic model for fetch_market_data node outputs."""
    market_prices: List[float] = (
        Field(..., description="List of current market prices.")
    )
    market_volumes: List[int] = (
        Field(..., description="List of current market volumes.")
    )


class AnalyzeMarketTrendsOutput(BaseModel):
    """Pydantic model for analyze_market_trends node outputs."""
    trend_directions: List[str] = (
        Field(..., description="List of trend directions (up, down, stable).")
    )
    trend_strengths: List[float] = (
        Field(..., description="List of trend strengths.")
    )


def analyze_market_trends(fetch_market_data_input: FetchMarketDataOutput, **kwargs) -> AnalyzeMarketTrendsOutput:
    """
    Analyzes market trends based on fetched market data, producing trend
    directions and strengths.

    Parameters
    ----------
    market_prices : List[float]
        List of current market prices fetched from reliable sources.
    market_volumes : List[int]
        List of current market volumes fetched from reliable sources.

    Returns
    -------
    Tuple[List[str], List[float]]
        A tuple containing a list of trend directions (up, down, stable) and
        a list of corresponding trend strengths.

    Raises
    ------
    ValueError
        If the input lists (market_prices, market_volumes) are of different
        lengths or empty.

    Examples
    --------
    >>> market_prices = [100.0, 120.0, 110.0]
    >>> market_volumes = [1000, 1200, 1100]
    >>> trend_directions, trend_strengths = analyze_market_trends(market_prices,
    market_volumes)
    (['up', 'down', 'stable'], [0.8, 0.4, 0.1])

    >>> market_prices = [50.0, 55.0, 60.0]
    >>> market_volumes = [500, 550, 600]
    >>> trend_directions, trend_strengths = analyze_market_trends(market_prices,
    market_volumes)
    (['up', 'up', 'up'], [0.9, 0.95, 1.0])

    """
    return AnalyzeMarketTrendsOutput(
        trend_directions=[],
        trend_strengths=[],
    )