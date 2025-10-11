from ._extract_player_statistics.validate_input_lists_length import validate_input_lists_length
from ._extract_player_statistics.validate_input_data_types import validate_input_data_types
from ._extract_player_statistics.parse_game_statistics import parse_game_statistics
from ._extract_player_statistics.aggregate_player_statistics import aggregate_player_statistics
from ._extract_player_statistics.extract_player_names import extract_player_names
from ._extract_player_statistics.extract_points_scored import extract_points_scored
from ._extract_player_statistics.extract_rebounds import extract_rebounds
from ._extract_player_statistics.extract_assists import extract_assists

from pydantic import BaseModel, Field
from typing import List


class GatherHistoricalGameDataOutput(BaseModel):
    """Pydantic model for gather_historical_game_data node outputs."""
    game_dates: List[str] = Field(..., description="List of game dates")
    opponents: List[str] = Field(..., description="List of opponents")
    scores: List[str] = (
        Field(..., description="List of game scores (e.g., '74-68')")
    )
    game_statistics: List[str] = (
        Field(..., description="List of game statistics (e.g., rebounds, turnovers, etc.)")
    )


class ExtractPlayerStatisticsOutput(BaseModel):
    """Pydantic model for extract_player_statistics node outputs."""
    player_names: List[str] = Field(..., description="List of player names")
    points_scored: List[int] = (
        Field(..., description="List of total points scored by each player")
    )
    rebounds: List[int] = (
        Field(..., description="List of total rebounds by each player")
    )
    assists: List[int] = (
        Field(..., description="List of total assists by each player")
    )


def extract_player_statistics(gather_historical_game_data_input: GatherHistoricalGameDataOutput, **kwargs) -> ExtractPlayerStatisticsOutput:
    """
    Extracts player statistics from historical game data, returning lists of
    player names and their respective statistics.

    Parameters
    ----------
    game_dates : List[str]
        List of game dates from the historical game data.
    opponents : List[str]
        List of opponents from the historical game data.
    scores : List[str]
        List of game scores from the historical game data.
    game_statistics : List[str]
        List of game statistics from the historical game data.

    Returns
    -------
    Tuple[List[str], List[int], List[int], List[int]]
        A tuple containing lists of player names, points scored, rebounds,
        and assists.

    Raises
    ------
    ValueError
        If the input lists are not of the same length.
    TypeError
        If the input data types are not as expected.

    Examples
    --------
    >>> game_dates = ['2022-01-01', '2022-01-03']
    >>> opponents = ['Team A', 'Team B']
    >>> scores = ['80-70', '90-85']
    >>> game_statistics = ['Player1:20,5,3;Player2:15,7,2',
    'Player1:22,6,4;Player2:18,8,3']
    >>> extract_player_statistics(game_dates, opponents, scores,
    game_statistics)
    (['Player1', 'Player2'], [42, 33], [11, 15], [7, 5])

    >>> game_dates = ['2022-02-01']
    >>> opponents = ['Team C']
    >>> scores = ['100-90']
    >>> game_statistics = ['Player1:25,4,5;Player2:20,6,4']
    >>> extract_player_statistics(game_dates, opponents, scores,
    game_statistics)
    (['Player1', 'Player2'], [25, 20], [4, 6], [5, 4])

    """
    validate_input_lists_length(game_dates=gather_historical_game_data_input.game_dates, 
                                  opponents=gather_historical_game_data_input.opponents,
                                  scores=gather_historical_game_data_input.scores,
                                  game_statistics=gather_historical_game_data_input.game_statistics)
    
    validate_input_data_types(game_dates=gather_historical_game_data_input.game_dates,
                                opponents=gather_historical_game_data_input.opponents,
                                scores=gather_historical_game_data_input.scores,
                                game_statistics=gather_historical_game_data_input.game_statistics)
    
    parsed_game_stats: List[dict] = parse_game_statistics(game_statistics=gather_historical_game_data_input.game_statistics)
    
    aggregated_stats: dict = aggregate_player_statistics(parsed_stats=parsed_game_stats)
    
    player_names: List[str] = extract_player_names(aggregated_stats=aggregated_stats)
    points_scored: List[int] = extract_points_scored(aggregated_stats=aggregated_stats, player_names=player_names)
    rebounds: List[int] = extract_rebounds(aggregated_stats=aggregated_stats, player_names=player_names)
    assists: List[int] = extract_assists(aggregated_stats=aggregated_stats, player_names=player_names)
    
    return ExtractPlayerStatisticsOutput(
        player_names=player_names,
        points_scored=points_scored,
        rebounds=rebounds,
        assists=assists
    )