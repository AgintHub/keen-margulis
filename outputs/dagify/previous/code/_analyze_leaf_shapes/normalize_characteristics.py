from typing import List


import re


def normalize_characteristics(characteristics: str) -> List[str]:
    """
    Normalizes a string of leaf characteristics into a list of standardized
    format.

    Parameters
    ----------
    characteristics : str
        Input string containing leaf characteristics to be normalized

    Returns
    -------
    List[str]
        List of normalized characteristic descriptions for each leaf

    Raises
    ------
    ValueError
        When the input string is empty or contains invalid characters
    TypeError
        When the input is not a string

    Examples
    --------
    >>> normalize_characteristics(characteristics='large, green, oval-shaped')
    >>> normalize_characteristics(characteristics='small, yellow, heart-shaped')
    ['large', 'green', 'oval-shaped']
    ['small', 'yellow', 'heart-shaped']

    >>> normalize_characteristics(characteristics='')
    []

    """
    if not isinstance(characteristics, str):
        raise TypeError("Input must be a string")
    
    if not characteristics:
        return []
    
    
    if not re.match(r'^[a-zA-Z0-9\s,\-]+$', characteristics):
        raise ValueError("Input contains invalid characters")
    
    parts = [part.strip() for part in characteristics.split(',')]
    normalized = [part for part in parts if part]
    
    return normalized