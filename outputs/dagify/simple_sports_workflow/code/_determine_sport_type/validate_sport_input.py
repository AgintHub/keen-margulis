def validate_sport_input(sport_name: str) -> str:
    """
    Validates the input sport name against a list of supported sports and
    returns the canonical name.

    Parameters
    ----------
    sport_name : str
        The sport name to validate. Must be a non-empty string.

    Returns
    -------
    str
        The validated sport name in lowercase, matching one of the supported
        sports.

    Raises
    ------
    TypeError
        If sport_name is not of type str.
    ValueError
        If sport_name is not found in the list of supported sports.

    Examples
    --------
    >>> result = validate_sport_input("soccer")
    >>> print(result)
    'soccer'

    >>> validate_sport_input("unknown_sport")
    ValueError: "'unknown_sport' is not a supported sport name."

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")