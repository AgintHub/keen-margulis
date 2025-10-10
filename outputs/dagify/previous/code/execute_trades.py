from ._execute_trades.validate_input_lengths import validate_input_lengths
from ._execute_trades.execute_single_trade import execute_single_trade
from ._execute_trades.determine_trade_status import determine_trade_status

from pydantic import BaseModel, Field
from typing import List


class GenerateTradingSignalsOutput(BaseModel):
    """Pydantic model for generate_trading_signals node outputs."""
    trading_signals: List[str] = (
        Field(..., description="Generated trading signals")
    )
    signal_confidence: List[float] = (
        Field(..., description="Confidence levels for the generated trading signals")
    )


class ExecuteTradesOutput(BaseModel):
    """Pydantic model for execute_trades node outputs."""
    trade_results: List[str] = (
        Field(..., description="Results of the executed trades")
    )
    trade_status: List[str] = (
        Field(..., description="Status of the executed trades (e.g., success, failure)")
    )


def execute_trades(generate_trading_signals_input: GenerateTradingSignalsOutput, **kwargs) -> ExecuteTradesOutput:
    """
    Execute trades according to the generated trading signals and return the
    results and status of the trades.

    Parameters
    ----------
    trading_signals : List[str]
        Generated trading signals (buy/sell/hold) from the parent node
        'generate_trading_signals'.
    signal_confidence : List[float]
        Confidence levels for the generated trading signals from the parent
        node 'generate_trading_signals'.

    Returns
    -------
    Tuple[List[str], List[str]]
        A tuple containing two lists: the first list contains the results of
        the executed trades, and the second list contains the status of the
        executed trades.

    Raises
    ------
    ValueError
        If the lengths of 'trading_signals' and 'signal_confidence' do not
        match.
    RuntimeError
        If there is an issue executing the trades.

    Examples
    --------
    >>> trading_signals = ['buy', 'sell', 'hold']
    >>> signal_confidence = [0.8, 0.7, 0.9]
    >>> trade_results, trade_status = execute_trades(trading_signals,
    signal_confidence)
    (['trade executed', 'trade executed', 'no action'], ['success', 'success',
    'held'])

    >>> trading_signals = ['buy', 'sell']
    >>> signal_confidence = [0.85, 0.65]
    >>> trade_results, trade_status = execute_trades(trading_signals,
    signal_confidence)
    (['trade executed', 'trade executed'], ['success', 'success'])

    """
    trading_signals = generate_trading_signals_input.trading_signals
    signal_confidence = generate_trading_signals_input.signal_confidence
    
    validate_input_lengths(signals=trading_signals, confidence=signal_confidence)
    
    trade_results: List[str] = []
    trade_status: List[str] = []
    
    for i, signal in enumerate(trading_signals):
        confidence = signal_confidence[i]
        
        if signal.lower() == 'hold':
            trade_results.append('no action')
            trade_status.append('held')
        else:
            execution_result: str = execute_single_trade(signal=signal, confidence=confidence)
            status: str = determine_trade_status(result=execution_result)
            trade_results.append(execution_result)
            trade_status.append(status)
    
    return ExecuteTradesOutput(
        trade_results=trade_results,
        trade_status=trade_status
    )