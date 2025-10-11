def format_win_loss_record(wins: str, losses: str) -> str:
    """
    Formats the win and loss counts into a string representation.

    Parameters
    ----------
    wins : str
        The number of wins as a string.
    losses : str
        The number of losses as a string.

    Returns
    -------
    str
        The formatted win/loss record (e.g., '20-10').

    Raises
    ------
    ValueError
        If either wins or losses cannot be converted to a non-negative
        integer.
    TypeError
        If wins or losses are not strings.

    Examples
    --------
    >>> format_win_loss_record(wins='20', losses='10')
    '20-10'

    >>> format_win_loss_record(wins='0', losses='5')
    '0-5'

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")