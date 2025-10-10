def create_node_description(workflow_name: str, node_name: str) -> str:
    """
    Creates a node description based on the workflow name and node name.

    Parameters
    ----------
    workflow_name : str
        The name of the workflow for which the node description is being
        generated.
    node_name : str
        The name of the node for which the description is being created.

    Returns
    -------
    str
        The generated node description.

    Raises
    ------
    TypeError
        If either workflow_name or node_name is not a string.
    ValueError
        If either workflow_name or node_name is empty or contains invalid
        characters.

    Examples
    --------
    >>> create_node_description(workflow_name='example_workflow',
    node_name='node_1')
    'Typed node for shim create_node_description'

    >>> create_node_description(workflow_name='another_workflow',
    node_name='node_2')
    'Typed node for shim create_node_description'

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")