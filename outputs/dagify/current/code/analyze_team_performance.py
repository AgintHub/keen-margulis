from ._analyze_team_performance.validate_input_data import validate_input_data
from ._analyze_team_performance.parse_score_strings import parse_score_strings
from ._analyze_team_performance.count_wins import count_wins
from ._analyze_team_performance.count_losses import count_losses
from ._analyze_team_performance.format_win_loss_record import format_win_loss_record
from ._analyze_team_performance.extract_team_scores import extract_team_scores
from ._analyze_team_performance.extract_opponent_scores import extract_opponent_scores
from ._analyze_team_performance.calculate_average_score import calculate_average_score

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


class AnalyzeTeamPerformanceOutput(BaseModel):
    """Pydantic model for analyze_team_performance node outputs."""
    win_loss_record: str = (
        Field(..., description="Team win/loss record (e.g., '20-10')")
    )
    average_score: float = Field(..., description="Average score per game")
    average_opponent_score: float = (
        Field(..., description="Average opponent score per game")
    )


def analyze_team_performance(gather_historical_game_data_input: GatherHistoricalGameDataOutput, **kwargs) -> AnalyzeTeamPerformanceOutput:
    """
    Analyzes team performance based on historical game data, computing win/loss
    record and average scores.

    Parameters
    ----------
    game_dates : List[str]
        List of game dates from historical game data.
    opponents : List[str]
        List of opponents from historical game data.
    scores : List[str]
        List of game scores from historical game data, formatted as
        'team_score-opponent_score'.
    game_statistics : List[str]
        List of game statistics from historical game data.

    Returns
    -------
    Tuple[str, float, float]
        A tuple containing the team's win/loss record, average score, and
        average opponent score.

    Raises
    ------
    ValueError
        If the input lists are of different lengths or if scores are not
        properly formatted.

    Examples
    --------
    >>> game_dates = ['2023-01-01', '2023-01-03']
    >>> opponents = ['Team A', 'Team B']
    >>> scores = ['80-70', '75-85']
    >>> game_statistics = ['stats1', 'stats2']
    >>> analyze_team_performance(game_dates, opponents, scores, game_statistics)
    ('1-1', 77.5, 77.5)

    >>> game_dates = ['2023-02-01', '2023-02-03', '2023-02-05']
    >>> opponents = ['Team C', 'Team D', 'Team E']
    >>> scores = ['90-80', '85-95', '100-90']
    >>> game_statistics = ['stats3', 'stats4', 'stats5']
    >>> analyze_team_performance(game_dates, opponents, scores, game_statistics)
    ('2-1', 91.66666666666667, 88.33333333333333)

    """
    validated_data = validate_input_data(game_dates=gather_historical_game_data_input.game_dates,
                                          opponents=gather_historical_game_data_input.opponents,
                                          scores=gather_historical_game_data_input.scores,
                                          game_statistics=gather_historical_game_data_input.game_statistics)
    
    parsed_scores: List[tuple] = parse_score_strings(scores=gather_historical_game_data_input.scores)
    
    wins: int = count_wins(parsed_scores=parsed_scores)
    losses: int = count_losses(parsed_scores=parsed_scores)
    
    win_loss_record: str = format_win_loss_record(wins=wins, losses=losses)
    
    team_scores: List[int] = extract_team_scores(parsed_scores=parsed_scores)
    opponent_scores: List[int] = extract_opponent_scores(parsed_scores=parsed_scores)
    
    average_score: float = calculate_average_score(scores=team_scores)
    average_opponent_score: float = calculate_average_score(scores=opponent_scores)
    
    return AnalyzeTeamPerformanceOutput(
        win_loss_record=win_loss_record,
        average_score=average_score,
        average_opponent_score=average_opponent_score
    )