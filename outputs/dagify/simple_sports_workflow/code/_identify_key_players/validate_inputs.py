def validate_inputs(sport: str, leagues: str) -> bool:
    """
    Return a boolean indicating whether the provided sport and leagues are
    valid.

    Parameters
    ----------
    sport : str
        The name of the sport; must be a non‑empty string.
    leagues : LIST_STR
        A list of league names; must contain at least one non‑empty string.

    Returns
    -------
    bool
        True if both `sport` and `leagues` are valid, otherwise False.

    Raises
    ------
    ValueError
        Raised when `sport` is an empty string or `leagues` is empty or
        contains non‑string elements.
    TypeError
        Raised when `sport` is not a string or `leagues` is not a list.

    Examples
    --------
    >>> validate_inputs('soccer', ['Premier League', 'La Liga'])
    True

    >>> validate_inputs('', ['Premier League'])
    False

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")