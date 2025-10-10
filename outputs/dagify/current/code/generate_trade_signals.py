from ._generate_trade_signals.validate_inputs import validate_inputs
from ._generate_trade_signals.generate_signals_from_trends import generate_signals_from_trends
from ._generate_trade_signals.calculate_signal_confidences import calculate_signal_confidences

from pydantic import BaseModel, Field
from typing import List


class AnalyzeMarketTrendsOutput(BaseModel):
    """Pydantic model for analyze_market_trends node outputs."""
    trend_indicators: List[float] = (
        Field(..., description="List of trend indicators")
    )
    trend_directions: List[str] = (
        Field(..., description="List of trend directions (up, down, neutral)")
    )


class GenerateTradeSignalsOutput(BaseModel):
    """Pydantic model for generate_trade_signals node outputs."""
    trade_signals: List[str] = (
        Field(..., description="List of trade signals (buy, sell, hold)")
    )
    signal_confidences: List[float] = (
        Field(..., description="List of signal confidences")
    )


def generate_trade_signals(analyze_market_trends_input: AnalyzeMarketTrendsOutput, **kwargs) -> GenerateTradeSignalsOutput:
    """
    Generate trade signals based on market trends and other factors.

    Parameters
    ----------
    trend_indicators : List[float]
        List of trend indicators from the analyze_market_trends node.
    trend_directions : List[str]
        List of trend directions (up, down, neutral) from the
        analyze_market_trends node.

    Returns
    -------
    Tuple[List[str], List[float]]
        A tuple containing a list of trade signals (buy, sell, hold) and a
        list of corresponding signal confidences.

    Raises
    ------
    ValueError
        If the lengths of trend_indicators and trend_directions do not
        match.
    TypeError
        If trend_indicators or trend_directions are not of the expected
        type.

    Examples
    --------
    >>> trend_indicators = [0.5, 0.7, 0.3]
    >>> trend_directions = ['up', 'down', 'neutral']
    >>> trade_signals, signal_confidences =
    generate_trade_signals(trend_indicators, trend_directions)
    (['buy', 'sell', 'hold'], [0.8, 0.9, 0.4])

    >>> trend_indicators = [0.2, 0.6]
    >>> trend_directions = ['down', 'up']
    >>> trade_signals, signal_confidences =
    generate_trade_signals(trend_indicators, trend_directions)
    (['sell', 'buy'], [0.7, 0.85])

    """
    validate_inputs(trend_indicators=analyze_market_trends_input.trend_indicators, trend_directions=analyze_market_trends_input.trend_directions)
    
    trade_signals: List[str] = generate_signals_from_trends(trend_indicators=analyze_market_trends_input.trend_indicators, trend_directions=analyze_market_trends_input.trend_directions)
    
    signal_confidences: List[float] = calculate_signal_confidences(trend_indicators=analyze_market_trends_input.trend_indicators, trend_directions=analyze_market_trends_input.trend_directions, trade_signals=trade_signals)
    
    return GenerateTradeSignalsOutput(trade_signals=trade_signals, signal_confidences=signal_confidences)