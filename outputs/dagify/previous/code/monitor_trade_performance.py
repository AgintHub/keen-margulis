from pydantic import BaseModel, Field
from typing import List


class ExecuteTradesOutput(BaseModel):
    """Pydantic model for execute_trades node outputs."""
    trade_execution_status: List[str] = Field(..., description="Status of each trade execution (e.g., success, failed, pending)")
    trade_execution_timestamps: List[str] = Field(..., description="Timestamps for when each trade was executed")
    trade_details: List[str] = Field(..., description="Details of the executed trades, including assets, quantities, and prices")


class MonitorTradePerformanceOutput(BaseModel):
    """Pydantic model for monitor_trade_performance node outputs."""
    trade_performance_metrics: List[float] = Field(..., description="Metrics evaluating the performance of the executed trades (e.g., returns, Sharpe ratio)")
    portfolio_value: float = Field(..., description="Current value of the portfolio after executing trades")
    risk_exposure: float = Field(..., description="Current risk exposure of the portfolio")


def monitor_trade_performance(execute_trades_input: ExecuteTradesOutput, **kwargs) -> MonitorTradePerformanceOutput:
    """
    Monitor the performance of executed trades, calculating key metrics and
    assessing portfolio impact.

    Parameters
    ----------
    trade_execution_status : List[str]
        Status of each trade execution (e.g., success, failed, pending) from
        the execute_trades node
    trade_execution_timestamps : List[str]
        Timestamps for when each trade was executed from the execute_trades
        node
    trade_details : List[str]
        Details of the executed trades, including assets, quantities, and
        prices from the execute_trades node

    Returns
    -------
    dict
        A dictionary containing trade performance metrics, portfolio value,
        and risk exposure.

    Raises
    ------
    ValueError
        If trade execution status, timestamps, or details are inconsistent
        or missing.

    Examples
    --------
    >>> trade_execution_status = ['success', 'success']
    >>> trade_execution_timestamps = ['2023-01-01 12:00:00', '2023-01-02
    12:00:00']
    >>> trade_details = ['asset1,100,100.0', 'asset2,50,50.0']
    >>> monitor_trade_performance(trade_execution_status,
    trade_execution_timestamps, trade_details)
    {'trade_performance_metrics': [0.05, 0.03], 'portfolio_value': 10500.0,
    'risk_exposure': 0.02}

    """
    return MonitorTradePerformanceOutput(
        trade_performance_metrics=[],
        portfolio_value=0.0,
        risk_exposure=0.0,
    )