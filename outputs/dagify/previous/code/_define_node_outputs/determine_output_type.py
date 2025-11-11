def determine_output_type(task: str) -> str:
    """
    Determines the output type for a given task.

    Parameters
    ----------
    task : str
        The task for which to determine the output type.

    Returns
    -------
    str
        The determined output type as a string.

    Raises
    ------
    ValueError
        If the task is invalid or cannot be processed.
    TypeError
        If the task is not of type string.

    Examples
    --------
    >>> determine_output_type(task='classification_task')
    'categorical'

    >>> determine_output_type(task='regression_task')
    'continuous'

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")