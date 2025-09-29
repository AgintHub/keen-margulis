from ._analyze_team_performance.validate_input_data import validate_input_data
from ._analyze_team_performance.calculate_key_performance_metrics import calculate_key_performance_metrics
from ._analyze_team_performance.identify_performance_trends import identify_performance_trends
from ._analyze_team_performance.identify_team_strengths import identify_team_strengths
from ._analyze_team_performance.identify_team_weaknesses import identify_team_weaknesses
from ._analyze_team_performance.determine_improvement_areas import determine_improvement_areas

from pydantic import BaseModel, Field
from typing import List


class CleanAndPreprocessDataOutput(BaseModel):
    """Pydantic model for clean_and_preprocess_data node outputs."""
    cleaned_game_statistics: List[float] = (
        Field(..., description="Cleaned game statistics")
    )
    preprocessed_player_information: List[str] = (
        Field(..., description="Preprocessed player information")
    )
    transformed_team_performance_metrics: List[float] = (
        Field(..., description="Transformed team performance metrics")
    )
    data_quality_score: float = (
        Field(..., description="Score indicating data quality")
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


def analyze_team_performance(clean_and_preprocess_data_input: CleanAndPreprocessDataOutput, **kwargs) -> AnalyzeTeamPerformanceOutput:
    """
    Analyze team performance using preprocessed data to determine key metrics
    and trends.

    Parameters
    ----------
    cleaned_game_statistics : List[float]
        Cleaned game statistics from the clean_and_preprocess_data node.
    transformed_team_performance_metrics : List[float]
        Transformed team performance metrics from the
        clean_and_preprocess_data node.

    Returns
    -------
    Tuple[List[float], List[str], List[str], List[str]]
        A tuple containing team performance metrics, team strengths, team
        weaknesses, and areas for team improvement.

    Raises
    ------
    ValueError
        If input data is empty or malformed.

    Examples
    --------
    >>> cleaned_game_statistics = [0.8, 0.7, 0.9]
    >>> transformed_team_performance_metrics = [0.85, 0.75, 0.95]
    >>> team_performance = analyze_team_performance(cleaned_game_statistics,
    transformed_team_performance_metrics)
    ([0.85, 0.75, 0.95], ['Strong offense'], ['Weak defense'], ['Improve
    teamwork'])

    """
    validate_input_data(game_stats=clean_and_preprocess_data_input.cleaned_game_statistics, performance_metrics=clean_and_preprocess_data_input.transformed_team_performance_metrics)
    
    calculated_metrics: List[float] = calculate_key_performance_metrics(game_stats=clean_and_preprocess_data_input.cleaned_game_statistics, performance_metrics=clean_and_preprocess_data_input.transformed_team_performance_metrics)
    
    performance_trends: List[float] = identify_performance_trends(metrics=calculated_metrics, game_stats=clean_and_preprocess_data_input.cleaned_game_statistics)
    
    team_strengths: List[str] = identify_team_strengths(metrics=calculated_metrics, trends=performance_trends)
    
    team_weaknesses: List[str] = identify_team_weaknesses(metrics=calculated_metrics, trends=performance_trends)
    
    improvement_areas: List[str] = determine_improvement_areas(strengths=team_strengths, weaknesses=team_weaknesses, metrics=calculated_metrics)
    
    return AnalyzeTeamPerformanceOutput(
        team_performance_metrics=calculated_metrics,
        team_strengths=team_strengths,
        team_weaknesses=team_weaknesses,
        areas_for_team_improvement=improvement_areas
    )