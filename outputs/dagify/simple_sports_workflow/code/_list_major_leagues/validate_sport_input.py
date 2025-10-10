def validate_sport_input(sport_name: str) -> str:
    """
    Validate and normalize a sport name.

    Parameters
    ----------
    sport_name : str
        The sport name provided by the user, to be validated.

    Returns
    -------
    str
        The validated and canonical sport name.

    Raises
    ------
    ValueError
        Raised when sport_name is empty or does not match any supported
        sport.
    TypeError
        Raised when sport_name is not a string.

    Examples
    --------
    >>> validate_sport_input('soccer')
    'soccer'

    >>> validate_sport_input('')
    ValueError: Sport name must not be empty.

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")