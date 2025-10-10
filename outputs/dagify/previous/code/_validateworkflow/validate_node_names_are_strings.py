def validate_node_names_are_strings(connected_nodes: str) -> str:
    """
    Validates that all connected node names are strings.

    Parameters
    ----------
    connected_nodes : List[str]
        A list of node names to be validated as strings.

    Returns
    -------
    str
        A message indicating whether the validation was successful or not.

    Raises
    ------
    TypeError
        If any of the node names in the list are not strings.

    Examples
    --------
    >>> validate_node_names_are_strings(connected_nodes=['node1', 'node2'])
    'Validation successful'

    >>> validate_node_names_are_strings(connected_nodes=['node1', 2])
    TypeError: All node names must be strings.

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")