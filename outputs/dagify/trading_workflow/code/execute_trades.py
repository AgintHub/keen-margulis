from ._execute_trades.validate_trading_signals import validate_trading_signals
from ._execute_trades.filter_signals_by_confidence import filter_signals_by_confidence
from ._execute_trades.convert_signals_to_orders import convert_signals_to_orders
from ._execute_trades.execute_trade_orders import execute_trade_orders
from ._execute_trades.check_execution_success import check_execution_success
from ._execute_trades.format_trade_details import format_trade_details

from pydantic import BaseModel, Field
from typing import List


class GenerateTradingSignalsOutput(BaseModel):
    """Pydantic model for generate_trading_signals node outputs."""
    trading_signals: List[str] = (
        Field(..., description="List of generated trading signals")
    )
    signal_confidence: List[float] = (
        Field(..., description="List of confidence levels for each trading signal")
    )
    signal_generation_status: bool = (
        Field(..., description="Whether signal generation was successful")
    )


class ExecuteTradesOutput(BaseModel):
    """Pydantic model for execute_trades node outputs."""
    trade_execution_status: bool = (
        Field(..., description="Whether trade execution was successful")
    )
    trade_details: List[str] = (
        Field(..., description="List of trade details, including trade type, quantity, and price")
    )


def execute_trades(generate_trading_signals_input: GenerateTradingSignalsOutput, **kwargs) -> ExecuteTradesOutput:
    """
    Execute trades based on the generated trading signals, returning the status
    of trade execution and details of the trades.

    Parameters
    ----------
    trading_signals : List[str]
        List of generated trading signals from the
        'generate_trading_signals' node.
    signal_confidence : List[float]
        List of confidence levels for each trading signal from the
        'generate_trading_signals' node.
    signal_generation_status : bool
        Whether signal generation was successful from the
        'generate_trading_signals' node.

    Returns
    -------
    Tuple[bool, List[str]]
        A tuple containing a boolean indicating whether trade execution was
        successful and a list of trade details.

    Raises
    ------
    ValueError
        If the input trading signals are invalid or if signal generation was
        not successful.
    RuntimeError
        If trade execution fails due to external factors.

    Examples
    --------
    >>> trading_signals = ['buy', 'sell', 'hold']
    >>> signal_confidence = [0.8, 0.7, 0.9]
    >>> signal_generation_status = True
    >>> trade_execution_status, trade_details = execute_trades(trading_signals,
    signal_confidence, signal_generation_status)
    (True, ['trade_type=buy,quantity=100,price=50.0',
    'trade_type=sell,quantity=50,price=51.0'])

    >>> trading_signals = ['invalid_signal']
    >>> signal_confidence = [0.5]
    >>> signal_generation_status = True
    >>> try:
    ...     trade_execution_status, trade_details =
    execute_trades(trading_signals, signal_confidence, signal_generation_status)
    >>> except ValueError as e:
    ...     print(e)
    'Invalid trading signal: invalid_signal'

    """
    validated_signals: List[str] = validate_trading_signals(signals=generate_trading_signals_input.trading_signals, status=generate_trading_signals_input.signal_generation_status)
    
    filtered_signals: List[str] = filter_signals_by_confidence(signals=validated_signals, confidence_levels=generate_trading_signals_input.signal_confidence)
    
    trade_orders: List[dict] = convert_signals_to_orders(signals=filtered_signals, confidence_levels=generate_trading_signals_input.signal_confidence)
    
    execution_results: List[dict] = execute_trade_orders(orders=trade_orders)
    
    execution_status: bool = check_execution_success(results=execution_results)
    
    formatted_trade_details: List[str] = format_trade_details(results=execution_results)
    
    return ExecuteTradesOutput(
        trade_execution_status=execution_status,
        trade_details=formatted_trade_details
    )