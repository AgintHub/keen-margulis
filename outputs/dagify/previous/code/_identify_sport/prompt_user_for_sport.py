def prompt_user_for_sport(message: str) -> str:
    """
    Prompts the user to enter a sport name and returns the raw string provided
    by the user.

    Parameters
    ----------
    message : str
        The prompt message displayed to the user.

    Returns
    -------
    str
        The string entered by the user.

    Raises
    ------
    TypeError
        Raised if the message argument is not a string.

    Examples
    --------
    >>> response = prompt_user_for_sport(message='Please specify a sport of
    interest: ')
    >>> print(response)
    'Soccer'

    >>> response = prompt_user_for_sport(message='Enter your favorite sport: ')
    >>> print(response)
    'Basketball'

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")