from typing import List


def get_major_tournaments(sport: str) -> List[str]:
    """
    Return a list of major international tournaments for the specified sport.

    Parameters
    ----------
    sport : str
        Name of the sport for which to retrieve major tournaments.

    Returns
    -------
    list
        A list of strings, each string being the name of a major tournament
        associated with the sport.

    Raises
    ------
    ValueError
        Raised when the sport name is not recognized or supported.
    TypeError
        Raised when the `sport` argument is not of type `str`.

    Examples
    --------
    >>> tournaments = get_major_tournaments('soccer')
    ['FIFA World Cup', 'UEFA Champions League', 'Copa América']

    >>> tournaments = get_major_tournaments('tennis')
    ['Wimbledon', 'French Open', 'US Open', 'Australian Open']

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")