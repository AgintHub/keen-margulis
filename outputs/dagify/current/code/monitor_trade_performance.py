from pydantic import BaseModel, Field
from typing import List


class ExecuteTradesOutput(BaseModel):
    """Pydantic model for execute_trades node outputs."""
    trade_outcomes: List[str] = (
        Field(..., description="Outcomes of executed trades")
    )
    trade_volumes: List[int] = (
        Field(..., description="Volumes of executed trades")
    )


class MonitorTradePerformanceOutput(BaseModel):
    """Pydantic model for monitor_trade_performance node outputs."""
    performance_metrics: List[float] = (
        Field(..., description="Performance metrics of executed trades")
    )
    adjustment_recommendations: List[str] = (
        Field(..., description="Recommendations for strategy adjustments")
    )


def monitor_trade_performance(execute_trades_input: ExecuteTradesOutput, **kwargs) -> MonitorTradePerformanceOutput:
    """
    Monitor trade performance and provide strategy adjustment recommendations.

    Parameters
    ----------
    trade_outcomes : List[str]
        Outcomes of executed trades from the 'execute_trades' node.
    trade_volumes : List[int]
        Volumes of executed trades from the 'execute_trades' node.

    Returns
    -------
    Tuple[List[float], List[str]]
        A tuple containing performance metrics of executed trades and
        recommendations for strategy adjustments.

    Raises
    ------
    ValueError
        If trade outcomes or volumes are empty or mismatched.

    Examples
    --------
    >>> trade_outcomes = ['success', 'failure', 'success']
    >>> trade_volumes = [100, 200, 300]
    >>> monitor_trade_performance(trade_outcomes, trade_volumes)
    ([0.8, 0.2], ['Increase risk for successful trades', 'Review strategy for
    failed trades'])

    >>> trade_outcomes = ['success', 'success', 'success']
    >>> trade_volumes = [500, 600, 700]
    >>> monitor_trade_performance(trade_outcomes, trade_volumes)
    ([1.0], ['Continue current successful strategy'])

    """
    return MonitorTradePerformanceOutput(
        performance_metrics=[],
        adjustment_recommendations=[],
    )