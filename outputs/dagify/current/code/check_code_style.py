from ._check_code_style.validate_source_files_exist import validate_source_files_exist
from ._check_code_style.run_style_linter import run_style_linter
from ._check_code_style.run_formatting_checker import run_formatting_checker

from pydantic import BaseModel, Field
from typing import List


class CollectSourceCodeOutput(BaseModel):
    """Pydantic model for collect_source_code node outputs."""
    source_code_files: List[str] = (
        Field(..., description="List of paths to source code files")
    )


class CheckCodeStyleOutput(BaseModel):
    """Pydantic model for check_code_style node outputs."""
    style_issues: List[str] = (
        Field(..., description="List of style issues identified")
    )
    formatting_errors: List[str] = (
        Field(..., description="List of formatting errors detected")
    )


def check_code_style(collect_source_code_input: CollectSourceCodeOutput, **kwargs) -> CheckCodeStyleOutput:
    """
    Analyze code style and formatting consistency using linters or style
    checkers.

    Parameters
    ----------
    source_code_files : List[str]
        List of paths to source code files collected by the
        'collect_source_code' node.

    Returns
    -------
    Tuple[List[str], List[str]]
        A tuple containing a list of style issues identified and a list of
        formatting errors detected.

    Raises
    ------
    FileNotFoundError
        If any of the source code files are not found.
    Exception
        If there is an error during the analysis process.

    Examples
    --------
    >>> source_code_files = ['/path/to/file1.py', '/path/to/file2.py']
    >>> style_issues, formatting_errors = check_code_style(source_code_files)
    (['unused import', 'invalid indentation'], [' trailing whitespace', '
    inconsistent spacing'])

    >>> source_code_files = ['/path/to/file3.py']
    >>> style_issues, formatting_errors = check_code_style(source_code_files)
    (['missing docstring'], [])

    """
    validated_files: List[str] = validate_source_files_exist(file_paths=collect_source_code_input.source_code_files)
    
    style_issues: List[str] = run_style_linter(file_paths=validated_files)
    
    formatting_errors: List[str] = run_formatting_checker(file_paths=validated_files)
    
    return CheckCodeStyleOutput(
        style_issues=style_issues,
        formatting_errors=formatting_errors
    )