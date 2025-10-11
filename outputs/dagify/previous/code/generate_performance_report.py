from ._generate_performance_report.validate_input_data import validate_input_data
from ._generate_performance_report.format_team_statistics import format_team_statistics
from ._generate_performance_report.create_top_performers_summary import create_top_performers_summary
from ._generate_performance_report.generate_comprehensive_summary import generate_comprehensive_summary

from pydantic import BaseModel, Field
from typing import List


class AnalyzeTeamPerformanceOutput(BaseModel):
    """Pydantic model for analyze_team_performance node outputs."""
    win_loss_record: str = (
        Field(..., description="Team win/loss record (e.g., '20-10')")
    )
    average_score: float = Field(..., description="Average score per game")
    average_opponent_score: float = (
        Field(..., description="Average opponent score per game")
    )


class IdentifyTopPerformersOutput(BaseModel):
    """Pydantic model for identify_top_performers node outputs."""
    top_scorers: List[str] = Field(..., description="List of top scorers")
    top_rebounders: List[str] = Field(..., description="List of top rebounders")
    top_assisters: List[str] = Field(..., description="List of top assisters")


class GeneratePerformanceReportOutput(BaseModel):
    """Pydantic model for generate_performance_report node outputs."""
    report_summary: str = (
        Field(..., description="Summary of the performance report")
    )
    team_statistics: List[str] = (
        Field(..., description="List of key team statistics")
    )
    top_performers_summary: str = (
        Field(..., description="Summary of top performers")
    )


def generate_performance_report(analyze_team_performance_input: AnalyzeTeamPerformanceOutput, identify_top_performers_input: IdentifyTopPerformersOutput, **kwargs) -> GeneratePerformanceReportOutput:
    """
    Generate a comprehensive performance report for the FSU basketball team.

    Parameters
    ----------
    team_performance_analysis : dict
        Analysis of team performance including win/loss record, average
        score, and average opponent score.
    top_performers : dict
        Identification of top performers including top scorers, rebounders,
        and assisters.

    Returns
    -------
    dict
        A dictionary containing the report summary, team statistics, and top
        performers summary.

    Raises
    ------
    ValueError
        If team performance analysis or top performers data is missing or
        invalid.

    Examples
    --------
    >>> team_performance_analysis = {'win_loss_record': '20-10',
    'average_score': 74.5, 'average_opponent_score': 68.2}
    >>> top_performers = {'top_scorers': ['Player1', 'Player2'],
    'top_rebounders': ['Player3'], 'top_assisters': ['Player4']}
    >>> generate_performance_report(team_performance_analysis, top_performers)
    {'report_summary': 'The team had a 20-10 record with an average score of
    74.5 and average opponent score of 68.2. Top scorers were Player1 and
    Player2.', 'team_statistics': ['Win/Loss Record: 20-10', 'Average Score:
    74.5', 'Average Opponent Score: 68.2'], 'top_performers_summary': 'Top
    scorers: Player1, Player2. Top rebounders: Player3. Top assisters:
    Player4.'}

    """
    validate_input_data(team_data=analyze_team_performance_input, performers_data=identify_top_performers_input)
    
    team_stats: List[str] = format_team_statistics(
        win_loss=analyze_team_performance_input.win_loss_record,
        avg_score=analyze_team_performance_input.average_score,
        avg_opponent_score=analyze_team_performance_input.average_opponent_score
    )
    
    performers_summary: str = create_top_performers_summary(
        scorers=identify_top_performers_input.top_scorers,
        rebounders=identify_top_performers_input.top_rebounders,
        assisters=identify_top_performers_input.top_assisters
    )
    
    report_summary: str = generate_comprehensive_summary(
        team_performance=analyze_team_performance_input,
        top_performers=identify_top_performers_input
    )
    
    return GeneratePerformanceReportOutput(
        report_summary=report_summary,
        team_statistics=team_stats,
        top_performers_summary=performers_summary
    )