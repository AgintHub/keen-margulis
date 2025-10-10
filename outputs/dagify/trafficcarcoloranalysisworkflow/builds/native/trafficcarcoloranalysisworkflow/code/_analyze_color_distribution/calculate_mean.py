import ast


def calculate_mean(scores: str) -> float:
    """
    Calculates the mean of a list of confidence scores passed as a string.

    Parameters
    ----------
    scores : str
        A string representation of a list of confidence scores.

    Returns
    -------
    float
        The mean of the confidence scores. Returns NaN if the input list is
        empty.

    Raises
    ------
    ValueError
        If the input string cannot be parsed into a list of numbers.
    TypeError
        If the input is not a string.

    Examples
    --------
    >>> calculate_mean(scores='[0.8, 0.9, 0.7]')
    0.8

    >>> calculate_mean(scores='[]')
    NaN

    """
    if not isinstance(scores, str):
        raise TypeError("If the input is not a string.")
    
    try:
        scores_list = ast.literal_eval(scores)
        if not isinstance(scores_list, list):
            raise ValueError("If the input string cannot be parsed into a list of numbers.")
        
        for item in scores_list:
            if not isinstance(item, (int, float)):
                raise ValueError("If the input string cannot be parsed into a list of numbers.")
        
    except (ValueError, SyntaxError) as e:
        raise ValueError("If the input string cannot be parsed into a list of numbers.") from e
    
    if len(scores_list) == 0:
        return float('nan')
    
    return sum(scores_list) / len(scores_list)