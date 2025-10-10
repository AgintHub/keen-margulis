from ._monitor_trades.validate_trade_execution_input import validate_trade_execution_input
from ._monitor_trades.parse_trade_details import parse_trade_details
from ._monitor_trades.analyze_trade_performance import analyze_trade_performance
from ._monitor_trades.generate_strategy_adjustments import generate_strategy_adjustments
from ._monitor_trades.update_monitoring_status import update_monitoring_status

from pydantic import BaseModel, Field
from typing import List


class ExecuteTradesOutput(BaseModel):
    """Pydantic model for execute_trades node outputs."""
    trade_execution_status: bool = (
        Field(..., description="Whether trade execution was successful")
    )
    trade_details: List[str] = (
        Field(..., description = (
            "List of trade details, including trade type, quantity, and price")
        )
    )


class MonitorTradesOutput(BaseModel):
    """Pydantic model for monitor_trades node outputs."""
    trade_monitoring_status: bool = (
        Field(..., description="Whether trade monitoring was successful")
    )
    strategy_adjustments: List[str] = (
        Field(..., description = (
            "List of adjustments made to the trading strategy")
        )
    )


def monitor_trades(execute_trades_input: ExecuteTradesOutput, **kwargs) -> MonitorTradesOutput:
    """
    Monitor trades and adjust the trading strategy as needed based on the trade
    execution status and trade details.

    Parameters
    ----------
    trade_execution_status : bool
        Whether trade execution was successful, received from
        'execute_trades' node.
    trade_details : List[str]
        List of trade details including trade type, quantity, and price,
        received from 'execute_trades' node.

    Returns
    -------
    Tuple[bool, List[str]]
        A tuple containing a boolean indicating whether trade monitoring was
        successful and a list of adjustments made to the trading strategy.

    Raises
    ------
    ValueError
        If trade execution status is False or trade details are empty or
        malformed.

    Examples
    --------
    >>> trade_execution_status = True
    >>> trade_details = ['Buy:100:AAPL:150.0', 'Sell:50:GOOG:2500.0']
    >>> monitor_trades(trade_execution_status, trade_details)
    (True, ['Adjusted risk tolerance', 'Updated position sizing'])

    >>> trade_execution_status = False
    >>> trade_details = []
    >>> monitor_trades(trade_execution_status, trade_details)
    (False, [])

    """
    validated_input: bool = validate_trade_execution_input(status=execute_trades_input.trade_execution_status, details=execute_trades_input.trade_details)
    
    if not validated_input:
        monitoring_status: bool = False
        adjustments: List[str] = []
    else:
        parsed_trade_data: List[dict] = parse_trade_details(trade_details=execute_trades_input.trade_details)
        performance_metrics: dict = analyze_trade_performance(trade_data=parsed_trade_data)
        strategy_recommendations: List[str] = generate_strategy_adjustments(performance=performance_metrics, execution_status=execute_trades_input.trade_execution_status)
        monitoring_status: bool = update_monitoring_status(adjustments=strategy_recommendations)
        adjustments: List[str] = strategy_recommendations
    
    return MonitorTradesOutput(
        trade_monitoring_status=monitoring_status,
        strategy_adjustments=adjustments
    )