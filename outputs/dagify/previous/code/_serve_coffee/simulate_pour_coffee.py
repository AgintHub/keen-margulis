def simulate_pour_coffee(temperature_c: str) -> float:
    """
    Simulates the temperature of coffee after pouring into a cup.

    Parameters
    ----------
    temperature_c : float
        The temperature of the coffee before pouring, expressed in degrees
        Celsius.

    Returns
    -------
    float
        The temperature of the coffee after pouring, in degrees Celsius.

    Raises
    ------
    ValueError
        Raised when the input temperature is outside the physically
        realistic range of -10°C to 100°C.
    TypeError
        Raised when the input temperature is not a float or int.

    Examples
    --------
    >>> simulate_pour_coffee(temperature_c=95.0)
    90.0

    >>> simulate_pour_coffee(temperature_c=60.0)
    58.0

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")