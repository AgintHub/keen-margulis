from typing import List


def format_game_scores(games: str) -> List[str]:
    """
    Formats game scores from a list of game records into a list of score
    strings.

    Parameters
    ----------
    games : str
        A string representation of game records, expected to be a JSON-like
        structure containing game information including scores.

    Returns
    -------
    List[str]
        A list of strings where each string represents a formatted game
        score (e.g., '74-68').

    Raises
    ------
    ValueError
        If the input string cannot be parsed into a valid game record
        structure.
    TypeError
        If the input is not a string.

    Examples
    --------
    >>> games = '[{"score": "74-68"}, {"score": "80-75"}]'
    >>> format_game_scores(games=games)
    ['74-68', '80-75']

    >>> games = '[{"score": "60-70"}]'
    >>> format_game_scores(games=games)
    ['60-70']

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")