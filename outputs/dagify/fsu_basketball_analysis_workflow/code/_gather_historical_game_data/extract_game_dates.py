from typing import List


def extract_game_dates(games: str) -> List[str]:
    """
    Extracts game dates from a list of game records represented as a string.

    Parameters
    ----------
    games : str
        A string representation of a list of game records.

    Returns
    -------
    List[str]
        A list of game dates in string format.

    Raises
    ------
    ValueError
        If the input string is not a valid representation of game records.
    TypeError
        If the input is not of type string.

    Examples
    --------
    >>> games = '[{"date": "2022-01-01"}, {"date": "2022-01-15"}]'
    >>> extract_game_dates(games=games)
    ['2022-01-01', '2022-01-15']

    >>> games = '[{"date": "2023-02-01"}, {"date": "2023-03-01"}]'
    >>> extract_game_dates(games=games)
    ['2023-02-01', '2023-03-01']

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")