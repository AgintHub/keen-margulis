from ._produce_sports_analysis_report.validate_input_data import validate_input_data
from ._produce_sports_analysis_report.generate_executive_summary import generate_executive_summary
from ._produce_sports_analysis_report.compile_detailed_findings import compile_detailed_findings
from ._produce_sports_analysis_report.format_actionable_recommendations import format_actionable_recommendations
from ._produce_sports_analysis_report.calculate_report_quality_score import calculate_report_quality_score

from pydantic import BaseModel, Field
from typing import List


class GenerateInsightsAndRecommendationsOutput(BaseModel):
    """Pydantic model for generate_insights_and_recommendations node outputs."""
    insights: List[str] = (
        Field(..., description="List of insights derived from the analysis")
    )
    recommendations: List[str] = (
        Field(..., description="List of recommendations for improvement")
    )
    confidence_score: float = (
        Field(..., description="Score indicating confidence in the recommendations")
    )


class ProduceSportsAnalysisReportOutput(BaseModel):
    """Pydantic model for produce_sports_analysis_report node outputs."""
    executive_summary: str = (
        Field(..., description="Brief summary of key findings and recommendations")
    )
    detailed_findings: List[str] = (
        Field(..., description="List of detailed findings")
    )
    actionable_recommendations: List[str] = (
        Field(..., description="List of actionable recommendations")
    )
    report_score: float = (
        Field(..., description="Score indicating the quality and reliability of the report")
    )


def produce_sports_analysis_report(generate_insights_and_recommendations_input: GenerateInsightsAndRecommendationsOutput, **kwargs) -> ProduceSportsAnalysisReportOutput:
    """
    Produces a sports analysis report summarizing key findings, insights, and
    recommendations.

    Parameters
    ----------
    insights_and_recommendations : dict
        Dictionary containing insights, recommendations, and confidence
        score from the generate_insights_and_recommendations node.

    Returns
    -------
    dict
        Dictionary containing executive summary, detailed findings,
        actionable recommendations, and report score.

    Raises
    ------
    ValueError
        If insights_and_recommendations is not a valid dictionary or missing
        required keys.
    TypeError
        If the input types do not match the expected types.

    Examples
    --------
    >>> insights_and_recommendations = {'insights': ['Player A is improving'],
    'recommendations': ['Focus on Player A'], 'confidence_score': 0.8}
    >>> report = produce_sports_analysis_report(insights_and_recommendations)
    {'executive_summary': 'Summary of key findings...', 'detailed_findings':
    ['Finding 1', 'Finding 2'], 'actionable_recommendations': ['Recommendation
    1'], 'report_score': 0.9}

    """
    validated_input: dict = validate_input_data(input_data=generate_insights_and_recommendations_input)
    
    executive_summary: str = generate_executive_summary(
        insights=validated_input['insights'],
        recommendations=validated_input['recommendations'],
        confidence_score=validated_input['confidence_score']
    )
    
    detailed_findings: List[str] = compile_detailed_findings(
        insights=validated_input['insights'],
        confidence_score=validated_input['confidence_score']
    )
    
    actionable_recommendations: List[str] = format_actionable_recommendations(
        recommendations=validated_input['recommendations']
    )
    
    report_score: float = calculate_report_quality_score(
        confidence_score=validated_input['confidence_score'],
        num_insights=len(validated_input['insights']),
        num_recommendations=len(validated_input['recommendations'])
    )
    
    return ProduceSportsAnalysisReportOutput(
        executive_summary=executive_summary,
        detailed_findings=detailed_findings,
        actionable_recommendations=actionable_recommendations,
        report_score=report_score
    )