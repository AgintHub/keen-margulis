def validate_liquid_type(liquid_type: str) -> bool:
    """
    Determines if the supplied liquid type is among the supported set for
    boiling simulation.

    Parameters
    ----------
    liquid_type : str
        Name of the liquid (e.g., 'water', 'coffee', 'milk').

    Returns
    -------
    bool
        True if the liquid_type is supported, False otherwise.

    Raises
    ------
    TypeError
        If liquid_type is not a string.
    ValueError
        If liquid_type is an empty string or contains only whitespace.

    Examples
    --------
    >>> result = validate_liquid_type('water')
    >>> print(result)
    True

    >>> result = validate_liquid_type('coffee')
    >>> print(result)
    False

    >>> validate_liquid_type(123)
    >>> print('This line will not be reached')
    Traceback (most recent call last):\n  File "<stdin>", line 1, in
    <module>\nTypeError: liquid_type must be a string

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")