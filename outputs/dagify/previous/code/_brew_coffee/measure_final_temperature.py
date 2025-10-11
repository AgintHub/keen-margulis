def measure_final_temperature(success: str, initial_temp: str) -> float:
    """
    Return the final temperature of brewed coffee based on whether the brewing
    process succeeded and the initial temperature of the boiled water.

    Parameters
    ----------
    success : str
        Indicates if the brewing process completed successfully. Expected
        values are the string literals "True" or "False".
    initial_temp : str
        The temperature of the boiled water in degrees Celsius, provided as
        a numeric string.

    Returns
    -------
    float
        The final temperature of the brewed coffee in degrees Celsius. If
        the brew was successful, the temperature is calculated as
        `float(initial_temp) - 15.0`. If unsuccessful, it defaults to `0.0`.

    Raises
    ------
    ValueError
        Raised when `success` is not "True" or "False", or when
        `initial_temp` cannot be converted to a float.
    TypeError
        Raised when `success` or `initial_temp` is not of type `str`.

    Examples
    --------
    >>> output = measure_final_temperature('True', '100')
    >>> print(output)
    85.0

    >>> output = measure_final_temperature('False', '90')
    >>> print(output)
    0.0

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")