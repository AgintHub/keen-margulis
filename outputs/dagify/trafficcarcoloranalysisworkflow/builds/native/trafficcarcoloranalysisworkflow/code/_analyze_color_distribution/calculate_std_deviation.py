import json
import math


def calculate_std_deviation(scores: str) -> float:
    """
    Calculates the standard deviation of confidence scores.

    Parameters
    ----------
    scores : str
        A string representation of a list of confidence scores.

    Returns
    -------
    float
        The standard deviation of the confidence scores.

    Raises
    ------
    ValueError
        If the input string cannot be converted to a list of numbers.
    TypeError
        If the input is not a string.

    Examples
    --------
    >>> import json
    >>> scores_str = '[0.8, 0.9, 0.7]'
    >>> result = calculate_std_deviation(scores_str)
    >>> print(result)
    0.08164965809277261

    >>> import json
    >>> scores_str = '[0.5, 0.6, 0.4]'
    >>> result = calculate_std_deviation(scores_str)
    >>> print(result)
    0.08164965809277258

    """
    if not isinstance(scores, str):
        raise TypeError("If the input is not a string.")
    
    try:
        scores_list = json.loads(scores)
    except (json.JSONDecodeError, ValueError):
        raise ValueError("If the input string cannot be converted to a list of numbers.")
    
    if not isinstance(scores_list, list):
        raise ValueError("If the input string cannot be converted to a list of numbers.")
    
    try:
        numeric_scores = [float(score) for score in scores_list]
    except (ValueError, TypeError):
        raise ValueError("If the input string cannot be converted to a list of numbers.")
    
    if len(numeric_scores) == 0:
        return 0.0
    
    if len(numeric_scores) == 1:
        return 0.0
    
    mean = sum(numeric_scores) / len(numeric_scores)
    variance = sum((x - mean) ** 2 for x in numeric_scores) / len(numeric_scores)
    std_deviation = math.sqrt(variance)
    
    return std_deviation