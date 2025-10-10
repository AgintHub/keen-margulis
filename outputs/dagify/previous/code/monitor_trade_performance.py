from ._monitor_trade_performance.validate_trade_inputs import validate_trade_inputs
from ._monitor_trade_performance.calculate_success_rate import calculate_success_rate
from ._monitor_trade_performance.parse_trade_profits import parse_trade_profits
from ._monitor_trade_performance.calculate_average_profit import calculate_average_profit
from ._monitor_trade_performance.generate_performance_summary import generate_performance_summary

from pydantic import BaseModel, Field
from typing import List


class ExecuteTradesOutput(BaseModel):
    """Pydantic model for execute_trades node outputs."""
    trade_results: List[str] = (
        Field(..., description="Results of the executed trades")
    )
    trade_status: List[str] = (
        Field(..., description="Status of the executed trades (e.g., success, failure)")
    )


class MonitorTradePerformanceOutput(BaseModel):
    """Pydantic model for monitor_trade_performance node outputs."""
    performance_metrics: List[float] = (
        Field(..., description="Performance metrics for the executed trades")
    )
    performance_summary: str = (
        Field(..., description="Summary of the trade performance")
    )


def monitor_trade_performance(execute_trades_input: ExecuteTradesOutput, **kwargs) -> MonitorTradePerformanceOutput:
    """
    Monitors and analyzes the performance of executed trades based on the trade
    results and status from the 'execute_trades' node.

    Parameters
    ----------
    trade_results : List[str]
        Results of the executed trades from the 'execute_trades' node.
    trade_status : List[str]
        Status of the executed trades (e.g., success, failure) from the
        'execute_trades' node.

    Returns
    -------
    Tuple[List[float], str]
        A tuple containing performance metrics as a list of floats and a
        summary of the trade performance as a string.

    Raises
    ------
    ValueError
        If trade results or status are not provided or are invalid.

    Examples
    --------
    >>> trade_results = ['profit:100', 'loss:50']
    >>> trade_status = ['success', 'failure']
    >>> performance_metrics, performance_summary =
    monitor_trade_performance(trade_results, trade_status)
    [0.5, 100.0], 'Overall performance: 50% success rate, average profit: 100.0'

    >>> trade_results = ['profit:200', 'profit:150']
    >>> trade_status = ['success', 'success']
    >>> performance_metrics, performance_summary =
    monitor_trade_performance(trade_results, trade_status)
    [1.0, 175.0], 'Overall performance: 100% success rate, average profit:
    175.0'

    """
    validate_trade_inputs(trade_results=execute_trades_input.trade_results, trade_status=execute_trades_input.trade_status)
    
    success_rate: float = calculate_success_rate(trade_status=execute_trades_input.trade_status)
    
    parsed_profits: List[float] = parse_trade_profits(trade_results=execute_trades_input.trade_results)
    
    average_profit: float = calculate_average_profit(profits=parsed_profits)
    
    performance_metrics: List[float] = [success_rate, average_profit]
    
    performance_summary: str = generate_performance_summary(success_rate=success_rate, average_profit=average_profit)
    
    return MonitorTradePerformanceOutput(
        performance_metrics=performance_metrics,
        performance_summary=performance_summary
    )