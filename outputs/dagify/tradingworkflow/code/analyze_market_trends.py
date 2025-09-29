from ._analyze_market_trends.validate_input_data import validate_input_data
from ._analyze_market_trends.preprocess_price_data import preprocess_price_data
from ._analyze_market_trends.preprocess_volume_data import preprocess_volume_data
from ._analyze_market_trends.analyze_price_trends import analyze_price_trends
from ._analyze_market_trends.analyze_volume_trends import analyze_volume_trends
from ._analyze_market_trends.analyze_other_metrics import analyze_other_metrics
from ._analyze_market_trends.combine_trend_indicators import combine_trend_indicators
from ._analyze_market_trends.determine_trend_directions import determine_trend_directions

from pydantic import BaseModel, Field
from typing import List


class CollectHistoricalMarketDataOutput(BaseModel):
    """Pydantic model for collect_historical_market_data node outputs."""
    historical_prices: List[float] = (
        Field(..., description="List of historical prices")
    )
    historical_volumes: List[float] = (
        Field(..., description="List of historical volumes")
    )
    other_metrics: List[str] = (
        Field(..., description="Other relevant historical metrics")
    )


class AnalyzeMarketTrendsOutput(BaseModel):
    """Pydantic model for analyze_market_trends node outputs."""
    trend_indicators: List[str] = (
        Field(..., description="List of trend indicators")
    )
    trend_directions: List[str] = (
        Field(..., description="List of trend directions")
    )


def analyze_market_trends(collect_historical_market_data_input: CollectHistoricalMarketDataOutput, **kwargs) -> AnalyzeMarketTrendsOutput:
    """
    Analyze historical market data to identify trends and patterns, returning
    trend indicators and directions.

    Parameters
    ----------
    historical_prices : List[float]
        List of historical prices from collect_historical_market_data
    historical_volumes : List[float]
        List of historical volumes from collect_historical_market_data
    other_metrics : List[str]
        Other relevant historical metrics from
        collect_historical_market_data

    Returns
    -------
    Tuple[List[str], List[str]]
        A tuple containing a list of trend indicators and a list of trend
        directions.

    Raises
    ------
    ValueError
        If historical_prices, historical_volumes, or other_metrics are empty
        or inconsistent.

    Examples
    --------
    >>> historical_prices = [100.0, 105.0, 110.0, 115.0, 120.0]
    >>> historical_volumes = [1000.0, 1200.0, 1500.0, 1800.0, 2000.0]
    >>> other_metrics = ['metric1', 'metric2', 'metric3', 'metric4', 'metric5']
    >>> trend_indicators, trend_directions =
    analyze_market_trends(historical_prices, historical_volumes, other_metrics)
    (['indicator1', 'indicator2'], ['up', 'up'])

    """
    validate_input_data(prices=collect_historical_market_data_input.historical_prices, volumes=collect_historical_market_data_input.historical_volumes, metrics=collect_historical_market_data_input.other_metrics)
    
    cleaned_prices: List[float] = preprocess_price_data(prices=collect_historical_market_data_input.historical_prices)
    cleaned_volumes: List[float] = preprocess_volume_data(volumes=collect_historical_market_data_input.historical_volumes)
    
    price_trends: List[str] = analyze_price_trends(prices=cleaned_prices)
    volume_trends: List[str] = analyze_volume_trends(volumes=cleaned_volumes)
    metric_indicators: List[str] = analyze_other_metrics(metrics=collect_historical_market_data_input.other_metrics)
    
    combined_indicators: List[str] = combine_trend_indicators(price_trends=price_trends, volume_trends=volume_trends, metric_indicators=metric_indicators)
    trend_directions: List[str] = determine_trend_directions(indicators=combined_indicators, prices=cleaned_prices, volumes=cleaned_volumes)
    
    return AnalyzeMarketTrendsOutput(trend_indicators=combined_indicators, trend_directions=trend_directions)