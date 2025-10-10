def determine_trade_status(result: str) -> str:
    """
    Determines the trade status based on the execution result.

    Parameters
    ----------
    result : str
        The execution result of the trade.

    Returns
    -------
    str
        The status of the trade (e.g., 'success', 'failure').

    Raises
    ------
    ValueError
        If the execution result is invalid or cannot be interpreted.

    Examples
    --------
    >>> determine_trade_status(result='Trade executed successfully')
    'success'

    >>> determine_trade_status(result='Insufficient funds')
    'failure'

    """
    if not isinstance(result, str):
        raise ValueError("Execution result must be a string")
    
    if not result or not result.strip():
        raise ValueError("Execution result is empty or invalid")
    
    result_lower = result.lower().strip()
    
    success_indicators = [
        'executed successfully', 'trade completed', 'order filled', 
        'transaction successful', 'success', 'completed', 'filled'
    ]
    
    failure_indicators = [
        'insufficient funds', 'failed', 'error', 'rejected', 
        'cancelled', 'timeout', 'invalid', 'denied'
    ]
    
    for indicator in success_indicators:
        if indicator in result_lower:
            return 'success'
    
    for indicator in failure_indicators:
        if indicator in result_lower:
            return 'failure'
    
    raise ValueError(f"Cannot interpret execution result: {result}")