from pydantic import BaseModel, Field
from typing import List


class ImplementTradingRiskManagementOutput(BaseModel):
    """Pydantic model for implement_trading_risk_management node outputs."""
    value_at_risk: float = Field(..., description="The calculated Value at Risk (VaR) for the trading workflow.")
    expected_shortfall: float = Field(..., description="The calculated Expected Shortfall (ES) for the trading workflow.")
    potential_future_exposure: float = Field(..., description="The calculated Potential Future Exposure (PFE) for the trading workflow.")
    risk_metrics_explanation: str = Field(..., description="An explanation of the risk metrics used in the implementation of trading risk management.")


class EvaluateTradingPerformanceOutput(BaseModel):
    """Pydantic model for evaluate_trading_performance node outputs."""
    total_profit_loss: float = Field(..., description="The total profit or loss from the trading workflow")
    max_drawdown: float = Field(..., description="The maximum drawdown experienced during the trading period")
    trading_metrics: List[str] = Field(..., description="List of other relevant trading metrics (e.g., Sharpe ratio, Sortino ratio)")
    performance_evaluation: str = Field(..., description="An explanation of the evaluation methods used and overall performance assessment")
    is_performance_satisfactory: bool = Field(..., description="Whether the trading performance is satisfactory based on predefined criteria")


def evaluate_trading_performance(implement_trading_risk_management_input: ImplementTradingRiskManagementOutput, **kwargs) -> EvaluateTradingPerformanceOutput:
    """
    Evaluates the trading performance of a trading workflow.

    Parameters
    ----------
    trading_workflow_data : dict
        Trading workflow data, including profit and loss, drawdowns, and
        other trading metrics.
    risk_management_data : dict
        Risk management data from the implement_trading_risk_management
        node.

    Returns
    -------
    dict
        A dictionary containing the total profit or loss, maximum drawdown,
        trading metrics, performance evaluation, and whether the performance
        is satisfactory.

    Raises
    ------
    ValueError
        If the input trading workflow data or risk management data is
        invalid or incomplete.

    Examples
    --------
    >>> evaluate_trading_performance(trading_workflow_data={'profit_loss':
    1000.0, 'drawdowns': [0.1, 0.2]}, risk_management_data={'value_at_risk':
    0.05, 'expected_shortfall': 0.03})
    {'total_profit_loss': 1000.0, 'max_drawdown': 0.2, 'trading_metrics':
    ['Sharpe ratio: 1.2', 'Sortino ratio: 1.1'], 'performance_evaluation': 'The
    trading performance is satisfactory.', 'is_performance_satisfactory': True}

    """
    return EvaluateTradingPerformanceOutput(
        total_profit_loss=0.0,
        max_drawdown=0.0,
        trading_metrics=[],
        performance_evaluation="",
        is_performance_satisfactory=False,
    )