def extract_volume(general_input: str, kwargs: str) -> float:
    """
    Extracts a numeric volume value from a string or keyword arguments.

    Parameters
    ----------
    general_input : str
        A string containing the volume information, e.g., '2L of water' or
        '1.5 liters'.
    kwargs : dict
        Optional keyword arguments that may supply the unit or override
        default parsing behaviour (e.g., unit='liters').

    Returns
    -------
    float
        The numeric volume value expressed in liters.

    Raises
    ------
    ValueError
        Raised when no numeric volume can be extracted or when the unit is
        unsupported.
    TypeError
        Raised when general_input is not a string or kwargs is not a
        dictionary.

    Examples
    --------
    >>> extract_volume('water 2L')
    2.0

    >>> extract_volume('1.5 liters of water', unit='liters')
    1.5

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")