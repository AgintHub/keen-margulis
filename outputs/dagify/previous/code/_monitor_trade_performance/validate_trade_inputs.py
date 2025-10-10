def validate_trade_inputs(trade_results: str, trade_status: str) -> str:
    """
    Validates trade inputs based on their results and status.

    Parameters
    ----------
    trade_results : str
        A string containing the results of the executed trades, expected to
        be in a specific format.
    trade_status : str
        A string containing the status of the executed trades, indicating
        success or failure.

    Returns
    -------
    str
        A string indicating the outcome of the validation process.

    Raises
    ------
    ValueError
        Raised when the trade results or status are not in the expected
        format or contain invalid data.
    TypeError
        Raised when the input types are not as expected (e.g., not strings).

    Examples
    --------
    >>> validate_trade_inputs(trade_results='success,100,buy',
    trade_status='success')
    >>> print(output)
    'Validation successful'

    >>> validate_trade_inputs(trade_results='failure,0,sell',
    trade_status='failure')
    >>> print(output)
    'Validation successful'

    """
    if not isinstance(trade_results, str):
        raise TypeError("trade_results must be a string")
    if not isinstance(trade_status, str):
        raise TypeError("trade_status must be a string")
    
    if trade_status not in ['success', 'failure']:
        raise ValueError("trade_status must be 'success' or 'failure'")
    
    if not trade_results:
        raise ValueError("trade_results cannot be empty")
    
    parts = trade_results.split(',')
    if len(parts) != 3:
        raise ValueError("trade_results must contain exactly 3 comma-separated values")
    
    status, amount, action = parts
    
    if status not in ['success', 'failure']:
        raise ValueError("First part of trade_results must be 'success' or 'failure'")
    
    try:
        amount_val = int(amount)
        if amount_val < 0:
            raise ValueError("Amount must be non-negative")
    except ValueError:
        raise ValueError("Second part of trade_results must be a valid non-negative integer")
    
    if action not in ['buy', 'sell']:
        raise ValueError("Third part of trade_results must be 'buy' or 'sell'")
    
    return 'Validation successful'