def validate_sport_name(sport_name: str) -> str:
    """
    Validate a sport name against a known list and return its canonical form.

    Parameters
    ----------
    sport_name : str
        The sport name to be validated. Can be a full name or abbreviation.

    Returns
    -------
    str
        The canonical sport name that matches an entry in the supported
        sports list.

    Raises
    ------
    TypeError
        Raised if sport_name is not a string.
    ValueError
        Raised if sport_name does not match any known sport.

    Examples
    --------
    >>> validate_sport_name('soccer')
    'Football'

    >>> validate_sport_name('basketball')
    'Basketball'

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")