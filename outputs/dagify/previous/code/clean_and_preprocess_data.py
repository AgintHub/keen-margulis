from ._clean_and_preprocess_data.validate_input_data import validate_input_data
from ._clean_and_preprocess_data.handle_missing_values_and_convert_stats import handle_missing_values_and_convert_stats
from ._clean_and_preprocess_data.clean_and_normalize_player_information import clean_and_normalize_player_information
from ._clean_and_preprocess_data.normalize_and_transform_team_metrics import normalize_and_transform_team_metrics
from ._clean_and_preprocess_data.calculate_data_quality_score import calculate_data_quality_score

from pydantic import BaseModel, Field
from typing import List


class CollectSportsDataOutput(BaseModel):
    """Pydantic model for collect_sports_data node outputs."""
    game_statistics: List[str] = (
        Field(..., description="List of game statistics collected from various sources.")
    )
    player_information: List[str] = (
        Field(..., description="List of player information collected from various sources.")
    )
    team_performance_metrics: List[float] = (
        Field(..., description="List of team performance metrics collected from various sources.")
    )
    is_data_collection_successful: bool = (
        Field(..., description="Boolean indicating whether the data collection was successful.")
    )


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


def clean_and_preprocess_data(collect_sports_data_input: CollectSportsDataOutput, **kwargs) -> CleanAndPreprocessDataOutput:
    """
    Cleans and preprocesses raw sports data for analysis.

    Parameters
    ----------
    game_statistics : List[str]
        Raw game statistics collected from various sources.
    player_information : List[str]
        Raw player information collected from various sources.
    team_performance_metrics : List[float]
        Raw team performance metrics collected from various sources.
    is_data_collection_successful : bool
        Flag indicating whether data collection was successful.

    Returns
    -------
    Tuple[List[float], List[str], List[float], float]
        A tuple containing cleaned game statistics, preprocessed player
        information, transformed team performance metrics, and a data
        quality score.

    Raises
    ------
    ValueError
        If input data is malformed or missing critical information.
    TypeError
        If input data types do not match expected types.

    Examples
    --------
    >>> game_statistics = ['stat1', 'stat2', 'stat3']
    >>> player_information = ['player1', 'player2', 'player3']
    >>> team_performance_metrics = [0.8, 0.7, 0.9]
    >>> is_data_collection_successful = True
    >>> cleaned_data = clean_and_preprocess_data(game_statistics,
    player_information, team_performance_metrics, is_data_collection_successful)
    ([0.8, 0.7, 0.9], ['player1', 'player2', 'player3'], [0.8, 0.7, 0.9], 0.95)

    >>> game_statistics = ['stat1', None, 'stat3']
    >>> player_information = ['player1', 'player2', 'player3']
    >>> team_performance_metrics = [0.8, 0.7, 0.9]
    >>> is_data_collection_successful = True
    >>> cleaned_data = clean_and_preprocess_data(game_statistics,
    player_information, team_performance_metrics, is_data_collection_successful)
    ([0.8, 0.7, 0.9], ['player1', 'player2', 'player3'], [0.8, 0.7, 0.9], 0.92)

    """
    validate_input_data(collect_sports_data_input)
    
    if not collect_sports_data_input.is_data_collection_successful:
        raise ValueError("Data collection was not successful")
    
    cleaned_game_stats: List[float] = handle_missing_values_and_convert_stats(game_statistics=collect_sports_data_input.game_statistics)
    
    preprocessed_player_info: List[str] = clean_and_normalize_player_information(player_information=collect_sports_data_input.player_information)
    
    transformed_team_metrics: List[float] = normalize_and_transform_team_metrics(team_metrics=collect_sports_data_input.team_performance_metrics)
    
    quality_score: float = calculate_data_quality_score(
        original_stats=collect_sports_data_input.game_statistics,
        cleaned_stats=cleaned_game_stats,
        player_info=preprocessed_player_info,
        team_metrics=transformed_team_metrics
    )
    
    return CleanAndPreprocessDataOutput(
        cleaned_game_statistics=cleaned_game_stats,
        preprocessed_player_information=preprocessed_player_info,
        transformed_team_performance_metrics=transformed_team_metrics,
        data_quality_score=quality_score
    )