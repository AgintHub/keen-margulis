def raise_value_error(message: str) -> str:
    """
    Raises a ValueError with a specified message.

    Parameters
    ----------
    message : str
        The message to be included in the ValueError.

    Raises
    ------
    ValueError
        Raised with the specified message.

    Examples
    --------
    >>> raise_value_error(message='Input validation failed')
    ValueError: Input validation failed

    >>> try: raise_value_error(message='Invalid input')
    >>> except ValueError as e: print(e)
    Invalid input

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")