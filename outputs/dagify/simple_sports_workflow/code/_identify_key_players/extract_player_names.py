from typing import List


def extract_player_names(player_data: str) -> List[str]:
    """
    Extracts the 'name' field from each dictionary in a list of player data and
    returns a list of names.

    Parameters
    ----------
    player_data : List[dict]
        A list where each element is a dictionary representing a player,
        containing at least a 'name' key.

    Returns
    -------
    List[str]
        A list of player names extracted from the input data.

    Raises
    ------
    ValueError
        Raised if any dictionary in `player_data` lacks a 'name' key.
    TypeError
        Raised if `player_data` is not a list.

    Examples
    --------
    >>> players = [{'name': 'LeBron James', 'team': 'Lakers'}, {'name': 'Kevin
    Durant', 'team': 'Nets'}]
    >>> extract_player_names(players)
    ['LeBron James', 'Kevin Durant']

    >>> players = [{'name': 'Stephen Curry'}, {'name': 'James Harden', 'team':
    'Nets'}]
    >>> extract_player_names(players)
    ['Stephen Curry', 'James Harden']

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")