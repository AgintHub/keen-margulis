def create_top_performers_summary(scorers: str, rebounders: str, assisters: str) -> str:
    """
    Creates a formatted summary of top performers from the provided lists of
    scorers, rebounders, and assisters.

    Parameters
    ----------
    scorers : List[str]
        List of top scorers in the team.
    rebounders : List[str]
        List of top rebounders in the team.
    assisters : List[str]
        List of top assisters in the team.

    Returns
    -------
    str
        A formatted summary including the names and roles of top performers.

    Raises
    ------
    TypeError
        If any of the input parameters are not lists of strings.
    ValueError
        If any of the input lists are empty.

    Examples
    --------
    >>> create_top_performers_summary(scorers=['Player1', 'Player2'],
    rebounders=['Player3', 'Player4'], assisters=['Player5', 'Player6'])
    'Top scorers: Player1, Player2. Top rebounders: Player3, Player4. Top
    assisters: Player5, Player6.'

    >>> create_top_performers_summary(scorers=['John', 'Doe'],
    rebounders=['Jane', 'Doe'], assisters=['Bob', 'Smith'])
    'Top scorers: John, Doe. Top rebounders: Jane, Doe. Top assisters: Bob,
    Smith.'

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")