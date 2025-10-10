def validate_source_files_exist(file_paths: str) -> str:
    """
    Validates the existence of source files provided as input file paths.

    Parameters
    ----------
    file_paths : str
        A comma-separated string of file paths to validate.

    Returns
    -------
    str
        A success message if all files exist, otherwise an error message.

    Raises
    ------
    FileNotFoundError
        If any of the provided file paths do not exist.
    TypeError
        If the input is not a string or if the string is not properly
        formatted.

    Examples
    --------
    >>>
    validate_source_files_exist(file_paths='path/to/file1.py,path/to/file2.py')
    'All files exist.'

    >>> validate_source_files_exist(file_paths='path/to/nonexistent_file.py')
    'File not found: path/to/nonexistent_file.py'

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")