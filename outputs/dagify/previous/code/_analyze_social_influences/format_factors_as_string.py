def format_factors_as_string(factors: str) -> str:
    """
    Format a list of factor names into a comma-separated string.

    Parameters
    ----------
    factors : List[str]
        List of factor names to format into a single string.

    Returns
    -------
    str
        A single string containing all factor names separated by commas and
        spaces.

    Raises
    ------
    ValueError
        Raised when the input list is empty or contains non-string items.
    TypeError
        Raised when the input is not a list.

    Examples
    --------
    >>> format_factors_as_string(['innovation', 'policy'])
    'innovation, policy'

    >>> format_factors_as_string(['fact1', 'fact2', 'fact3'])
    'fact1, fact2, fact3'

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")