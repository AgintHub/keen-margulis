def read_source_file(file_path: str) -> str:
    """
    Reads the content of a source file specified by the file path and returns it
    as a string.

    Parameters
    ----------
    file_path : str
        The path to the source file to be read.

    Returns
    -------
    str
        The content of the source file.

    Raises
    ------
    FileNotFoundError
        If the file specified by the file path does not exist.
    PermissionError
        If there is a permission issue reading the file.
    Exception
        For any other unexpected errors during file reading.

    Examples
    --------
    >>> read_source_file(file_path='/path/to/example.py')
    '# Example Python code\ndef example():\n    pass'

    >>> read_source_file(file_path='/path/to/another_example.py')
    '# Another example Python code\nclass AnotherExample:\n    def
    __init__(self):\n        pass'

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")