from typing import List


def scan_directory_for_source_files(directory_path: str) -> List[str]:
    """
    Scans a directory for source code files and returns their paths

    Parameters
    ----------
    directory_path : str
        The path to the directory that needs to be scanned for source code
        files

    Returns
    -------
    List[str]
        A list containing the paths to all source code files found in the
        specified directory

    Raises
    ------
    FileNotFoundError
        If the specified directory does not exist
    PermissionError
        If there are insufficient permissions to access the directory
    NotADirectoryError
        If the provided path is not a directory

    Examples
    --------
    >>> scan_directory_for_source_files(directory_path='/path/to/project')
    >>> # Assuming /path/to/project contains source code files
    ['/path/to/project/file1.py', '/path/to/project/file2.java']

    >>>
    scan_directory_for_source_files(directory_path='/non/existent/directory')
    FileNotFoundError: Directory '/non/existent/directory' not found

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")