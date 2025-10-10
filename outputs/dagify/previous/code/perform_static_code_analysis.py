from ._perform_static_code_analysis.validate_source_files_exist import validate_source_files_exist
from ._perform_static_code_analysis.run_static_analysis_tools import run_static_analysis_tools
from ._perform_static_code_analysis.scan_for_vulnerabilities import scan_for_vulnerabilities
from ._perform_static_code_analysis.filter_and_format_issues import filter_and_format_issues
from ._perform_static_code_analysis.format_vulnerability_results import format_vulnerability_results

from pydantic import BaseModel, Field
from typing import List


class CollectSourceCodeOutput(BaseModel):
    """Pydantic model for collect_source_code node outputs."""
    source_code_files: List[str] = (
        Field(..., description="List of paths to source code files")
    )


class PerformStaticCodeAnalysisOutput(BaseModel):
    """Pydantic model for perform_static_code_analysis node outputs."""
    static_analysis_results: List[str] = (
        Field(..., description="List of issues identified by static code analysis")
    )
    vulnerabilities_found: List[str] = (
        Field(..., description="List of vulnerabilities detected")
    )


def perform_static_code_analysis(collect_source_code_input: CollectSourceCodeOutput, **kwargs) -> PerformStaticCodeAnalysisOutput:
    """
    Perform static code analysis on the provided source code files to identify
    issues and vulnerabilities.

    Parameters
    ----------
    source_code_files : List[str]
        List of paths to source code files collected by the
        'collect_source_code' node.

    Returns
    -------
    Tuple[List[str], List[str]]
        A tuple containing two lists: 'static_analysis_results' and
        'vulnerabilities_found'. The first list contains issues identified
        by static code analysis, and the second list contains
        vulnerabilities detected.

    Raises
    ------
    FileNotFoundError
        If any of the source code files listed in 'source_code_files' are
        not found.
    AnalysisToolError
        If there's an error running the static code analysis tools.

    Examples
    --------
    >>> source_code_files = ['/path/to/file1.py', '/path/to/file2.py']
    >>> static_analysis_results, vulnerabilities_found =
    perform_static_code_analysis(source_code_files)
    (['unused import', 'undefined variable'], ['SQL injection vulnerability'])

    >>> source_code_files = ['/path/to/secure_code.py']
    >>> static_analysis_results, vulnerabilities_found =
    perform_static_code_analysis(source_code_files)
    ([], [])

    """
    validate_source_files_exist(file_paths=collect_source_code_input.source_code_files)
    
    static_issues: List[str] = run_static_analysis_tools(source_files=collect_source_code_input.source_code_files)
    
    security_vulnerabilities: List[str] = scan_for_vulnerabilities(source_files=collect_source_code_input.source_code_files)
    
    filtered_issues: List[str] = filter_and_format_issues(raw_issues=static_issues)
    
    formatted_vulnerabilities: List[str] = format_vulnerability_results(raw_vulnerabilities=security_vulnerabilities)
    
    return PerformStaticCodeAnalysisOutput(
        static_analysis_results=filtered_issues,
        vulnerabilities_found=formatted_vulnerabilities
    )