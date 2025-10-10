from ._generate_color_analysis_report.validate_input_data import validate_input_data
from ._generate_color_analysis_report.analyze_color_patterns import analyze_color_patterns
from ._generate_color_analysis_report.generate_report_summary import generate_report_summary
from ._generate_color_analysis_report.create_color_distribution_chart import create_color_distribution_chart
from ._generate_color_analysis_report.validate_report_quality import validate_report_quality

from ._generate_color_analysis_report.validate_input_data import validate_input_data
from ._generate_color_analysis_report.analyze_color_patterns import analyze_color_patterns
from ._generate_color_analysis_report.generate_report_summary import generate_report_summary
from ._generate_color_analysis_report.create_color_distribution_chart import create_color_distribution_chart
from ._generate_color_analysis_report.validate_report_quality import validate_report_quality

from pydantic import BaseModel, Field
from typing import List


class AnalyzeColorDistributionOutput(BaseModel):
    """Pydantic model for analyze_color_distribution node outputs."""
    color_frequencies: List[float] = (
        Field(..., description="Frequency of each observed vehicle color")
    )
    most_common_colors: List[str] = (
        Field(..., description="List of most common vehicle colors observed")
    )
    color_distribution_stats: List[float] = (
        Field(..., description = (
            "Statistical measures (mean, median, std dev) of color distribution")
        )
    )


class GenerateColorAnalysisReportOutput(BaseModel):
    """Pydantic model for generate_color_analysis_report node outputs."""
    report_summary: str = (
        Field(..., description = (
            "Summary of key findings from the color analysis")
        )
    )
    color_distribution_visualization: str = (
        Field(..., description = (
            "Path to visualization file showing color distribution")
        )
    )
    is_report_valid: bool = (
        Field(..., description = (
            "Whether the generated report is valid and accurate")
        )
    )


def generate_color_analysis_report(analyze_color_distribution_input: AnalyzeColorDistributionOutput, **kwargs) -> GenerateColorAnalysisReportOutput:
    """
    Generate a detailed report on vehicle color analysis during rush hour.

    Parameters
    ----------
    color_frequencies : List[float]
        Frequency of each observed vehicle color from the analysis.
    most_common_colors : List[str]
        List of most common vehicle colors observed during rush hour.
    color_distribution_stats : List[float]
        Statistical measures (mean, median, std dev) of color distribution.

    Returns
    -------
    Tuple[str, str, bool]
        A tuple containing the report summary, path to color distribution
        visualization, and a boolean indicating report validity.

    Raises
    ------
    ValueError
        If input data is inconsistent or missing required fields.
    RuntimeError
        If visualization generation fails.

    Examples
    --------
    >>> color_frequencies = [0.3, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1]
    >>> most_common_colors = ['black', 'white', 'gray', 'red', 'blue', 'silver',
    'other']
    >>> color_distribution_stats = [0.2, 0.1, 0.05]
    >>> report_summary, visualization_path, is_valid =
    generate_color_analysis_report(color_frequencies, most_common_colors,
    color_distribution_stats)
    ('Summary: Black and white are most common...',
    '/path/to/visualization.png', True)

    >>> color_frequencies = [0.4, 0.3, 0.3]
    >>> most_common_colors = ['black', 'white', 'gray']
    >>> color_distribution_stats = [0.3, 0.3, 0.0]
    >>> report_summary, visualization_path, is_valid =
    generate_color_analysis_report(color_frequencies, most_common_colors,
    color_distribution_stats)
    ('Summary: Black and white dominate...', '/path/to/visualization2.png',
    True)

    """
    validated_data: bool = validate_input_data(
        color_frequencies=analyze_color_distribution_input.color_frequencies,
        most_common_colors=analyze_color_distribution_input.most_common_colors,
        color_distribution_stats=analyze_color_distribution_input.color_distribution_stats
    )
    
    if not validated_data:
        raise ValueError("Input data is inconsistent or missing required fields")
    
    key_insights: List[str] = analyze_color_patterns(
        frequencies=analyze_color_distribution_input.color_frequencies,
        colors=analyze_color_distribution_input.most_common_colors,
        stats=analyze_color_distribution_input.color_distribution_stats
    )
    
    summary_text: str = generate_report_summary(
        insights=key_insights,
        most_common_colors=analyze_color_distribution_input.most_common_colors,
        distribution_stats=analyze_color_distribution_input.color_distribution_stats
    )
    
    visualization_path: str = create_color_distribution_chart(
        color_frequencies=analyze_color_distribution_input.color_frequencies,
        color_names=analyze_color_distribution_input.most_common_colors
    )
    
    if not visualization_path:
        raise RuntimeError("Visualization generation fails")
    
    is_valid: bool = validate_report_quality(
        summary=summary_text,
        visualization_path=visualization_path,
        input_data=analyze_color_distribution_input
    )
    
    return GenerateColorAnalysisReportOutput(
        report_summary=summary_text,
        color_distribution_visualization=visualization_path,
        is_report_valid=is_valid
    )