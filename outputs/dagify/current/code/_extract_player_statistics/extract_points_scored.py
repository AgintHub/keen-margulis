from typing import List


def extract_points_scored(aggregated_stats: str, player_names: str) -> List[int]:
    """
    Extracts the total points scored by each player from the provided aggregated
    statistics.

    Parameters
    ----------
    aggregated_stats : str
        A string representation of aggregated game statistics, containing
        player performance data.
    player_names : str
        A string representation of the list of player names corresponding to
        the statistics in aggregated_stats.

    Returns
    -------
    List[int]
        A list of integers representing the total points scored by each
        player in the order corresponding to player_names.

    Raises
    ------
    ValueError
        If the aggregated_stats string is not properly formatted or if it
        doesn't contain valid player statistics.
    TypeError
        If aggregated_stats or player_names are not strings, or if the
        parsed statistics do not contain expected data types.

    Examples
    --------
    >>> aggregated_stats = '{\"Player1\": {\"points\": 10}, \"Player2\":
    {\"points\": 20}}'
    >>> player_names = '[\"Player1\", \"Player2\"]'
    >>> extract_points_scored(aggregated_stats=aggregated_stats,
    player_names=player_names)
    [10, 20]

    >>> aggregated_stats = '{\"John\": {\"points\": 15}, \"Doe\": {\"points\":
    25}}'
    >>> player_names = '[\"John\", \"Doe\"]'
    >>> extract_points_scored(aggregated_stats=aggregated_stats,
    player_names=player_names)
    [15, 25]

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")