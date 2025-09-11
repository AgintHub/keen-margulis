from pydantic import BaseModel, Field
from typing import List


class SelectTradingStrategyOutput(BaseModel):
    """Pydantic model for select_trading_strategy node outputs."""
    selected_strategy_name: str = Field(..., description="The name of the selected trading strategy.")
    strategy_principles: List[str] = Field(..., description="A list of key principles associated with the selected trading strategy.")
    strategy_metrics: List[str] = Field(..., description="A list of metrics used in the selected trading strategy.")


class DetermineTradingRulesOutput(BaseModel):
    """Pydantic model for determine_trading_rules node outputs."""
    entry_points: List[float] = Field(..., description="List of entry points for each trading instrument")
    exit_points: List[float] = Field(..., description="List of exit points for each trading instrument")
    stop_loss_levels: List[float] = Field(..., description="List of stop-loss levels for each trading instrument")
    position_sizing_strategy: str = Field(..., description="Description of the position sizing strategy")
    trading_rules_summary: str = Field(..., description="Summary of the determined trading rules")


def determine_trading_rules(select_trading_strategy_input: SelectTradingStrategyOutput, **kwargs) -> DetermineTradingRulesOutput:
    """
    Determine trading rules including entry and exit points, stop-loss levels,
    and position sizing based on a selected trading strategy.

    Parameters
    ----------
    selected_strategy : dict
        A dictionary containing the selected trading strategy details,
        including 'selected_strategy_name', 'strategy_principles', and
        'strategy_metrics'.

    Returns
    -------
    dict
        A dictionary containing the determined trading rules, including
        'entry_points', 'exit_points', 'stop_loss_levels',
        'position_sizing_strategy', and 'trading_rules_summary'.

    Raises
    ------
    ValueError
        If the selected trading strategy is invalid or does not contain
        required details.

    Examples
    --------
    >>> determine_trading_rules({'selected_strategy_name': 'Moving Average
    Crossover', 'strategy_principles': ['MA_50', 'MA_200'], 'strategy_metrics':
    [' Sharpe Ratio']})
    {'entry_points': [1.0, 2.0], 'exit_points': [3.0, 4.0], 'stop_loss_levels':
    [0.9, 1.9], 'position_sizing_strategy': 'Fixed Fractional',
    'trading_rules_summary': 'Based on Moving Average Crossover strategy'}

    """
    return DetermineTradingRulesOutput(
        entry_points=[],
        exit_points=[],
        stop_loss_levels=[],
        position_sizing_strategy="",
        trading_rules_summary="",
    )