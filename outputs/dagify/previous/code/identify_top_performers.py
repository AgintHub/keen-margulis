from ._identify_top_performers.validate_input_lists import validate_input_lists
from ._identify_top_performers.rank_players_by_metric import rank_players_by_metric

from pydantic import BaseModel, Field
from typing import List


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


class IdentifyTopPerformersOutput(BaseModel):
    """Pydantic model for identify_top_performers node outputs."""
    top_scorers: List[str] = Field(..., description="List of top scorers")
    top_rebounders: List[str] = Field(..., description="List of top rebounders")
    top_assisters: List[str] = Field(..., description="List of top assisters")


def identify_top_performers(extract_player_statistics_input: ExtractPlayerStatisticsOutput, **kwargs) -> IdentifyTopPerformersOutput:
    """
    Identify top performing players based on points scored, rebounds, assists,
    and other relevant metrics.

    Parameters
    ----------
    player_names : List[str]
        List of player names extracted from game data.
    points_scored : List[int]
        List of total points scored by each player.
    rebounds : List[int]
        List of total rebounds by each player.
    assists : List[int]
        List of total assists by each player.

    Returns
    -------
    Tuple[List[str], List[str], List[str]]
        A tuple containing lists of top scorers, top rebounders, and top
        assisters.

    Raises
    ------
    ValueError
        If the input lists are of different lengths.
    TypeError
        If the input types are not as expected.

    Examples
    --------
    >>> player_names = ['Player1', 'Player2', 'Player3']
    >>> points_scored = [20, 15, 25]
    >>> rebounds = [5, 10, 7]
    >>> assists = [8, 6, 9]
    >>> top_scorers, top_rebounders, top_assisters =
    identify_top_performers(player_names, points_scored, rebounds, assists)
    (['Player3', 'Player1', 'Player2'], ['Player2', 'Player3', 'Player1'],
    ['Player3', 'Player1', 'Player2'])

    >>> player_names = ['PlayerA', 'PlayerB']
    >>> points_scored = [30, 20]
    >>> rebounds = [8, 12]
    >>> assists = [7, 5]
    >>> top_scorers, top_rebounders, top_assisters =
    identify_top_performers(player_names, points_scored, rebounds, assists)
    (['PlayerA', 'PlayerB'], ['PlayerB', 'PlayerA'], ['PlayerA', 'PlayerB'])

    """
    validate_input_lists(player_names=extract_player_statistics_input.player_names, 
                          points_scored=extract_player_statistics_input.points_scored,
                          rebounds=extract_player_statistics_input.rebounds,
                          assists=extract_player_statistics_input.assists)
    
    sorted_scorers: List[str] = rank_players_by_metric(player_names=extract_player_statistics_input.player_names,
                                                         metric_values=extract_player_statistics_input.points_scored)
    
    sorted_rebounders: List[str] = rank_players_by_metric(player_names=extract_player_statistics_input.player_names,
                                                            metric_values=extract_player_statistics_input.rebounds)
    
    sorted_assisters: List[str] = rank_players_by_metric(player_names=extract_player_statistics_input.player_names,
                                                           metric_values=extract_player_statistics_input.assists)
    
    return IdentifyTopPerformersOutput(
        top_scorers=sorted_scorers,
        top_rebounders=sorted_rebounders,
        top_assisters=sorted_assisters
    )