def validate_strategy_inputs(strategy: str, confidence: str) -> str:
    """
    Validates trading strategy and confidence level, raising errors on invalid
    inputs and returning a confirmation string.

    Parameters
    ----------
    strategy : str
        The name of the trading strategy to be validated.
    confidence : str
        String representation of the confidence level associated with the
        strategy.

    Returns
    -------
    str
        A message confirming that the strategy and confidence level are
        valid.

    Raises
    ------
    TypeError
        If strategy or confidence is not a string.
    ValueError
        If strategy is not one of the accepted strategies or if confidence
        is not a numeric string between 0 and 1.

    Examples
    --------
    >>> validate_strategy_inputs(strategy='scalping', confidence='0.85')
    'Strategy scalping with confidence 0.85 validated.'

    >>> validate_strategy_inputs(strategy='mean_reversion', confidence='1.2')
    ValueError: Confidence must be a numeric string between 0 and 1.

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")