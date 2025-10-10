from ._analyze_market_trends.validate_input_data import validate_input_data
from ._analyze_market_trends.normalize_market_data import normalize_market_data
from ._analyze_market_trends.analyze_price_trends import analyze_price_trends
from ._analyze_market_trends.analyze_volume_indicators import analyze_volume_indicators
from ._analyze_market_trends.combine_trend_indicators import combine_trend_indicators
from ._analyze_market_trends.identify_chart_patterns import identify_chart_patterns

from pydantic import BaseModel, Field
from typing import List


class GatherMarketDataOutput(BaseModel):
    """Pydantic model for gather_market_data node outputs."""
    current_prices: List[float] = (
        Field(..., description="Current prices of the assets")
    )
    historical_prices: List[float] = (
        Field(..., description="Historical price data for the assets over a specified period")
    )
    trading_volumes: List[float] = (
        Field(..., description="Trading volumes for the assets")
    )


class AnalyzeMarketTrendsOutput(BaseModel):
    """Pydantic model for analyze_market_trends node outputs."""
    trend_indicators: List[str] = (
        Field(..., description="Indicators of market trends (e.g., bullish, bearish)")
    )
    pattern_recognition: List[str] = (
        Field(..., description="Patterns recognized in the market data")
    )


def analyze_market_trends(gather_market_data_input: GatherMarketDataOutput, **kwargs) -> AnalyzeMarketTrendsOutput:
    """
    Analyzes market trends based on gathered data.

    Parameters
    ----------
    current_prices : List[float]
        Current prices of the assets gathered by the gather_market_data
        node.
    historical_prices : List[float]
        Historical price data for the assets over a specified period
        gathered by the gather_market_data node.
    trading_volumes : List[float]
        Trading volumes for the assets gathered by the gather_market_data
        node.

    Returns
    -------
    Tuple[List[str], List[str]]
        A tuple containing a list of trend indicators and a list of
        recognized patterns in the market data.

    Raises
    ------
    ValueError
        If any of the input lists (current_prices, historical_prices,
        trading_volumes) are empty or of different lengths.

    Examples
    --------
    >>> current_prices = [100.0, 120.0, 110.0]
    >>> historical_prices = [90.0, 100.0, 110.0, 120.0]
    >>> trading_volumes = [1000.0, 1200.0, 1100.0]
    >>> trend_indicators, pattern_recognition =
    analyze_market_trends(current_prices, historical_prices, trading_volumes)
    (['bullish'], ['ascending triangle'])

    >>> current_prices = [100.0, 80.0, 90.0]
    >>> historical_prices = [110.0, 100.0, 90.0, 80.0]
    >>> trading_volumes = [1000.0, 800.0, 900.0]
    >>> trend_indicators, pattern_recognition =
    analyze_market_trends(current_prices, historical_prices, trading_volumes)
    (['bearish'], ['descending triangle'])

    """
    validate_input_data(current_prices=gather_market_data_input.current_prices, 
                         historical_prices=gather_market_data_input.historical_prices, 
                         trading_volumes=gather_market_data_input.trading_volumes)
    
    normalized_data: dict = normalize_market_data(current_prices=gather_market_data_input.current_prices,
                                                   historical_prices=gather_market_data_input.historical_prices,
                                                   trading_volumes=gather_market_data_input.trading_volumes)
    
    price_trends: List[str] = analyze_price_trends(current_prices=gather_market_data_input.current_prices,
                                                     historical_prices=gather_market_data_input.historical_prices)
    
    volume_indicators: List[str] = analyze_volume_indicators(trading_volumes=gather_market_data_input.trading_volumes,
                                                              price_data=gather_market_data_input.current_prices)
    
    combined_indicators: List[str] = combine_trend_indicators(price_trends=price_trends, 
                                                               volume_trends=volume_indicators)
    
    chart_patterns: List[str] = identify_chart_patterns(current_prices=gather_market_data_input.current_prices,
                                                          historical_prices=gather_market_data_input.historical_prices,
                                                          volumes=gather_market_data_input.trading_volumes)
    
    return AnalyzeMarketTrendsOutput(trend_indicators=combined_indicators, pattern_recognition=chart_patterns)