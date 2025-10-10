def calculate_success_rate(trade_status: str) -> float:
    """
    Calculates the success rate of trades based on their status.

    Parameters
    ----------
    trade_status : List[str]
        A list of strings representing the status of each trade (e.g.,
        'success', 'failure').

    Returns
    -------
    float
        The success rate of the trades as a float value between 0 and 1.

    Raises
    ------
    ValueError
        If the input list is empty or contains invalid status values.
    TypeError
        If the input is not a list or if the list contains non-string
        values.

    Examples
    --------
    >>> trade_status = ['success', 'failure', 'success']
    >>> success_rate = calculate_success_rate(trade_status=trade_status)
    0.6666666666666666

    >>> trade_status = ['success', 'success', 'success']
    >>> success_rate = calculate_success_rate(trade_status=trade_status)
    1.0

    """
    if not isinstance(trade_status, list):
        raise TypeError("Input must be a list")
    
    if len(trade_status) == 0:
        raise ValueError("Input list cannot be empty")
    
    for status in trade_status:
        if not isinstance(status, str):
            raise TypeError("All elements in the list must be strings")
        if status not in ['success', 'failure']:
            raise ValueError("Invalid status value. Must be 'success' or 'failure'")
    
    success_count = trade_status.count('success')
    total_count = len(trade_status)
    
    return success_count / total_count