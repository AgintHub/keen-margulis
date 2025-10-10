def validate_input_types(evaluations: str, strategies: str) -> str:
    """
    Validates the input types of evaluations and strategies, raising exceptions
    for invalid types.

    Parameters
    ----------
    evaluations : List[str]
        A list of strategy evaluations to be validated.
    strategies : List[str]
        A list of recommended strategies to be validated.

    Returns
    -------
    str
        A success message if both inputs are valid List[str].

    Raises
    ------
    TypeError
        If either evaluations or strategies is not a List[str].

    Examples
    --------
    >>> validate_input_types(evaluations=['eval1', 'eval2'],
    strategies=['strat1', 'strat2'])
    'Input types are valid.'

    >>> validate_input_types(evaluations='not a list', strategies=['strat1',
    'strat2'])
    TypeError: Evaluations must be a List[str]

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")