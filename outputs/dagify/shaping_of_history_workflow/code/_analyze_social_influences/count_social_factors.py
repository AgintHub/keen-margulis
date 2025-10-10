def count_social_factors(factors: str) -> int:
    """
    Return the number of unique social factors from a list.

    Parameters
    ----------
    factors : List[str]
        A list of social factor names (strings) to be counted.

    Returns
    -------
    int
        The count of distinct social factor names in the input list.

    Raises
    ------
    TypeError
        Raised if `factors` is not an iterable of strings.
    ValueError
        Raised if any element in `factors` is not a string.

    Examples
    --------
    >>> count_social_factors(['democracy', 'freedom', 'equality'])
    3

    >>> count_social_factors(['democracy', 'freedom', 'democracy'])
    2

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")