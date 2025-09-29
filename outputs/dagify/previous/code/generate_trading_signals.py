from ._generate_trading_signals.validate_input_data import validate_input_data
from ._generate_trading_signals.generate_trend_based_signals import generate_trend_based_signals
from ._generate_trading_signals.generate_pattern_based_signals import generate_pattern_based_signals
from ._generate_trading_signals.generate_anomaly_based_signals import generate_anomaly_based_signals
from ._generate_trading_signals.analyze_price_momentum import analyze_price_momentum
from ._generate_trading_signals.analyze_volume_patterns import analyze_volume_patterns
from ._generate_trading_signals.analyze_economic_indicators import analyze_economic_indicators
from ._generate_trading_signals.combine_all_signals import combine_all_signals
from ._generate_trading_signals.filter_and_prioritize_signals import filter_and_prioritize_signals
from ._generate_trading_signals.calculate_signal_confidence import calculate_signal_confidence
from ._generate_trading_signals.validate_signal_generation import validate_signal_generation

from pydantic import BaseModel, Field
from typing import List


class AnalyzeMarketDataOutput(BaseModel):
    """Pydantic model for analyze_market_data node outputs."""
    trend_identification: List[str] = (
        Field(..., description="List of identified trends")
    )
    pattern_recognition: List[str] = (
        Field(..., description="List of recognized patterns")
    )
    anomaly_detection: List[str] = (
        Field(..., description="List of detected anomalies")
    )
    analysis_status: bool = (
        Field(..., description="Whether data analysis was successful")
    )


class CollectMarketDataOutput(BaseModel):
    """Pydantic model for collect_market_data node outputs."""
    stock_prices: List[float] = Field(..., description="List of stock prices")
    trading_volumes: List[int] = (
        Field(..., description="List of trading volumes")
    )
    economic_indicators: List[float] = (
        Field(..., description="List of economic indicators")
    )
    data_collection_status: bool = (
        Field(..., description="Whether data collection was successful")
    )


class GenerateTradingSignalsOutput(BaseModel):
    """Pydantic model for generate_trading_signals node outputs."""
    trading_signals: List[str] = (
        Field(..., description="List of generated trading signals")
    )
    signal_confidence: List[float] = (
        Field(..., description="List of confidence levels for each trading signal")
    )
    signal_generation_status: bool = (
        Field(..., description="Whether signal generation was successful")
    )


def generate_trading_signals(analyze_market_data_input: AnalyzeMarketDataOutput, collect_market_data_input: CollectMarketDataOutput, **kwargs) -> GenerateTradingSignalsOutput:
    """
    Generate trading signals based on analyzed market data, including stock
    prices, trading volumes, economic indicators, identified trends, recognized
    patterns, and detected anomalies.

    Parameters
    ----------
    market_data : dict
        Collected market data including stock prices, trading volumes, and
        economic indicators.
    analysis_results : dict
        Results of the market data analysis, including identified trends,
        recognized patterns, and detected anomalies.

    Returns
    -------
    Tuple[List[str], List[float], bool]
        A tuple containing the list of generated trading signals, their
        confidence levels, and the status of signal generation.

    Raises
    ------
    ValueError
        If the input data is incomplete or inconsistent.
    RuntimeError
        If there's an issue during signal generation.

    Examples
    --------
    >>> market_data = {'stock_prices': [100.0, 101.0], 'trading_volumes': [1000,
    1200], 'economic_indicators': [0.5, 0.6]}
    >>> analysis_results = {'trend_identification': ['uptrend'],
    'pattern_recognition': ['bullish'], 'anomaly_detection': ['none']}
    >>> generate_trading_signals(market_data, analysis_results)
    (['buy'], [0.8], True)

    >>> market_data = {'stock_prices': [100.0, 99.0], 'trading_volumes': [1000,
    800], 'economic_indicators': [0.5, 0.4]}
    >>> analysis_results = {'trend_identification': ['downtrend'],
    'pattern_recognition': ['bearish'], 'anomaly_detection': ['none']}
    >>> generate_trading_signals(market_data, analysis_results)
    (['sell'], [0.7], True)

    """
    validated_data: bool = validate_input_data(market_data=collect_market_data_input, analysis_results=analyze_market_data_input)
    
    if not validated_data:
        return GenerateTradingSignalsOutput(
            trading_signals=[],
            signal_confidence=[],
            signal_generation_status=False
        )
    
    trend_signals: List[str] = generate_trend_based_signals(trends=analyze_market_data_input.trend_identification)
    pattern_signals: List[str] = generate_pattern_based_signals(patterns=analyze_market_data_input.pattern_recognition)
    anomaly_signals: List[str] = generate_anomaly_based_signals(anomalies=analyze_market_data_input.anomaly_detection)
    
    price_momentum_signals: List[str] = analyze_price_momentum(prices=collect_market_data_input.stock_prices)
    volume_signals: List[str] = analyze_volume_patterns(volumes=collect_market_data_input.trading_volumes)
    economic_signals: List[str] = analyze_economic_indicators(indicators=collect_market_data_input.economic_indicators)
    
    combined_signals: List[str] = combine_all_signals(
        trend_signals=trend_signals,
        pattern_signals=pattern_signals,
        anomaly_signals=anomaly_signals,
        price_signals=price_momentum_signals,
        volume_signals=volume_signals,
        economic_signals=economic_signals
    )
    
    final_signals: List[str] = filter_and_prioritize_signals(signals=combined_signals)
    confidence_levels: List[float] = calculate_signal_confidence(
        signals=final_signals,
        market_data=collect_market_data_input,
        analysis_results=analyze_market_data_input
    )
    
    generation_status: bool = validate_signal_generation(signals=final_signals, confidence=confidence_levels)
    
    return GenerateTradingSignalsOutput(
        trading_signals=final_signals,
        signal_confidence=confidence_levels,
        signal_generation_status=generation_status
    )