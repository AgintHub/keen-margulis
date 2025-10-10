from ._collect_source_code.extract_repository_path import extract_repository_path
from ._collect_source_code.validate_path_exists import validate_path_exists
from ._collect_source_code.check_path_permissions import check_path_permissions
from ._collect_source_code.scan_directory_for_source_files import scan_directory_for_source_files
from ._collect_source_code.filter_source_code_files import filter_source_code_files

from pydantic import BaseModel, Field
from typing import List


class CollectSourceCodeOutput(BaseModel):
    """Pydantic model for collect_source_code node outputs."""
    source_code_files: List[str] = (
        Field(..., description="List of paths to source code files")
    )


def collect_source_code(general_input: str, **kwargs) -> CollectSourceCodeOutput:
    """
    Collects source code files from a specified directory or repository.

    Parameters
    ----------
    repository_path : str
        Path to the repository or project directory to search for source
        code files.

    Returns
    -------
    List[str]
        A list of paths to the collected source code files.

    Raises
    ------
    FileNotFoundError
        If the specified repository_path does not exist.
    PermissionError
        If there is no permission to access the repository_path or any of
        its contents.

    Examples
    --------
    >>> collect_source_code(repository_path='/home/user/project')
    ['/home/user/project/file1.py', '/home/user/project/file2.py']

    >>> collect_source_code(repository_path='/home/user/non_existent_project')
    FileNotFoundError: /home/user/non_existent_project does not exist.

    """
    repository_path: str = extract_repository_path(general_input=general_input, kwargs=kwargs)
    validate_path_exists(path=repository_path)
    check_path_permissions(path=repository_path)
    file_paths: List[str] = scan_directory_for_source_files(directory_path=repository_path)
    filtered_files: List[str] = filter_source_code_files(file_paths=file_paths)
    return CollectSourceCodeOutput(source_code_files=filtered_files)