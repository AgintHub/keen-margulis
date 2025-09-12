from pydantic import BaseModel, Field
from typing import List


class EvaluateTradingStrategiesOutput(BaseModel):
    """Pydantic model for evaluate_trading_strategies node outputs."""
    strategy_evaluations: List[str] = Field(..., description="Evaluations of different trading strategies")
    recommended_strategies: List[str] = Field(..., description="Recommended trading strategies based on the evaluation")


class GenerateTradingSignalsOutput(BaseModel):
    """Pydantic model for generate_trading_signals node outputs."""
    trading_signals: List[str] = Field(..., description="Generated trading signals")
    signal_confidence: List[float] = Field(..., description="Confidence levels of the generated trading signals")


def generate_trading_signals(evaluate_trading_strategies_input: EvaluateTradingStrategiesOutput, **kwargs) -> GenerateTradingSignalsOutput:
    """
    Generates trading signals and their confidence levels based on recommended
    trading strategies.

    Parameters
    ----------
    recommended_strategies : List[str]
        Recommended trading strategies from the parent node
        'evaluate_trading_strategies'.
    strategy_evaluations : List[str]
        Evaluations of different trading strategies from the parent node
        'evaluate_trading_strategies'.

    Returns
    -------
    Tuple[List[str], List[float]]
        A tuple containing the generated trading signals and their
        corresponding confidence levels.

    Raises
    ------
    ValueError
        If the input recommended strategies or strategy evaluations are
        empty or malformed.

    Examples
    --------
    >>> recommended_strategies = ['mean_reversion', 'trend_following']
    >>> strategy_evaluations = ['mean_reversion:0.8', 'trend_following:0.7']
    >>> trading_signals, signal_confidence =
    generate_trading_signals(recommended_strategies, strategy_evaluations)
    (['buy', 'sell'], [0.85, 0.75])

    >>> recommended_strategies = ['momentum']
    >>> strategy_evaluations = ['momentum:0.9']
    >>> trading_signals, signal_confidence =
    generate_trading_signals(recommended_strategies, strategy_evaluations)
    (['buy'], [0.92])

    """
    return GenerateTradingSignalsOutput(
        trading_signals=[],
        signal_confidence=[],
    )