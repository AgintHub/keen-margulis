from ._gather_historical_game_data.identify_fsu_basketball_data_sources import identify_fsu_basketball_data_sources
from ._gather_historical_game_data.fetch_historical_game_records import fetch_historical_game_records
from ._gather_historical_game_data.validate_game_data_integrity import validate_game_data_integrity
from ._gather_historical_game_data.extract_game_dates import extract_game_dates
from ._gather_historical_game_data.extract_opponent_names import extract_opponent_names
from ._gather_historical_game_data.format_game_scores import format_game_scores
from ._gather_historical_game_data.compile_game_statistics import compile_game_statistics

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


def gather_historical_game_data(general_input: str, **kwargs) -> GatherHistoricalGameDataOutput:
    """
    Gathers historical game data for the FSU basketball team.

    Returns
    -------
    Tuple[List[str], List[str], List[str], List[str]]
        A tuple containing lists of game dates, opponents, scores, and game
        statistics.

    Raises
    ------
    DataCollectionError
        If there's an issue collecting the historical game data.

    Examples
    --------
    >>> game_data = gather_historical_game_data()
    >>> print(game_data)
    (['2023-01-01', '2023-01-03'], ['Team A', 'Team B'], ['74-68', '80-75'],
    ['Rebounds: 40, Turnovers: 15', 'Rebounds: 35, Turnovers: 10'])

    """
    data_sources: List[str] = identify_fsu_basketball_data_sources()
    raw_game_data: List[dict] = fetch_historical_game_records(sources=data_sources, team="FSU")
    validated_games: List[dict] = validate_game_data_integrity(raw_data=raw_game_data)
    game_dates: List[str] = extract_game_dates(games=validated_games)
    opponents: List[str] = extract_opponent_names(games=validated_games)
    scores: List[str] = format_game_scores(games=validated_games)
    game_statistics: List[str] = compile_game_statistics(games=validated_games)
    return GatherHistoricalGameDataOutput(
        game_dates=game_dates,
        opponents=opponents,
        scores=scores,
        game_statistics=game_statistics
    )