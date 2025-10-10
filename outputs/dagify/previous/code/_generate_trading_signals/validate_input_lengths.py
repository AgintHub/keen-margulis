import ast


def validate_input_lengths(evaluations: str, strategies: str) -> str:
    """
    Validates the lengths of input lists for evaluations and strategies.

    Parameters
    ----------
    evaluations : str
        String representation of a list of evaluations.
    strategies : str
        String representation of a list of strategies.

    Returns
    -------
    str
        Output indicating whether the input lists have the same length.

    Raises
    ------
    ValueError
        If the lengths of the input lists do not match.

    Examples
    --------
    >>> validate_input_lengths(evaluations='[1, 2, 3]', strategies='["a", "b",
    "c"]')
    'Input lengths are valid'

    >>> validate_input_lengths(evaluations='[1, 2]', strategies='["a", "b",
    "c"]')
    ValueError: 'Input lists have different lengths'

    """
    
    try:
        eval_list = ast.literal_eval(evaluations)
        strat_list = ast.literal_eval(strategies)
    except (ValueError, SyntaxError) as e:
        raise ValueError(f"Invalid list format in input strings: {e}")
    
    if not isinstance(eval_list, list) or not isinstance(strat_list, list):
        raise ValueError("Input strings must represent valid lists")
    
    if len(eval_list) != len(strat_list):
        raise ValueError("Input lists have different lengths")
    
    return "Input lengths are valid"