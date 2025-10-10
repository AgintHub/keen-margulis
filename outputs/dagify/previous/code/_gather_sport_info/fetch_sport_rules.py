from typing import List


def fetch_sport_rules(sport: str) -> List[str]:
    """
    Retrieve a list of key rules for the specified sport.

    Parameters
    ----------
    sport : str
        Name of the sport for which rules are requested (e.g., 'soccer',
        'basketball').

    Returns
    -------
    list[str]
        A list of strings, each describing a key rule that governs the
        specified sport.

    Raises
    ------
    ValueError
        If the sport name is not recognized or not supported.
    TypeError
        If the `sport` argument is not of type `str`.

    Examples
    --------
    >>> rules = fetch_sport_rules('basketball')
    ['3‑point line distance: 23.75 ft', 'Maximum team size: 5 players', 'Shot
    clock: 24 seconds']

    >>> fetch_sport_rules('unknown_sport')
    ValueError: Unsupported sport name: unknown_sport

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")