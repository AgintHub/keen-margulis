from ._integrate_analysis_results.validate_input_data import validate_input_data
from ._integrate_analysis_results.synthesize_strengths import synthesize_strengths
from ._integrate_analysis_results.synthesize_weaknesses import synthesize_weaknesses
from ._integrate_analysis_results.analyze_capabilities import analyze_capabilities
from ._integrate_analysis_results.generate_future_outlook import generate_future_outlook
from ._integrate_analysis_results.compile_wcfb_report import compile_wcfb_report
from ._integrate_analysis_results.generate_recommendations import generate_recommendations
from ._integrate_analysis_results.create_implementation_roadmap import create_implementation_roadmap

from pydantic import BaseModel, Field
from typing import List


class AnalyzeBusinessOperationsOutput(BaseModel):
    """Pydantic model for analyze_business_operations node outputs."""
    strengths: List[str] = (
        Field(..., description="List of business operation strengths")
    )
    weaknesses: List[str] = (
        Field(..., description="List of business operation weaknesses")
    )
    efficiency_metrics: List[float] = (
        Field(..., description="List of efficiency metrics for business operations")
    )


class ExamineCustomerFeedbackOutput(BaseModel):
    """Pydantic model for examine_customer_feedback node outputs."""
    customer_satisfaction_score: float = (
        Field(..., description="Overall customer satisfaction score")
    )
    common_complaints: List[str] = (
        Field(..., description="List of common customer complaints")
    )
    positive_feedback_themes: List[str] = (
        Field(..., description="List of themes from positive customer feedback")
    )


class AssessMarketTrendsOutput(BaseModel):
    """Pydantic model for assess_market_trends node outputs."""
    market_opportunities: List[str] = (
        Field(..., description="List of market opportunities")
    )
    market_threats: List[str] = Field(..., description="List of market threats")
    trend_forecast: str = (
        Field(..., description="Forecast of future market trends")
    )


class IntegrateAnalysisResultsOutput(BaseModel):
    """Pydantic model for integrate_analysis_results node outputs."""
    wcfb_analysis_report: str = (
        Field(..., description="Comprehensive WCFB analysis report")
    )
    key_recommendations: str = (
        Field(..., description="List of key recommendations based on the WCFB analysis")
    )
    implementation_roadmap: str = (
        Field(..., description="List of steps for implementing the recommendations")
    )


def integrate_analysis_results(analyze_business_operations_input: AnalyzeBusinessOperationsOutput, examine_customer_feedback_input: ExamineCustomerFeedbackOutput, assess_market_trends_input: AssessMarketTrendsOutput, **kwargs) -> IntegrateAnalysisResultsOutput:
    """
    Integrates analysis results from multiple sources into a comprehensive WCFB
    analysis report, key recommendations, and an implementation roadmap.

    Parameters
    ----------
    business_operations_analysis : dict
        Results from business operations analysis, including strengths,
        weaknesses, and efficiency metrics.
    customer_feedback_examination : dict
        Results from customer feedback examination, including customer
        satisfaction score, common complaints, and positive feedback themes.
    market_trends_assessment : dict
        Results from market trends assessment, including market
        opportunities, market threats, and trend forecast.

    Returns
    -------
    tuple[str, list[str], list[str]]
        A tuple containing the comprehensive WCFB analysis report, key
        recommendations, and implementation roadmap.

    Raises
    ------
    ValueError
        If any of the input analysis results are missing or invalid.

    Examples
    --------
    >>> business_operations_analysis = {'strengths': ['Efficient supply chain'],
    'weaknesses': ['High employee turnover'], 'efficiency_metrics': [0.8]}
    >>> customer_feedback_examination = {'customer_satisfaction_score': 0.7,
    'common_complaints': ['Poor customer service'], 'positive_feedback_themes':
    ['Quality products']}
    >>> market_trends_assessment = {'market_opportunities': ['Growing demand for
    eco-friendly products'], 'market_threats': ['Increasing competition'],
    'trend_forecast': 'Steady growth'}
    >>> integrate_analysis_results(business_operations_analysis,
    customer_feedback_examination, market_trends_assessment)
    ('Comprehensive WCFB analysis report...', ['Improve customer service',
    'Invest in eco-friendly products'], ['Step 1: Train customer service staff',
    'Step 2: Develop eco-friendly product line'])

    """
    validate_input_data(business_ops=analyze_business_operations_input, customer_feedback=examine_customer_feedback_input, market_trends=assess_market_trends_input)
    
    strengths_analysis: str = synthesize_strengths(strengths=analyze_business_operations_input.strengths, positive_themes=examine_customer_feedback_input.positive_feedback_themes, opportunities=assess_market_trends_input.market_opportunities)
    
    weaknesses_analysis: str = synthesize_weaknesses(weaknesses=analyze_business_operations_input.weaknesses, complaints=examine_customer_feedback_input.common_complaints, threats=assess_market_trends_input.market_threats)
    
    capabilities_analysis: str = analyze_capabilities(efficiency_metrics=analyze_business_operations_input.efficiency_metrics, satisfaction_score=examine_customer_feedback_input.customer_satisfaction_score)
    
    future_outlook: str = generate_future_outlook(trend_forecast=assess_market_trends_input.trend_forecast, current_performance=capabilities_analysis)
    
    wcfb_report: str = compile_wcfb_report(strengths=strengths_analysis, weaknesses=weaknesses_analysis, capabilities=capabilities_analysis, future_outlook=future_outlook)
    
    recommendations: str = generate_recommendations(weaknesses=analyze_business_operations_input.weaknesses, complaints=examine_customer_feedback_input.common_complaints, opportunities=assess_market_trends_input.market_opportunities, threats=assess_market_trends_input.market_threats)
    
    roadmap: str = create_implementation_roadmap(recommendations=recommendations, current_capabilities=capabilities_analysis)
    
    return IntegrateAnalysisResultsOutput(
        wcfb_analysis_report=wcfb_report,
        key_recommendations=recommendations,
        implementation_roadmap=roadmap
    )