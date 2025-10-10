from ._analyze_market_trends.validate_input_data import validate_input_data
from ._analyze_market_trends.preprocess_price_data import preprocess_price_data
from ._analyze_market_trends.preprocess_volume_data import preprocess_volume_data
from ._analyze_market_trends.preprocess_metrics_data import preprocess_metrics_data
from ._analyze_market_trends.analyze_price_trends import analyze_price_trends
from ._analyze_market_trends.analyze_volume_trends import analyze_volume_trends
from ._analyze_market_trends.analyze_metric_trends import analyze_metric_trends
from ._analyze_market_trends.combine_trend_predictions import combine_trend_predictions
from ._analyze_market_trends.calculate_confidence_levels import calculate_confidence_levels

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
    validate_input_data(stock_prices=gather_market_data_input.stock_prices, trading_volumes=gather_market_data_input.trading_volumes, market_metrics=gather_market_data_input.market_metrics)
    
    processed_price_data: List[float] = preprocess_price_data(prices=gather_market_data_input.stock_prices)
    processed_volume_data: List[float] = preprocess_volume_data(volumes=gather_market_data_input.trading_volumes)
    processed_metrics_data: List[float] = preprocess_metrics_data(metrics=gather_market_data_input.market_metrics)
    
    price_trends: List[str] = analyze_price_trends(price_data=processed_price_data)
    volume_trends: List[str] = analyze_volume_trends(volume_data=processed_volume_data)
    metric_trends: List[str] = analyze_metric_trends(metrics_data=processed_metrics_data)
    
    combined_predictions: List[str] = combine_trend_predictions(price_trends=price_trends, volume_trends=volume_trends, metric_trends=metric_trends)
    confidence_scores: List[float] = calculate_confidence_levels(price_data=processed_price_data, volume_data=processed_volume_data, metrics_data=processed_metrics_data, predictions=combined_predictions)
    
    return AnalyzeMarketTrendsOutput(
        trend_predictions=combined_predictions,
        trend_confidence=confidence_scores
    )