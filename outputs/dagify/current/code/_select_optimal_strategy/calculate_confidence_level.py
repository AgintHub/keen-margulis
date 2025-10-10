def calculate_confidence_level(scores: str, optimal_index: str) -> float:
    """
    Calculate the confidence level for a selected trading strategy.

    Parameters
    ----------
    scores : List[float]
        A list of numeric scores, each corresponding to a strategy
        evaluation.
    optimal_index : int
        The index of the strategy identified as optimal within the `scores`
        list.

    Returns
    -------
    float
        A confidence level between 0 and 1, computed as the score at
        `optimal_index` divided by the sum of all scores.

    Raises
    ------
    ValueError
        If `scores` is empty or `optimal_index` is out of bounds.
    TypeError
        If `scores` is not a list of floats or `optimal_index` is not an
        integer.

    Examples
    --------
    >>> scores = [0.8, 0.5, 0.7]
    >>> conf = calculate_confidence_level(scores, 0)
    >>> print(conf)
    0.4

    >>> scores = [0.3, 0.6]
    >>> conf = calculate_confidence_level(scores, 1)
    >>> print(conf)
    0.6666666666666666

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")