def check_boiling_status(temperature: str, boiling_point: str) -> bool:
    """
    Determine if a liquid has reached its boiling point.

    Parameters
    ----------
    temperature : float
        Current temperature of the liquid in degrees Celsius.
    boiling_point : float
        Boiling point temperature of the liquid in degrees Celsius.

    Returns
    -------
    bool
        True if temperature is greater than or equal to boiling_point;
        otherwise False.

    Raises
    ------
    ValueError
        Raised when temperature or boiling_point is negative.
    TypeError
        Raised when either temperature or boiling_point is not a numeric
        type.

    Examples
    --------
    >>> check_boiling_status(temperature=100.0, boiling_point=100.0)
    True

    >>> check_boiling_status(temperature=90.0, boiling_point=100.0)
    False

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")