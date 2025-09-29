from ._analyze_market_trends.validate_market_data import validate_market_data
from ._analyze_market_trends.validate_volume_data import validate_volume_data
from ._analyze_market_trends.calculate_price_trends import calculate_price_trends
from ._analyze_market_trends.calculate_volume_trends import calculate_volume_trends
from ._analyze_market_trends.combine_trend_indicators import combine_trend_indicators
from ._analyze_market_trends.identify_price_patterns import identify_price_patterns
from ._analyze_market_trends.identify_volume_patterns import identify_volume_patterns
from ._analyze_market_trends.combine_pattern_results import combine_pattern_results

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
    trend_indicators: List[float] = (
        Field(..., description="List of indicators showing market trends.")
    )
    pattern_recognition_results: List[str] = (
        Field(..., description="List of identified patterns in the market data.")
    )


def analyze_market_trends(fetch_market_data_input: FetchMarketDataOutput, **kwargs) -> AnalyzeMarketTrendsOutput:
    """
    Analyze market data to identify trends and patterns.

    Parameters
    ----------
    market_prices : List[float]
        List of current market prices fetched from reliable sources.
    market_volumes : List[int]
        List of current market volumes fetched from reliable sources.

    Returns
    -------
    Tuple[List[float], List[str]]
        A tuple containing a list of trend indicators and a list of pattern
        recognition results.

    Raises
    ------
    ValueError
        If market_prices or market_volumes are empty or malformed.

    Examples
    --------
    >>> market_prices = [100.0, 105.0, 110.0, 115.0, 120.0]
    >>> market_volumes = [1000, 1200, 1500, 1800, 2000]
    >>> analyze_market_trends(market_prices, market_volumes)
    ([1.0, 1.2, 1.5, 1.8, 2.0], ['uptrend', 'increasing_volume'])

    >>> market_prices = [120.0, 115.0, 110.0, 105.0, 100.0]
    >>> market_volumes = [2000, 1800, 1500, 1200, 1000]
    >>> analyze_market_trends(market_prices, market_volumes)
    ([-1.0, -1.2, -1.5, -1.8, -2.0], ['downtrend', 'decreasing_volume'])

    """
    validated_prices: List[float] = validate_market_data(prices=fetch_market_data_input.market_prices, volumes=fetch_market_data_input.market_volumes)
    validated_volumes: List[int] = validate_volume_data(volumes=fetch_market_data_input.market_volumes)
    
    price_trends: List[float] = calculate_price_trends(prices=validated_prices)
    volume_trends: List[float] = calculate_volume_trends(volumes=validated_volumes)
    
    combined_indicators: List[float] = combine_trend_indicators(price_trends=price_trends, volume_trends=volume_trends)
    
    price_patterns: List[str] = identify_price_patterns(prices=validated_prices)
    volume_patterns: List[str] = identify_volume_patterns(volumes=validated_volumes)
    
    all_patterns: List[str] = combine_pattern_results(price_patterns=price_patterns, volume_patterns=volume_patterns)
    
    return AnalyzeMarketTrendsOutput(
        trend_indicators=combined_indicators,
        pattern_recognition_results=all_patterns
    )