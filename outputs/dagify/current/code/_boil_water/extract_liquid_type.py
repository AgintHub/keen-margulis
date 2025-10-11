def extract_liquid_type(general_input: str, kwargs: str) -> str:
    """
    Extracts the liquid type from a general input string, returning a
    standardized lowercase string.

    Parameters
    ----------
    general_input : str
        The raw input string that may contain a liquid type followed by
        additional descriptors such as volume or units.
    kwargs : str
        Additional keyword arguments in string form; currently unused but
        retained for API compatibility.

    Returns
    -------
    str
        The liquid type extracted from the input, lowercased. Example:
        'water', 'coffee', 'milk'.

    Raises
    ------
    ValueError
        Raised when the liquid type cannot be determined from the input.
    TypeError
        Raised when either `general_input` or `kwargs` is not a string.

    Examples
    --------
    >>> print(extract_liquid_type('Water 500ml', {}))
    'water'

    >>> print(extract_liquid_type('Coffee 300ml', {}))
    'coffee'

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")