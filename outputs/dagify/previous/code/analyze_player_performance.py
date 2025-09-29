from ._analyze_player_performance.validate_input_data import validate_input_data
from ._analyze_player_performance.calculate_performance_metrics import calculate_performance_metrics
from ._analyze_player_performance.identify_player_strengths import identify_player_strengths
from ._analyze_player_performance.identify_player_weaknesses import identify_player_weaknesses
from ._analyze_player_performance.determine_improvement_areas import determine_improvement_areas

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


def analyze_player_performance(clean_and_preprocess_data_input: CleanAndPreprocessDataOutput, **kwargs) -> AnalyzePlayerPerformanceOutput:
    """
    Analyzes player performance using preprocessed data to identify key metrics
    and trends.

    Parameters
    ----------
    preprocessed_player_information : List[str]
        Preprocessed player information from the clean_and_preprocess_data
        node.
    cleaned_game_statistics : List[float]
        Cleaned game statistics from the clean_and_preprocess_data node.

    Returns
    -------
    Tuple[List[float], List[str], List[str], List[str]]
        A tuple containing player performance metrics, strengths,
        weaknesses, and areas for improvement.

    Raises
    ------
    ValueError
        If preprocessed_player_information or cleaned_game_statistics are
        empty or malformed.

    Examples
    --------
    >>> preprocessed_data = ['Player1', 'Player2']
    >>> game_stats = [0.8, 0.9]
    >>> result = analyze_player_performance(preprocessed_data, game_stats)
    ([0.85, 0.9], ['Consistency'], ['Scoring'], ['Defense'])

    """
    validate_input_data(preprocessed_player_info=clean_and_preprocess_data_input.preprocessed_player_information, game_stats=clean_and_preprocess_data_input.cleaned_game_statistics)
    
    performance_metrics: List[float] = calculate_performance_metrics(game_statistics=clean_and_preprocess_data_input.cleaned_game_statistics, player_info=clean_and_preprocess_data_input.preprocessed_player_information)
    
    strengths: List[str] = identify_player_strengths(performance_metrics=performance_metrics, player_info=clean_and_preprocess_data_input.preprocessed_player_information)
    
    weaknesses: List[str] = identify_player_weaknesses(performance_metrics=performance_metrics, game_stats=clean_and_preprocess_data_input.cleaned_game_statistics)
    
    improvement_areas: List[str] = determine_improvement_areas(strengths=strengths, weaknesses=weaknesses, performance_metrics=performance_metrics)
    
    return AnalyzePlayerPerformanceOutput(
        player_performance_metrics=performance_metrics,
        player_strengths=strengths,
        player_weaknesses=weaknesses,
        areas_for_improvement=improvement_areas
    )