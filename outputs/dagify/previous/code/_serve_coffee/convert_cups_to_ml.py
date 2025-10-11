def convert_cups_to_ml(volume_cups: str) -> int:
    """
    Converts a volume measurement from cups to milliliters using the standard
    conversion factor of 236.588 ml per cup.

    Parameters
    ----------
    volume_cups : int
        The number of cups to be converted; must be a non‑negative integer.

    Returns
    -------
    int
        The equivalent volume in milliliters, rounded to the nearest
        integer.

    Raises
    ------
    ValueError
        Raised if `volume_cups` is negative.
    TypeError
        Raised if `volume_cups` is not an integer.

    Examples
    --------
    >>> convert_cups_to_ml(2)
    473

    >>> convert_cups_to_ml(0)
    0

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")