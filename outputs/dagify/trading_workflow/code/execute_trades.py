from pydantic import BaseModel, Field
from typing import List


class MakeTradingDecisionsOutput(BaseModel):
    """Pydantic model for make_trading_decisions node outputs."""
    trading_decisions: List[str] = Field(..., description="Made trading decisions")
    decision_rationale: List[str] = Field(..., description="Rationale behind the trading decisions")


class ExecuteTradesOutput(BaseModel):
    """Pydantic model for execute_trades node outputs."""
    trade_execution_status: List[str] = Field(..., description="Status of trade executions")
    trade_outcomes: List[str] = Field(..., description="Outcomes of the executed trades")


def execute_trades(make_trading_decisions_input: MakeTradingDecisionsOutput, **kwargs) -> ExecuteTradesOutput:
    """
    Executes trades based on the provided trading decisions and returns the
    status and outcomes of these trades.

    Parameters
    ----------
    trading_decisions : List[str]
        Made trading decisions, output from 'make_trading_decisions' node.
    decision_rationale : List[str]
        Rationale behind the trading decisions, output from
        'make_trading_decisions' node.

    Returns
    -------
    {'trade_execution_status': List[str], 'trade_outcomes': List[str]}
        A dictionary containing two lists: 'trade_execution_status' for the
        status of trade executions and 'trade_outcomes' for the outcomes of
        the executed trades.

    Raises
    ------
    ValueError
        If the input lists ('trading_decisions' and 'decision_rationale')
        are not of the same length.
    RuntimeError
        If there is an issue during the execution of trades.

    Examples
    --------
    >>> trading_decisions = ['buy', 'sell', 'hold']
    >>> decision_rationale = ['good opportunity', 'bad market', 'wait for more
    info']
    >>> result = execute_trades(trading_decisions, decision_rationale)
    {'trade_execution_status': ['success', 'success', 'pending'],
    'trade_outcomes': ['profit', 'loss', 'awaiting']}

    >>> trading_decisions = ['buy']
    >>> decision_rationale = ['confident in market']
    >>> result = execute_trades(trading_decisions, decision_rationale)
    {'trade_execution_status': ['success'], 'trade_outcomes': ['profit']}

    """
    return ExecuteTradesOutput(
        trade_execution_status=[],
        trade_outcomes=[],
    )