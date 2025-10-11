def calculate_grounds_amount(desired_cup_count: str, grounds_type: str) -> float:
    """
    Compute the grams of coffee grounds needed for a given cup count and grounds
    type.

    Parameters
    ----------
    desired_cup_count : int
        Number of cups to brew; must be a positive integer.
    grounds_type : str
        Coffee grounds type (e.g., 'medium', 'dark', 'light') that
        determines the grams-per-cup ratio.

    Returns
    -------
    float
        Total grams of coffee grounds required.

    Raises
    ------
    ValueError
        Raised when desired_cup_count is not a positive integer or
        grounds_type is unsupported.
    TypeError
        Raised when inputs are of incorrect types.

    Examples
    --------
    >>> calculate_grounds_amount(desired_cup_count=4, grounds_type='medium')
    10.0

    >>> calculate_grounds_amount(desired_cup_count=2, grounds_type='dark')
    6.0

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")