from pydantic import BaseModel, Field
from typing import List


class EvaluateTradingStrategiesOutput(BaseModel):
    """Pydantic model for evaluate_trading_strategies node outputs."""
    strategy_evaluations: List[str] = (
        Field(..., description="Evaluations of different trading strategies")
    )
    strategy_risks: List[float] = (
        Field(..., description="Risk assessments for each trading strategy")
    )


class SelectOptimalStrategyOutput(BaseModel):
    """Pydantic model for select_optimal_strategy node outputs."""
    optimal_strategy: str = (
        Field(..., description="The selected optimal trading strategy")
    )
    strategy_confidence: float = (
        Field(..., description="Confidence level in the selected strategy")
    )


def select_optimal_strategy(evaluate_trading_strategies_input: EvaluateTradingStrategiesOutput, **kwargs) -> SelectOptimalStrategyOutput:
    """
    Selects the optimal trading strategy based on evaluations and risk
    assessments.

    Parameters
    ----------
    strategy_evaluations : List[str]
        Evaluations of different trading strategies from the
        'evaluate_trading_strategies' node.
    strategy_risks : List[float]
        Risk assessments for each trading strategy from the
        'evaluate_trading_strategies' node.

    Returns
    -------
    Tuple[str, float]
        A tuple containing the optimal trading strategy and its confidence
        level.

    Raises
    ------
    ValueError
        If the lengths of 'strategy_evaluations' and 'strategy_risks' do not
        match.

    Examples
    --------
    >>> strategy_evaluations = ['Good', 'Average', 'Poor']
    >>> strategy_risks = [0.1, 0.5, 0.8]
    >>> optimal_strategy, strategy_confidence =
    select_optimal_strategy(strategy_evaluations, strategy_risks)
    ('Good', 0.9)

    >>> strategy_evaluations = ['Average', 'Good', 'Poor']
    >>> strategy_risks = [0.5, 0.1, 0.8]
    >>> optimal_strategy, strategy_confidence =
    select_optimal_strategy(strategy_evaluations, strategy_risks)
    ('Good', 0.9)

    """
    return SelectOptimalStrategyOutput(
        optimal_strategy="",
        strategy_confidence=0.0,
    )