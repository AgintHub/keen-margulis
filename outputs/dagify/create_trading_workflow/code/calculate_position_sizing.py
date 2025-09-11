from pydantic import BaseModel, Field
from typing import List


class DetermineTradingRulesOutput(BaseModel):
    """Pydantic model for determine_trading_rules node outputs."""
    entry_points: List[float] = Field(..., description="List of entry points for each trading instrument")
    exit_points: List[float] = Field(..., description="List of exit points for each trading instrument")
    stop_loss_levels: List[float] = Field(..., description="List of stop-loss levels for each trading instrument")
    position_sizing_strategy: str = Field(..., description="Description of the position sizing strategy")
    trading_rules_summary: str = Field(..., description="Summary of the determined trading rules")


class CalculatePositionSizingOutput(BaseModel):
    """Pydantic model for calculate_position_sizing node outputs."""
    instrument_position_sizes: List[float] = Field(..., description="List of position sizes for each trading instrument")
    position_size_explanations: List[str] = Field(..., description="List of explanations for the factors that influence position sizing for each trading instrument")
    total_portfolio_value: float = Field(..., description="Total portfolio value after calculating position sizes")
    is_position_sizing_valid: bool = Field(..., description="Whether the calculated position sizes are valid and within allowed limits")


def calculate_position_sizing(determine_trading_rules_input: DetermineTradingRulesOutput, **kwargs) -> CalculatePositionSizingOutput:
    """
    Calculates the position sizing for each trading instrument based on the
    trading rules and strategy.

    Parameters
    ----------
    trading_rules : dict
        Trading rules determined by the determine_trading_rules node,
        including entry_points, exit_points, stop_loss_levels,
        position_sizing_strategy, and trading_rules_summary.
    trading_instruments : List[str]
        List of trading instruments identified for inclusion in the
        workflow.

    Returns
    -------
    dict
        A dictionary containing instrument_position_sizes,
        position_size_explanations, total_portfolio_value, and
        is_position_sizing_valid.

    Raises
    ------
    ValueError
        If the trading rules or instruments are invalid.

    Examples
    --------
    >>> trading_rules = {
    ...     'entry_points': [10.0, 20.0],
    ...     'exit_points': [15.0, 25.0],
    ...     'stop_loss_levels': [9.0, 19.0],
    ...     'position_sizing_strategy': 'fixed',
    ...     'trading_rules_summary': 'Example trading rules'
    >>> }
    >>> trading_instruments = ['Instrument1', 'Instrument2']
    >>> calculate_position_sizing(trading_rules, trading_instruments)
    {'instrument_position_sizes': [100.0, 200.0], 'position_size_explanations':
    ['Fixed position size of 100.0', 'Fixed position size of 200.0'],
    'total_portfolio_value': 300.0, 'is_position_sizing_valid': True}

    """
    return CalculatePositionSizingOutput(
        instrument_position_sizes=[],
        position_size_explanations=[],
        total_portfolio_value=0.0,
        is_position_sizing_valid=False,
    )