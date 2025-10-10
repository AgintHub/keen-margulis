from typing import List


import ast


def calculate_frequencies(counts: str, total: str) -> List[float]:
    """
    Calculates frequencies of occurrences based on input counts and total,
    returning a list of float values.

    Parameters
    ----------
    counts : str
        String representation of a list of integers where each integer
        represents the count of occurrences.
    total : str
        String representation of an integer that represents the total count
        of all occurrences.

    Returns
    -------
    List[float]
        A list of float values representing the frequency of each count
        relative to the total.

    Raises
    ------
    ValueError
        If the input counts or total cannot be properly parsed into
        integers, or if total is zero.
    TypeError
        If the input counts or total are not strings that can be interpreted
        as integers or lists of integers.

    Examples
    --------
    >>> counts = '[1, 2, 3]'
    >>> total = '6'
    >>> calculate_frequencies(counts=counts, total=total)
    [0.16666666666666666, 0.3333333333333333, 0.5]

    >>> counts = '[4, 5, 6]'
    >>> total = '15'
    >>> calculate_frequencies(counts=counts, total=total)
    [0.26666666666666666, 0.3333333333333333, 0.4]

    """
    
    if not isinstance(counts, str) or not isinstance(total, str):
        raise TypeError("Input counts and total must be strings")
    
    try:
        counts_list = ast.literal_eval(counts)
        if not isinstance(counts_list, list) or not all(isinstance(x, int) for x in counts_list):
            raise ValueError("Counts must be a string representation of a list of integers")
    except (ValueError, SyntaxError) as e:
        raise ValueError("Input counts cannot be properly parsed into a list of integers") from e
    
    try:
        total_int = int(total)
    except ValueError as e:
        raise ValueError("Input total cannot be properly parsed into an integer") from e
    
    if total_int == 0:
        raise ValueError("Total cannot be zero")
    
    frequencies = [count / total_int for count in counts_list]
    return frequencies