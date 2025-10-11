def get_boiling_point(liquid_type: str) -> float:
    """
    Return the standard boiling point of a liquid in degrees Celsius.

    Parameters
    ----------
    liquid_type : str
        The name of the liquid (e.g., 'water', 'ethanol').

    Returns
    -------
    float
        The boiling point of the specified liquid in degrees Celsius.

    Raises
    ------
    ValueError
        Raised when the supplied liquid_type is not supported.
    TypeError
        Raised when liquid_type is not a string.

    Examples
    --------
    >>> get_boiling_point('water')
    100.0

    >>> get_boiling_point('ethanol')
    78.37

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")