from typing import List


def extract_black_pieces(piece_positions: str) -> List[str]:
    """
    Extracts the positions of all black pieces from the given list of chess
    piece positions.

    Parameters
    ----------
    piece_positions : List[str]
        A list of chess piece position strings, e.g., ['e4', 'B5', 'c6',
        'D1'].

    Returns
    -------
    List[str]
        A list containing only the positions of black pieces.

    Raises
    ------
    TypeError
        Raised when `piece_positions` is not a list or contains non-string
        elements.
    ValueError
        Raised when any element in `piece_positions` is an empty string or
        does not conform to expected format.

    Examples
    --------
    >>> extract_black_pieces(['e4', 'B5', 'c6', 'D1'])
    ['e4', 'c6']

    >>> extract_black_pieces([])
    []

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")