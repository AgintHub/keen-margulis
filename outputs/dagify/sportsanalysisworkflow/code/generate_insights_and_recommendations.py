from ._generate_insights_and_recommendations.validate_input_data import validate_input_data
from ._generate_insights_and_recommendations.analyze_player_insights import analyze_player_insights
from ._generate_insights_and_recommendations.analyze_team_insights import analyze_team_insights
from ._generate_insights_and_recommendations.combine_insights import combine_insights
from ._generate_insights_and_recommendations.generate_player_recommendations import generate_player_recommendations
from ._generate_insights_and_recommendations.generate_team_recommendations import generate_team_recommendations
from ._generate_insights_and_recommendations.combine_recommendations import combine_recommendations
from ._generate_insights_and_recommendations.calculate_confidence_score import calculate_confidence_score

from pydantic import BaseModel, Field
from typing import List


class AnalyzePlayerPerformanceOutput(BaseModel):
    """Pydantic model for analyze_player_performance node outputs."""
    player_performance_metrics: List[float] = (
        Field(..., description="List of player performance metrics")
    )
    player_strengths: List[str] = (
        Field(..., description="List of player strengths")
    )
    player_weaknesses: List[str] = (
        Field(..., description="List of player weaknesses")
    )
    areas_for_improvement: List[str] = (
        Field(..., description="List of areas for player improvement")
    )


class AnalyzeTeamPerformanceOutput(BaseModel):
    """Pydantic model for analyze_team_performance node outputs."""
    team_performance_metrics: List[float] = (
        Field(..., description="List of team performance metrics")
    )
    team_strengths: List[str] = Field(..., description="List of team strengths")
    team_weaknesses: List[str] = (
        Field(..., description="List of team weaknesses")
    )
    areas_for_team_improvement: List[str] = (
        Field(..., description="List of areas for team improvement")
    )


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


def generate_insights_and_recommendations(analyze_player_performance_input: AnalyzePlayerPerformanceOutput, analyze_team_performance_input: AnalyzeTeamPerformanceOutput, **kwargs) -> GenerateInsightsAndRecommendationsOutput:
    """
    Generate insights and recommendations based on player and team performance
    analysis.

    Parameters
    ----------
    player_performance_metrics : List[float]
        List of player performance metrics from analyze_player_performance
    player_strengths : List[str]
        List of player strengths from analyze_player_performance
    player_weaknesses : List[str]
        List of player weaknesses from analyze_player_performance
    areas_for_improvement : List[str]
        List of areas for player improvement from analyze_player_performance
    team_performance_metrics : List[float]
        List of team performance metrics from analyze_team_performance
    team_strengths : List[str]
        List of team strengths from analyze_team_performance
    team_weaknesses : List[str]
        List of team weaknesses from analyze_team_performance
    areas_for_team_improvement : List[str]
        List of areas for team improvement from analyze_team_performance

    Returns
    -------
    Tuple[List[str], List[str], float]
        A tuple containing a list of insights, a list of recommendations,
        and a confidence score.

    Raises
    ------
    ValueError
        If any of the input lists are empty or if the confidence score
        cannot be calculated.

    Examples
    --------
    >>> player_performance_metrics = [0.8, 0.7, 0.9]
    >>> player_strengths = ['Shooting', 'Passing']
    >>> player_weaknesses = ['Defense']
    >>> areas_for_improvement = ['Free throws']
    >>> team_performance_metrics = [0.85, 0.75, 0.95]
    >>> team_strengths = ['Teamwork', 'Strategy']
    >>> team_weaknesses = ['Communication']
    >>> areas_for_team_improvement = ['Coordination']
    >>> generate_insights_and_recommendations(player_performance_metrics,
    player_strengths, player_weaknesses, areas_for_improvement,
    team_performance_metrics, team_strengths, team_weaknesses,
    areas_for_team_improvement)
    (['Improve shooting and teamwork'], ['Practice free throws and
    coordination'], 0.9)

    >>> player_performance_metrics = [0.5, 0.6, 0.4]
    >>> player_strengths = ['Speed']
    >>> player_weaknesses = ['Accuracy']
    >>> areas_for_improvement = ['Shooting technique']
    >>> team_performance_metrics = [0.55, 0.65, 0.45]
    >>> team_strengths = ['Agility']
    >>> team_weaknesses = ['Endurance']
    >>> areas_for_team_improvement = ['Stamina training']
    >>> generate_insights_and_recommendations(player_performance_metrics,
    player_strengths, player_weaknesses, areas_for_improvement,
    team_performance_metrics, team_strengths, team_weaknesses,
    areas_for_team_improvement)
    (['Focus on accuracy and endurance'], ['Improve shooting technique and
    stamina'], 0.8)

    """
    validate_input_data(player_performance=analyze_player_performance_input, team_performance=analyze_team_performance_input)
    
    player_insights: List[str] = analyze_player_insights(metrics=analyze_player_performance_input.player_performance_metrics, strengths=analyze_player_performance_input.player_strengths, weaknesses=analyze_player_performance_input.player_weaknesses)
    
    team_insights: List[str] = analyze_team_insights(metrics=analyze_team_performance_input.team_performance_metrics, strengths=analyze_team_performance_input.team_strengths, weaknesses=analyze_team_performance_input.team_weaknesses)
    
    combined_insights: List[str] = combine_insights(player_insights=player_insights, team_insights=team_insights)
    
    player_recommendations: List[str] = generate_player_recommendations(areas_for_improvement=analyze_player_performance_input.areas_for_improvement, weaknesses=analyze_player_performance_input.player_weaknesses)
    
    team_recommendations: List[str] = generate_team_recommendations(areas_for_improvement=analyze_team_performance_input.areas_for_team_improvement, weaknesses=analyze_team_performance_input.team_weaknesses)
    
    combined_recommendations: List[str] = combine_recommendations(player_recommendations=player_recommendations, team_recommendations=team_recommendations)
    
    confidence_score: float = calculate_confidence_score(player_metrics=analyze_player_performance_input.player_performance_metrics, team_metrics=analyze_team_performance_input.team_performance_metrics)
    
    return GenerateInsightsAndRecommendationsOutput(
        insights=combined_insights,
        recommendations=combined_recommendations,
        confidence_score=confidence_score
    )