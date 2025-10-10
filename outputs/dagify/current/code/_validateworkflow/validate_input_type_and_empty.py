def validate_input_type_and_empty(connected_nodes: str) -> str:
    """
    Validates that the input connected_nodes is a non-empty list of strings.

    Parameters
    ----------
    connected_nodes : List[str]
        List of connected node names to be validated.

    Returns
    -------
    str
        Output indicating the validation result or an error message.

    Raises
    ------
    ValueError
        If the input list is empty.
    TypeError
        If the input is not a list or if any element in the list is not a
        string.

    Examples
    --------
    >>> validate_input_type_and_empty(connected_nodes=['node1', 'node2'])
    'Validation successful'

    >>> validate_input_type_and_empty(connected_nodes=[])
    ValueError: Input list is empty

    >>> validate_input_type_and_empty(connected_nodes=['node1', 2])
    TypeError: All elements in the list must be strings

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")