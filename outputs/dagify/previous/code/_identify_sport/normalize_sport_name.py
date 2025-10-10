def normalize_sport_name(sport_name: str) -> str:
    """
    Normalize a raw sport name string to a canonical form.

    Parameters
    ----------
    sport_name : str
        The raw sport name string to be normalized.

    Returns
    -------
    str
        Normalized sport name string following canonical conventions.

    Raises
    ------
    ValueError
        Raised when the input is empty, contains only whitespace, or
        includes invalid characters.
    TypeError
        Raised when the input is not of type str.

    Examples
    --------
    >>> normalize_sport_name('soccer')
    'Soccer'

    >>> normalize_sport_name('  baseball ')
    'Baseball'

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")