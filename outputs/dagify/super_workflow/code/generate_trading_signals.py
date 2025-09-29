from ._generate_trading_signals.validate_input_lengths import validate_input_lengths
from ._generate_trading_signals.validate_value_ranges import validate_value_ranges
from ._generate_trading_signals.generate_signals_from_trends_and_patterns import generate_signals_from_trends_and_patterns
from ._generate_trading_signals.adjust_signals_for_risk import adjust_signals_for_risk
from ._generate_trading_signals.calculate_signal_confidence import calculate_signal_confidence

from pydantic import BaseModel, Field
from typing import List


class AnalyzeMarketTrendsOutput(BaseModel):
    """Pydantic model for analyze_market_trends node outputs."""
    trend_indicators: List[float] = (
        Field(..., description="List of indicators showing market trends.")
    )
    pattern_recognition_results: List[str] = (
        Field(..., description="List of identified patterns in the market data.")
    )


class AssessRiskOutput(BaseModel):
    """Pydantic model for assess_risk node outputs."""
    risk_levels: List[float] = (
        Field(..., description="List of risk levels associated with different trades.")
    )
    risk_factors: List[str] = (
        Field(..., description="List of factors contributing to the risk assessment.")
    )


class GenerateTradingSignalsOutput(BaseModel):
    """Pydantic model for generate_trading_signals node outputs."""
    trading_signals: List[str] = (
        Field(..., description="List of trading signals (buy/sell/hold).")
    )
    signal_confidence: List[float] = (
        Field(..., description="List of confidence levels for each trading signal.")
    )


def generate_trading_signals(analyze_market_trends_input: AnalyzeMarketTrendsOutput, assess_risk_input: AssessRiskOutput, **kwargs) -> GenerateTradingSignalsOutput:
    """
    Generate trading signals based on analyzed trends and risk assessment.

    Parameters
    ----------
    trend_indicators : List[float]
        List of indicators showing market trends from the
        analyze_market_trends node.
    pattern_recognition_results : List[str]
        List of identified patterns in the market data from the
        analyze_market_trends node.
    risk_levels : List[float]
        List of risk levels associated with different trades from the
        assess_risk node.
    risk_factors : List[str]
        List of factors contributing to the risk assessment from the
        assess_risk node.

    Returns
    -------
    Tuple[List[str], List[float]]
        A tuple containing a list of trading signals and a list of their
        confidence levels.

    Raises
    ------
    ValueError
        If the input lists are of different lengths or if the trend
        indicators or risk levels are out of expected ranges.

    Examples
    --------
    >>> trend_indicators = [0.5, 0.7, 0.3]
    >>> pattern_recognition_results = ['uptrend', 'downtrend', 'uptrend']
    >>> risk_levels = [0.2, 0.5, 0.1]
    >>> risk_factors = ['volatility', 'economic indicators', 'market sentiment']
    >>> trading_signals, signal_confidence =
    generate_trading_signals(trend_indicators, pattern_recognition_results,
    risk_levels, risk_factors)
    (['buy', 'sell', 'hold'], [0.8, 0.6, 0.9])

    """
    validate_input_lengths(trend_indicators=analyze_market_trends_input.trend_indicators, pattern_results=analyze_market_trends_input.pattern_recognition_results, risk_levels=assess_risk_input.risk_levels, risk_factors=assess_risk_input.risk_factors)
    validate_value_ranges(trend_indicators=analyze_market_trends_input.trend_indicators, risk_levels=assess_risk_input.risk_levels)
    
    trading_signals: List[str] = generate_signals_from_trends_and_patterns(trend_indicators=analyze_market_trends_input.trend_indicators, patterns=analyze_market_trends_input.pattern_recognition_results)
    risk_adjusted_signals: List[str] = adjust_signals_for_risk(signals=trading_signals, risk_levels=assess_risk_input.risk_levels, risk_factors=assess_risk_input.risk_factors)
    confidence_levels: List[float] = calculate_signal_confidence(trend_indicators=analyze_market_trends_input.trend_indicators, patterns=analyze_market_trends_input.pattern_recognition_results, risk_levels=assess_risk_input.risk_levels)
    
    return GenerateTradingSignalsOutput(trading_signals=risk_adjusted_signals, signal_confidence=confidence_levels)