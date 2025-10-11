from typing import List


def format_team_statistics(win_loss: str, avg_score: str, avg_opponent_score: str) -> List[str]:
    """
    Formats team statistics into a list of strings based on the provided
    win/loss record, average score, and average opponent score.

    Parameters
    ----------
    win_loss : str
        The team's win/loss record in the format 'wins-losses'.
    avg_score : str
        The average score of the team per game.
    avg_opponent_score : str
        The average score of the team's opponents per game.

    Returns
    -------
    List[str]
        A list of strings representing the formatted team statistics.

    Raises
    ------
    ValueError
        If the win/loss record is not in the correct format.
    TypeError
        If any of the input parameters are not strings.

    Examples
    --------
    >>> format_team_statistics(win_loss='20-10', avg_score='80.5',
    avg_opponent_score='75.2')
    ['Win/Loss Record: 20-10', 'Average Score: 80.5', 'Average Opponent Score:
    75.2']

    >>> format_team_statistics(win_loss='15-15', avg_score='70.0',
    avg_opponent_score='70.0')
    ['Win/Loss Record: 15-15', 'Average Score: 70.0', 'Average Opponent Score:
    70.0']

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")