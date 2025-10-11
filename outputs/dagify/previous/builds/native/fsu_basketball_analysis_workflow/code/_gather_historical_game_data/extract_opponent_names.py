from typing import List


def extract_opponent_names(games: str) -> List[str]:
    """
    Extracts opponent names from the provided games data string.

    Parameters
    ----------
    games : str
        A string representing the games data from which opponent names will
        be extracted.

    Returns
    -------
    List[str]
        A list of strings representing the names of opponents extracted from
        the input games data.

    Raises
    ------
    ValueError
        If the input games data is not in the expected format or is empty.
    TypeError
        If the input games data is not a string.

    Examples
    --------
    >>> extract_opponent_names(games='[{\"opponent\": \"Team A\"},
    {\"opponent\": \"Team B\"}]')
    ['Team A', 'Team B']

    >>> extract_opponent_names(games='[{\"opponent\": \"Team C\"}]')
    ['Team C']

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")