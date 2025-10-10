from typing import List


def validate_source_files_exist(file_paths: str) -> List[str]:
    """
    Validates a list of source file paths and returns those that exist.

    Parameters
    ----------
    file_paths : str
        A string containing a list of file paths to validate, separated by
        commas or other delimiters as needed.

    Returns
    -------
    List[str]
        A list of file paths that were found to exist.

    Raises
    ------
    ValueError
        If the input string is malformed or empty.
    TypeError
        If the input is not a string.

    Examples
    --------
    >>> file_paths = 'path/to/file1.py,path/to/file2.py'
    >>> validate_source_files_exist(file_paths=file_paths)
    ['path/to/file1.py', 'path/to/file2.py']

    >>> file_paths = 'path/to/nonexistent_file.py,path/to/file2.py'
    >>> validate_source_files_exist(file_paths=file_paths)
    ['path/to/file2.py']

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")