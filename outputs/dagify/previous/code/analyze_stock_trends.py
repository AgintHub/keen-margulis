from ._analyze_stock_trends.validate_input_data import validate_input_data
from ._analyze_stock_trends.identify_price_trends import identify_price_trends
from ._analyze_stock_trends.analyze_volume_patterns import analyze_volume_patterns
from ._analyze_stock_trends.combine_trend_patterns import combine_trend_patterns
from ._analyze_stock_trends.detect_anomalies import detect_anomalies

from pydantic import BaseModel, Field
from typing import List


class CollectStockDataOutput(BaseModel):
    """Pydantic model for collect_stock_data node outputs."""
    stock_symbols: List[str] = (
        Field(..., description="List of stock symbols analyzed")
    )
    historical_prices: List[float] = (
        Field(..., description="Historical stock prices for each symbol")
    )
    trading_volumes: List[int] = (
        Field(..., description="Trading volumes for each stock symbol")
    )


class ProcessStockDataOutput(BaseModel):
    """Pydantic model for process_stock_data node outputs."""
    cleaned_stock_data: List[float] = (
        Field(..., description="Preprocessed stock price data")
    )
    normalized_volumes: List[float] = (
        Field(..., description="Normalized trading volumes")
    )


class AnalyzeStockTrendsOutput(BaseModel):
    """Pydantic model for analyze_stock_trends node outputs."""
    trend_analysis: List[str] = (
        Field(..., description="List of identified trends and patterns")
    )
    anomaly_detected: bool = (
        Field(..., description="Whether any anomalies were detected")
    )


def analyze_stock_trends(collect_stock_data_input: CollectStockDataOutput, process_stock_data_input: ProcessStockDataOutput, **kwargs) -> AnalyzeStockTrendsOutput:
    """
    Analyze preprocessed stock data to identify trends, patterns, and anomalies.

    Parameters
    ----------
    cleaned_stock_data : List[float]
        Preprocessed stock price data from process_stock_data node
    normalized_volumes : List[float]
        Normalized trading volumes from process_stock_data node

    Returns
    -------
    Tuple[List[str], bool]
        A tuple containing a list of identified trends and patterns, and a
        boolean indicating whether any anomalies were detected

    Raises
    ------
    ValueError
        If cleaned_stock_data or normalized_volumes are empty or malformed

    Examples
    --------
    >>> cleaned_stock_data = [100.0, 102.0, 101.0, 103.0, 105.0]
    >>> normalized_volumes = [0.5, 0.6, 0.4, 0.7, 0.8]
    >>> result = analyze_stock_trends(cleaned_stock_data, normalized_volumes)
    (['Uptrend', 'Increasing Volume'], True)

    >>> cleaned_stock_data = [50.0, 49.0, 48.0, 47.0, 46.0]
    >>> normalized_volumes = [0.3, 0.2, 0.1, 0.4, 0.5]
    >>> result = analyze_stock_trends(cleaned_stock_data, normalized_volumes)
    (['Downtrend', 'Mixed Volume'], False)

    """
    validate_input_data(cleaned_data=process_stock_data_input.cleaned_stock_data, volumes=process_stock_data_input.normalized_volumes)
    
    price_trends: List[str] = identify_price_trends(stock_prices=process_stock_data_input.cleaned_stock_data)
    volume_patterns: List[str] = analyze_volume_patterns(volumes=process_stock_data_input.normalized_volumes)
    
    combined_trends: List[str] = combine_trend_patterns(price_trends=price_trends, volume_patterns=volume_patterns)
    
    anomalies_found: bool = detect_anomalies(stock_data=process_stock_data_input.cleaned_stock_data, volumes=process_stock_data_input.normalized_volumes)
    
    return AnalyzeStockTrendsOutput(
        trend_analysis=combined_trends,
        anomaly_detected=anomalies_found
    )