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
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")