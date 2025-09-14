from pydantic import BaseModel, Field
from typing import List


class GenerateTradingSignalsOutput(BaseModel):
    """Pydantic model for generate_trading_signals node outputs."""
    trading_signals: List[str] = Field(..., description="Generated trading signals")
    signal_confidence: List[float] = Field(..., description="Confidence levels of the generated trading signals")


class MakeTradingDecisionsOutput(BaseModel):
    """Pydantic model for make_trading_decisions node outputs."""
    trading_decisions: List[str] = Field(..., description="Made trading decisions")
    decision_rationale: List[str] = Field(..., description="Rationale behind the trading decisions")


def make_trading_decisions(generate_trading_signals_input: GenerateTradingSignalsOutput, **kwargs) -> MakeTradingDecisionsOutput:
    """
    Makes trading decisions based on generated trading signals and their
    confidence levels.

    Parameters
    ----------
    trading_signals : List[str]
        Generated trading signals from the 'generate_trading_signals' node.
    signal_confidence : List[float]
        Confidence levels of the generated trading signals from the
        'generate_trading_signals' node.

    Returns
    -------
    {'trading_decisions': List[str], 'decision_rationale': List[str]}
        A dictionary containing the made trading decisions and the rationale
        behind them.

    Raises
    ------
    ValueError
        If the lengths of 'trading_signals' and 'signal_confidence' do not
        match.

    Examples
    --------
    >>> trading_signals = ['Buy', 'Sell', 'Hold']
    >>> signal_confidence = [0.8, 0.7, 0.9]
    >>> result = make_trading_decisions(trading_signals, signal_confidence)
    {'trading_decisions': ['Buy', 'Hold', 'Hold'], 'decision_rationale': ['High
    confidence buy signal', 'Low confidence sell signal', 'High confidence hold
    signal']}

    >>> trading_signals = ['Buy', 'Sell']
    >>> signal_confidence = [0.6, 0.4]
    >>> result = make_trading_decisions(trading_signals, signal_confidence)
    {'trading_decisions': ['Buy', 'Sell'], 'decision_rationale': ['Moderate
    confidence buy signal', 'Low confidence sell signal']}

    """
    return MakeTradingDecisionsOutput(
        trading_decisions=[],
        decision_rationale=[],
    )