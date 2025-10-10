def generate_validation_error_message(connectivity_valid: str, schema_valid: str, execution_path_valid: str) -> str:
    """
    Generates a validation error message based on the given validation results.

    Parameters
    ----------
    connectivity_valid : str
        A boolean string indicating whether the node connectivity is valid
        ('True' or 'False').
    schema_valid : str
        A boolean string indicating whether the node schema is valid ('True'
        or 'False').
    execution_path_valid : str
        A boolean string indicating whether the execution path is valid
        ('True' or 'False').

    Returns
    -------
    str
        A detailed error message indicating which validation checks failed.

    Raises
    ------
    ValueError
        If any of the input boolean strings are not 'True' or 'False'.

    Examples
    --------
    >>> generate_validation_error_message(connectivity_valid='False',
    schema_valid='True', execution_path_valid='False')
    'Validation failed due to invalid connectivity and execution path.'

    >>> generate_validation_error_message(connectivity_valid='True',
    schema_valid='False', execution_path_valid='True')
    'Validation failed due to invalid schema.'

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")