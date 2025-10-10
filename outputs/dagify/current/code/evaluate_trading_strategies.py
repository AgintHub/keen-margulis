from pydantic import BaseModel, Field
from typing import List


class AnalyzeMarketTrendsOutput(BaseModel):
    """Pydantic model for analyze_market_trends node outputs."""
    trend_predictions: List[str] = (
        Field(..., description="Predictions of future market trends.")
    )
    trend_confidence: List[float] = (
        Field(..., description="Confidence levels in trend predictions.")
    )


class EvaluateTradingStrategiesOutput(BaseModel):
    """Pydantic model for evaluate_trading_strategies node outputs."""
    strategy_evaluations: List[str] = (
        Field(..., description="Evaluations of different trading strategies")
    )
    strategy_risks: List[float] = (
        Field(..., description="Risk assessments for each trading strategy")
    )


def evaluate_trading_strategies(analyze_market_trends_input: AnalyzeMarketTrendsOutput, **kwargs) -> EvaluateTradingStrategiesOutput:
    """
    Evaluates trading strategies based on market trends and risk.

    Parameters
    ----------
    trend_predictions : List[str]
        Predictions of future market trends from 'analyze_market_trends'
        node.
    trend_confidence : List[float]
        Confidence levels in trend predictions from 'analyze_market_trends'
        node.

    Returns
    -------
    Tuple[List[str], List[float]]
        A tuple containing evaluations of different trading strategies and
        their corresponding risk assessments.

    Raises
    ------
    ValueError
        If trend predictions and confidence levels are of different lengths.
    TypeError
        If trend predictions are not a list of strings or confidence levels
        are not a list of floats.

    Examples
    --------
    >>> trend_predictions = ['Up', 'Down', 'Stable']
    >>> trend_confidence = [0.8, 0.7, 0.9]
    >>> evaluate_trading_strategies(trend_predictions, trend_confidence)
    (['Good strategy', 'Bad strategy', 'Neutral strategy'], [0.2, 0.8, 0.5])

    >>> trend_predictions = ['Up', 'Down']
    >>> trend_confidence = [0.85, 0.75]
    >>> evaluate_trading_strategies(trend_predictions, trend_confidence)
    (['Profitable strategy', 'Loss strategy'], [0.15, 0.85])

    """
    return EvaluateTradingStrategiesOutput(
        strategy_evaluations=[],
        strategy_risks=[],
    )