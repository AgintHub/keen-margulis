from pydantic import BaseModel, Field
from typing import List


class CalculatePositionSizingOutput(BaseModel):
    """Pydantic model for calculate_position_sizing node outputs."""
    instrument_position_sizes: List[float] = Field(..., description="List of position sizes for each trading instrument")
    position_size_explanations: List[str] = Field(..., description="List of explanations for the factors that influence position sizing for each trading instrument")
    total_portfolio_value: float = Field(..., description="Total portfolio value after calculating position sizes")
    is_position_sizing_valid: bool = Field(..., description="Whether the calculated position sizes are valid and within allowed limits")


class ImplementOrderExecutionOutput(BaseModel):
    """Pydantic model for implement_order_execution node outputs."""
    order_execution_status: bool = Field(..., description="Whether the order execution was successful")
    executed_orders: List[str] = Field(..., description="List of executed orders, including order IDs and instrument symbols")
    entry_order_prices: List[float] = Field(..., description="List of entry order prices for each trading instrument")
    stop_loss_order_prices: List[float] = Field(..., description="List of stop-loss order prices for each trading instrument")
    profit_target_prices: List[float] = Field(..., description="List of profit target prices for each trading instrument")


def implement_order_execution(calculate_position_sizing_input: CalculatePositionSizingOutput, **kwargs) -> ImplementOrderExecutionOutput:
    """
    Implement the order execution logic for each trading instrument.

    Parameters
    ----------
    instrument_position_sizes : List[float]
        List of position sizes for each trading instrument
    entry_points : List[float]
        List of entry points for each trading instrument
    stop_loss_levels : List[float]
        List of stop-loss levels for each trading instrument
    profit_targets : List[float]
        List of profit targets for each trading instrument

    Returns
    -------
    dict
        A dictionary containing the order execution status, executed orders,
        entry order prices, stop-loss order prices, and profit target
        prices.

    Raises
    ------
    ValueError
        If the input lists are not of the same length.
    RuntimeError
        If an error occurs during order execution.

    Examples
    --------
    >>> instrument_position_sizes = [100.0, 200.0, 300.0]
    >>> entry_points = [10.0, 20.0, 30.0]
    >>> stop_loss_levels = [9.0, 19.0, 29.0]
    >>> profit_targets = [11.0, 21.0, 31.0]
    >>> implement_order_execution(instrument_position_sizes, entry_points,
    stop_loss_levels, profit_targets)
    {'order_execution_status': True, 'executed_orders': ['order1', 'order2',
    'order3'], 'entry_order_prices': [10.0, 20.0, 30.0],
    'stop_loss_order_prices': [9.0, 19.0, 29.0], 'profit_target_prices': [11.0,
    21.0, 31.0]}

    """
    return ImplementOrderExecutionOutput(
        order_execution_status=False,
        executed_orders=[],
        entry_order_prices=[],
        stop_loss_order_prices=[],
        profit_target_prices=[],
    )