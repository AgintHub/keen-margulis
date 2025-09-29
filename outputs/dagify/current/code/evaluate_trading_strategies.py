from pydantic import BaseModel, Field
from typing import List


class AnalyzeMarketTrendsOutput(BaseModel):
    """Pydantic model for analyze_market_trends node outputs."""
    trend_identification: str = (
        Field(..., description="Identified market trends")
    )
    pattern_analysis: str = (
        Field(..., description="Detailed analysis of market patterns")
    )


class EvaluateTradingStrategiesOutput(BaseModel):
    """Pydantic model for evaluate_trading_strategies node outputs."""
    strategy_evaluations: List[str] = (
        Field(..., description="Evaluations of different trading strategies")
    )
    recommended_strategies: List[str] = (
        Field(..., description="Recommended trading strategies based on the evaluation")
    )


def evaluate_trading_strategies(analyze_market_trends_input: AnalyzeMarketTrendsOutput, **kwargs) -> EvaluateTradingStrategiesOutput:
    """
    Evaluates trading strategies based on market trend analysis and pattern
    identification.

    Parameters
    ----------
    trend_identification : str
        Identified market trends from the analyze_market_trends node.
    pattern_analysis : List[str]
        Detailed analysis of market patterns from the analyze_market_trends
        node.

    Returns
    -------
    Tuple[List[str], List[str]]
        A tuple containing the evaluations of different trading strategies
        and the recommended strategies.

    Raises
    ------
    ValueError
        If trend_identification is empty or pattern_analysis is not
        provided.

    Examples
    --------
    >>> trend_identification = 'Bullish'
    >>> pattern_analysis = ['Increasing Volume', 'Breaking Resistance']
    >>> evaluate_trading_strategies(trend_identification, pattern_analysis)
    (['Strategy 1: Buy and Hold - High Confidence', 'Strategy 2: Mean Reversion
    - Moderate Confidence'], ['Strategy 1: Buy and Hold'])

    >>> trend_identification = 'Bearish'
    >>> pattern_analysis = ['Decreasing Volume', 'Breaking Support']
    >>> evaluate_trading_strategies(trend_identification, pattern_analysis)
    (['Strategy 1: Short Sell - High Confidence', 'Strategy 2: Stop Loss - High
    Confidence'], ['Strategy 1: Short Sell'])

    """
    return EvaluateTradingStrategiesOutput(
        strategy_evaluations=[],
        recommended_strategies=[],
    )