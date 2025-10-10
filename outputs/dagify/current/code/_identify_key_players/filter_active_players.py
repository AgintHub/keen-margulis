from typing import List


def filter_active_players(players_data: str) -> List[str]:
    """
    Return a filtered list of active players from given player data.

    Parameters
    ----------
    players_data : str
        A JSON-formatted string representing a list of player dictionaries.
        Each dictionary must contain at least a 'status' key with values
        such as 'active', 'retired', 'injured', etc.

    Returns
    -------
    str
        A JSON string representing a list of dictionaries, each describing
        an active player. The returned value is compatible with JSON parsing
        into a Python list of dicts.

    Raises
    ------
    ValueError
        Raised if the input string cannot be parsed as JSON or if the parsed
        object is not a list.
    TypeError
        Raised if `players_data` is not of type `str`.

    Examples
    --------
    >>> sample_input = '[{"name": "Alice", "status": "active"}, {"name": "Bob",
    "status": "retired"}]'
    >>> result = filter_active_players(sample_input)
    >>> print(result)
    "[{'name': 'Alice', 'status': 'active'}]"

    >>> invalid_input = '{"name": "Charlie", "status": "active"}'
    >>> try:
    ...     filter_active_players(invalid_input)
    >>> except ValueError as e:
    ...     print(e)
    "Input must be a JSON list of player dictionaries."

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")