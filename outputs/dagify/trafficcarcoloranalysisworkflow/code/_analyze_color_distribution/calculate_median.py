import ast
import statistics


def calculate_median(scores: str) -> float:
    """
    Calculates the median of a list of confidence scores.

    Parameters
    ----------
    scores : str
        A string representation of a list of confidence scores.

    Returns
    -------
    float
        The median value of the confidence scores.

    Raises
    ------
    ValueError
        If the input string cannot be converted to a list of numbers.
    TypeError
        If the input is not a string or if the list contains non-numeric
        values.

    Examples
    --------
    >>> calculate_median(scores='[0.8, 0.9, 0.7]')
    0.8

    >>> calculate_median(scores='[0.5, 0.6, 0.4, 0.7]')
    0.55

    """
    
    if not isinstance(scores, str):
        raise TypeError("Input must be a string")
    
    try:
        scores_list = ast.literal_eval(scores)
    except (ValueError, SyntaxError) as e:
        raise ValueError("Input string cannot be converted to a list of numbers") from e
    
    if not isinstance(scores_list, list):
        raise ValueError("Input string must represent a list")
    
    for score in scores_list:
        if not isinstance(score, (int, float)):
            raise TypeError("List contains non-numeric values")
    
    if len(scores_list) == 0:
        raise ValueError("Cannot calculate median of empty list")
    
    return statistics.median(scores_list)