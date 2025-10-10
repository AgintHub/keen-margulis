from ._evaluate_trading_strategies.validate_inputs import validate_inputs
from ._evaluate_trading_strategies.get_available_trading_strategies import get_available_trading_strategies
from ._evaluate_trading_strategies.evaluate_strategies_against_trends import evaluate_strategies_against_trends
from ._evaluate_trading_strategies.select_recommended_strategies import select_recommended_strategies

from pydantic import BaseModel, Field
from typing import List


class AnalyzeMarketTrendsOutput(BaseModel):
    """Pydantic model for analyze_market_trends node outputs."""
    trend_indicators: List[str] = (
        Field(..., description="Indicators of market trends (e.g., bullish, bearish)")
    )
    pattern_recognition: List[str] = (
        Field(..., description="Patterns recognized in the market data")
    )


class EvaluateTradingStrategiesOutput(BaseModel):
    """Pydantic model for evaluate_trading_strategies node outputs."""
    strategy_evaluations: List[str] = (
        Field(..., description="Evaluations of different trading strategies")
    )
    recommended_strategies: List[str] = (
        Field(..., description="Recommended trading strategies based on the evaluations")
    )


def evaluate_trading_strategies(analyze_market_trends_input: AnalyzeMarketTrendsOutput, **kwargs) -> EvaluateTradingStrategiesOutput:
    """
    Evaluate trading strategies based on market trend analysis.

    Parameters
    ----------
    trend_indicators : List[str]
        Indicators of market trends (e.g., bullish, bearish) from
        analyze_market_trends.
    pattern_recognition : List[str]
        Patterns recognized in the market data from analyze_market_trends.

    Returns
    -------
    Tuple[List[str], List[str]]
        A tuple containing the evaluations of different trading strategies
        and the recommended trading strategies.

    Raises
    ------
    ValueError
        If trend_indicators or pattern_recognition are empty or not
        provided.

    Examples
    --------
    >>> trend_indicators = ['bullish', 'bearish']
    >>> pattern_recognition = ['ascending triangle', 'descending triangle']
    >>> strategy_evaluations, recommended_strategies =
    evaluate_trading_strategies(trend_indicators, pattern_recognition)
    (['Strategy 1: Buy', 'Strategy 2: Sell'], ['Strategy 1', 'Strategy 3'])

    >>> trend_indicators = ['neutral']
    >>> pattern_recognition = ['symmetrical triangle']
    >>> strategy_evaluations, recommended_strategies =
    evaluate_trading_strategies(trend_indicators, pattern_recognition)
    (['Strategy 3: Hold'], ['Strategy 3'])

    """
    trend_indicators = analyze_market_trends_input.trend_indicators
    pattern_recognition = analyze_market_trends_input.pattern_recognition
    
    validate_inputs(trend_indicators=trend_indicators, pattern_recognition=pattern_recognition)
    
    available_strategies: List[str] = get_available_trading_strategies()
    
    strategy_evaluations: List[str] = evaluate_strategies_against_trends(
        strategies=available_strategies,
        trend_indicators=trend_indicators,
        pattern_recognition=pattern_recognition
    )
    
    recommended_strategies: List[str] = select_recommended_strategies(
        evaluations=strategy_evaluations,
        trend_indicators=trend_indicators,
        pattern_recognition=pattern_recognition
    )
    
    return EvaluateTradingStrategiesOutput(
        strategy_evaluations=strategy_evaluations,
        recommended_strategies=recommended_strategies
    )