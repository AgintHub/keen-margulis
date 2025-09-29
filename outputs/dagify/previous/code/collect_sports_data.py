from ._collect_sports_data.identify_data_sources import identify_data_sources
from ._collect_sports_data.establish_database_connections import establish_database_connections
from ._collect_sports_data.fetch_game_statistics_from_db import fetch_game_statistics_from_db
from ._collect_sports_data.fetch_player_information_from_apis import fetch_player_information_from_apis
from ._collect_sports_data.fetch_team_metrics_from_files import fetch_team_metrics_from_files
from ._collect_sports_data.validate_data_format import validate_data_format
from ._collect_sports_data.process_game_statistics import process_game_statistics
from ._collect_sports_data.process_player_information import process_player_information
from ._collect_sports_data.process_team_performance_metrics import process_team_performance_metrics
from ._collect_sports_data.close_connections import close_connections

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


def collect_sports_data(general_input: str, **kwargs) -> CollectSportsDataOutput:
    """
    Collects sports data from multiple sources and returns it along with a
    success indicator.

    Returns
    -------
    Tuple[List[str], List[str], List[float], bool]
        A tuple containing game statistics, player information, team
        performance metrics, and a boolean indicating if data collection was
        successful.

    Raises
    ------
    ConnectionError
        If there's an issue connecting to the data sources.
    DataFormatError
        If the collected data is not in the expected format.

    Examples
    --------
    >>> game_statistics, player_information, team_performance_metrics,
    is_data_collection_successful = collect_sports_data()
    (['stat1', 'stat2'], ['player1', 'player2'], [0.8, 0.9], True)

    >>> game_statistics, player_information, team_performance_metrics,
    is_data_collection_successful = collect_sports_data()
    ([], [], [], False)

    """
    data_sources: List[str] = identify_data_sources(input_query=general_input)
    
    db_connection_status: bool = establish_database_connections(sources=data_sources)
    if not db_connection_status:
        return CollectSportsDataOutput(
            game_statistics=[],
            player_information=[],
            team_performance_metrics=[],
            is_data_collection_successful=False
        )
    
    raw_game_data: List[dict] = fetch_game_statistics_from_db(query_params=general_input)
    raw_player_data: List[dict] = fetch_player_information_from_apis(sources=data_sources)
    raw_team_data: List[dict] = fetch_team_metrics_from_files(file_sources=data_sources)
    
    validated_game_data: bool = validate_data_format(data=raw_game_data, expected_type="game_stats")
    validated_player_data: bool = validate_data_format(data=raw_player_data, expected_type="player_info")
    validated_team_data: bool = validate_data_format(data=raw_team_data, expected_type="team_metrics")
    
    if not all([validated_game_data, validated_player_data, validated_team_data]):
        return CollectSportsDataOutput(
            game_statistics=[],
            player_information=[],
            team_performance_metrics=[],
            is_data_collection_successful=False
        )
    
    processed_game_stats: List[str] = process_game_statistics(raw_data=raw_game_data)
    processed_player_info: List[str] = process_player_information(raw_data=raw_player_data)
    processed_team_metrics: List[float] = process_team_performance_metrics(raw_data=raw_team_data)
    
    close_connections()
    
    return CollectSportsDataOutput(
        game_statistics=processed_game_stats,
        player_information=processed_player_info,
        team_performance_metrics=processed_team_metrics,
        is_data_collection_successful=True
    )