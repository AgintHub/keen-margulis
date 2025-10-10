def validate_input_types(colors: str, scores: str) -> str:
    """
    Validates the types of input colors and scores.

    Parameters
    ----------
    colors : List[str]
        List of detected vehicle colors.
    scores : List[float]
        List of confidence scores corresponding to the detected vehicle
        colors.

    Returns
    -------
    str
        A message indicating whether the input types are valid.

    Raises
    ------
    TypeError
        If the input colors are not a list of strings or if the scores are
        not a list of floats.

    Examples
    --------
    >>> colors = ['red', 'blue', 'green']
    >>> scores = [0.8, 0.9, 0.7]
    >>> validate_input_types(colors=colors, scores=scores)
    'Input types are valid.'

    >>> colors = ['red', 1, 'green']
    >>> scores = [0.8, 0.9, 0.7]
    >>> validate_input_types(colors=colors, scores=scores)
    TypeError: 'colors' must be a list of strings.

    """
    if not isinstance(colors, list):
        raise TypeError("'colors' must be a list of strings.")
    
    for color in colors:
        if not isinstance(color, str):
            raise TypeError("'colors' must be a list of strings.")
    
    if not isinstance(scores, list):
        raise TypeError("'scores' must be a list of floats.")
    
    for score in scores:
        if not isinstance(score, (float, int)):
            raise TypeError("'scores' must be a list of floats.")
    
    return "Input types are valid."