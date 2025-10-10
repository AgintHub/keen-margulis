from typing import List


def validate_economic_factors_input(factors: str) -> List[str]:
    """
    Validate and sanitize a list of economic factor names.

    Parameters
    ----------
    factors : List[str]
        List of raw economic factor names to validate.

    Returns
    -------
    List[str]
        A cleaned list of valid economic factor names.

    Raises
    ------
    TypeError
        If `factors` is not a list or contains non-string elements.
    ValueError
        If any factor is empty or contains non-alphabetic characters.

    Examples
    --------
    >>> validate_economic_factors_input(['inflation', 'gdp', 'taxation'])
    ['inflation', 'gdp', 'taxation']

    >>> validate_economic_factors_input(['inflation', '123', 'gdp'])
    ValueError: Factor '123' contains non-alphabetic characters.

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")