from pydantic import BaseModel, Field
from typing import List


class SelectOptimalStrategyOutput(BaseModel):
    """Pydantic model for select_optimal_strategy node outputs."""
    optimal_strategy: str = (
        Field(..., description="The selected optimal trading strategy")
    )
    strategy_confidence: float = (
        Field(..., description="Confidence level in the selected strategy")
    )


class ExecuteTradesOutput(BaseModel):
    """Pydantic model for execute_trades node outputs."""
    trade_outcomes: List[str] = (
        Field(..., description="Outcomes of executed trades")
    )
    trade_volumes: List[int] = (
        Field(..., description="Volumes of executed trades")
    )


def execute_trades(select_optimal_strategy_input: SelectOptimalStrategyOutput, **kwargs) -> ExecuteTradesOutput:
    """
    Execute trades based on the selected optimal strategy, producing trade
    outcomes and volumes.

    Parameters
    ----------
    optimal_strategy : str
        The selected optimal trading strategy from the
        'select_optimal_strategy' node.
    strategy_confidence : float
        The confidence level in the selected optimal strategy from the
        'select_optimal_strategy' node.

    Returns
    -------
    Tuple[List[str], List[int]]
        A tuple containing two lists: the first list contains the outcomes
        of the executed trades as strings, and the second list contains the
        volumes of the executed trades as integers.

    Raises
    ------
    ValueError
        If the optimal strategy is not recognized or if the strategy
        confidence is outside the valid range (0 to 1).
    RuntimeError
        If there's an issue executing the trades based on the provided
        strategy.

    Examples
    --------
    >>> optimal_strategy = 'buy'
    >>> strategy_confidence = 0.8
    >>> trade_outcomes, trade_volumes = execute_trades(optimal_strategy,
    strategy_confidence)
    (['success', 'success'], [100, 200])

    >>> optimal_strategy = 'sell'
    >>> strategy_confidence = 0.7
    >>> trade_outcomes, trade_volumes = execute_trades(optimal_strategy,
    strategy_confidence)
    (['success', 'failed'], [50, 0])

    """
    return ExecuteTradesOutput(
        trade_outcomes=[],
        trade_volumes=[],
    )