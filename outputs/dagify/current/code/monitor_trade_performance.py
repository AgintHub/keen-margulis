from ._monitor_trade_performance.validate_trade_data import validate_trade_data
from ._monitor_trade_performance.calculate_performance_metrics import calculate_performance_metrics
from ._monitor_trade_performance.extract_metrics_values import extract_metrics_values
from ._monitor_trade_performance.determine_strategy_adjustments import determine_strategy_adjustments

from pydantic import BaseModel, Field
from typing import List


class ExecuteTradesOutput(BaseModel):
    """Pydantic model for execute_trades node outputs."""
    trade_outcomes: List[str] = (
        Field(..., description="List of trade outcomes (success, failure)")
    )
    trade_ids: List[str] = Field(..., description="List of trade IDs")


class MonitorTradePerformanceOutput(BaseModel):
    """Pydantic model for monitor_trade_performance node outputs."""
    performance_metrics: List[float] = (
        Field(..., description="List of performance metrics (e.g. returns, Sharpe ratio)")
    )
    strategy_adjustments: List[str] = (
        Field(..., description="List of strategy adjustments made")
    )


def monitor_trade_performance(execute_trades_input: ExecuteTradesOutput, **kwargs) -> MonitorTradePerformanceOutput:
    """
    Monitor trade performance and adjust trading strategy.

    Parameters
    ----------
    trade_outcomes : List[str]
        List of trade outcomes (success, failure) from the execute_trades
        node.
    trade_ids : List[str]
        List of trade IDs from the execute_trades node.

    Returns
    -------
    Tuple[List[float], List[str]]
        A tuple containing a list of performance metrics and a list of
        strategy adjustments made.

    Raises
    ------
    ValueError
        If trade_outcomes or trade_ids are empty or mismatched in length.

    Examples
    --------
    >>> trade_outcomes = ['success', 'failure', 'success']
    >>> trade_ids = ['trade1', 'trade2', 'trade3']
    >>> monitor_trade_performance(trade_outcomes, trade_ids)
    ([0.05, 0.02], ['increased_risk', 'adjusted_stop_loss'])

    >>> trade_outcomes = ['success', 'success']
    >>> trade_ids = ['trade4', 'trade5']
    >>> monitor_trade_performance(trade_outcomes, trade_ids)
    ([0.03, 0.01], ['maintained_risk'])

    """
    validated_data = validate_trade_data(trade_outcomes=execute_trades_input.trade_outcomes, trade_ids=execute_trades_input.trade_ids)
    
    performance_data = calculate_performance_metrics(trade_outcomes=execute_trades_input.trade_outcomes, trade_ids=execute_trades_input.trade_ids)
    
    calculated_metrics: List[float] = extract_metrics_values(performance_data=performance_data)
    
    strategy_recommendations: List[str] = determine_strategy_adjustments(performance_metrics=calculated_metrics, trade_outcomes=execute_trades_input.trade_outcomes)
    
    return MonitorTradePerformanceOutput(
        performance_metrics=calculated_metrics,
        strategy_adjustments=strategy_recommendations
    )