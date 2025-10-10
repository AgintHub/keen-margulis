from pydantic import BaseModel, Field
from typing import List


class PerformStaticCodeAnalysisOutput(BaseModel):
    """Pydantic model for perform_static_code_analysis node outputs."""
    static_analysis_results: List[str] = (
        Field(..., description="List of issues identified by static code analysis")
    )
    vulnerabilities_found: List[str] = (
        Field(..., description="List of vulnerabilities detected")
    )


class MeasureCodeComplexityOutput(BaseModel):
    """Pydantic model for measure_code_complexity node outputs."""
    complexity_metrics: List[float] = (
        Field(..., description="List of complexity metrics for each file.")
    )
    cyclomatic_complexity: List[int] = (
        Field(..., description="Cyclomatic complexity values for each file.")
    )


class CheckCodeStyleOutput(BaseModel):
    """Pydantic model for check_code_style node outputs."""
    style_issues: List[str] = (
        Field(..., description="List of style issues identified")
    )
    formatting_errors: List[str] = (
        Field(..., description="List of formatting errors detected")
    )


class CompileAnalysisReportOutput(BaseModel):
    """Pydantic model for compile_analysis_report node outputs."""
    analysis_summary: str = (
        Field(..., description="Summary of the overall analysis results")
    )
    recommendations: List[str] = (
        Field(..., description="List of recommendations for improving code quality")
    )
    quality_score: float = Field(..., description="Overall code quality score")


def compile_analysis_report(perform_static_code_analysis_input: PerformStaticCodeAnalysisOutput, measure_code_complexity_input: MeasureCodeComplexityOutput, check_code_style_input: CheckCodeStyleOutput, **kwargs) -> CompileAnalysisReportOutput:
    """
    Compile a comprehensive report summarizing the analysis results from static
    code analysis, complexity measurement, and style checking.

    Parameters
    ----------
    static_analysis_results : List[str]
        List of issues identified by static code analysis from
        perform_static_code_analysis node.
    vulnerabilities_found : List[str]
        List of vulnerabilities detected by static code analysis from
        perform_static_code_analysis node.
    complexity_metrics : List[float]
        List of complexity metrics for each file from
        measure_code_complexity node.
    cyclomatic_complexity : List[int]
        Cyclomatic complexity values for each file from
        measure_code_complexity node.
    style_issues : List[str]
        List of style issues identified by check_code_style node.
    formatting_errors : List[str]
        List of formatting errors detected by check_code_style node.

    Returns
    -------
    Tuple[str, List[str], float]
        A tuple containing the analysis summary, list of recommendations,
        and overall code quality score.

    Raises
    ------
    ValueError
        If any of the input lists are empty or invalid.

    Examples
    --------
    >>> static_analysis_results = ['issue1', 'issue2']
    >>> vulnerabilities_found = ['vuln1']
    >>> complexity_metrics = [0.5, 0.7]
    >>> cyclomatic_complexity = [3, 5]
    >>> style_issues = ['style_issue1']
    >>> formatting_errors = ['formatting_error1']
    >>> analysis_summary, recommendations, quality_score =
    compile_analysis_report(static_analysis_results, vulnerabilities_found,
    complexity_metrics, cyclomatic_complexity, style_issues, formatting_errors)
    ('Analysis Summary: Found 2 issues, 1 vulnerability, and 2 complexity
    metrics.', ['Fix issue1', 'Reduce cyclomatic complexity'], 0.8)

    """
    return CompileAnalysisReportOutput(
        analysis_summary="",
        recommendations=[],
        quality_score=0.0,
    )