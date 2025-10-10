from typing import List


def get_popular_leagues(sport: str) -> List[str]:
    """
    Retrieve a list of prominent professional leagues for the specified sport.

    Parameters
    ----------
    sport : str
        The name of the sport for which to fetch popular leagues.

    Returns
    -------
    LIST_STR
        A list of league names (strings) that are considered the most
        popular or influential within the specified sport.

    Raises
    ------
    ValueError
        Raised when the provided sport name is not supported or cannot be
        matched to known sports.
    TypeError
        Raised when the sport argument is not of type str.

    Examples
    --------
    >>> leagues = get_popular_leagues('soccer')
    >>> print(leagues)
    ['Premier League', 'La Liga', 'Bundesliga']

    >>> leagues = get_popular_leagues('basketball')
    >>> print(leagues)
    ['NBA', 'EuroLeague', 'NBL']

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")