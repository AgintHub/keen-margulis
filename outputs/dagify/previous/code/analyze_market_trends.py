from ._analyze_market_trends.validate_market_data import validate_market_data
from ._analyze_market_trends.calculate_technical_indicators import calculate_technical_indicators
from ._analyze_market_trends.determine_trend_directions import determine_trend_directions
from ._analyze_market_trends.normalize_trend_indicators import normalize_trend_indicators

from pydantic import BaseModel, Field
from typing import List


class FetchMarketDataOutput(BaseModel):
    """Pydantic model for fetch_market_data node outputs."""
    market_prices: List[float] = (
        Field(..., description="List of current market prices")
    )
    market_volumes: List[int] = (
        Field(..., description="List of current market volumes")
    )


class AnalyzeMarketTrendsOutput(BaseModel):
    """Pydantic model for analyze_market_trends node outputs."""
    trend_indicators: List[float] = (
        Field(..., description="List of trend indicators")
    )
    trend_directions: List[str] = (
        Field(..., description="List of trend directions (up, down, neutral)")
    )


def analyze_market_trends(fetch_market_data_input: FetchMarketDataOutput, **kwargs) -> AnalyzeMarketTrendsOutput:
    """
    Analyze market trends using historical data and technical indicators.

    Parameters
    ----------
    market_prices : List[float]
        List of current market prices from fetch_market_data node.
    market_volumes : List[int]
        List of current market volumes from fetch_market_data node.

    Returns
    -------
    Tuple[List[float], List[str]]
        A tuple containing a list of trend indicators and a list of trend
        directions.

    Raises
    ------
    ValueError
        If market_prices or market_volumes are empty or malformed.

    Examples
    --------
    >>> market_prices = [100.0, 120.0, 110.0]
    >>> market_volumes = [1000, 1200, 1100]
    >>> trend_indicators, trend_directions =
    analyze_market_trends(market_prices, market_volumes)
    ([1.2, 0.9, 1.1], ['up', 'down', 'up'])

    """
    validated_data: dict = validate_market_data(prices=fetch_market_data_input.market_prices, volumes=fetch_market_data_input.market_volumes)
    
    technical_indicators: List[float] = calculate_technical_indicators(prices=fetch_market_data_input.market_prices, volumes=fetch_market_data_input.market_volumes)
    
    trend_signals: List[str] = determine_trend_directions(indicators=technical_indicators, prices=fetch_market_data_input.market_prices)
    
    normalized_indicators: List[float] = normalize_trend_indicators(raw_indicators=technical_indicators)
    
    return AnalyzeMarketTrendsOutput(
        trend_indicators=normalized_indicators,
        trend_directions=trend_signals
    )