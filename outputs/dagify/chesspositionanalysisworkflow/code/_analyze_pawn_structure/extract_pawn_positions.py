from typing import List


def extract_pawn_positions(piece_positions: str, side: str) -> List[str]:
    """
    Extracts the positions of all pawns for a specified side from a list of all
    piece positions.

    Parameters
    ----------
    piece_positions : List[str]
        A list of strings representing all piece positions on the board
        (e.g., ['e4', 'd5', 'c3']). Each string follows standard algebraic
        notation without piece type identifiers.
    side : str
        The side whose pawn positions should be returned; expected values
        are 'white' or 'black'.

    Returns
    -------
    List[str]
        A list of position strings corresponding to the pawns belonging to
        the specified side.

    Raises
    ------
    ValueError
        Raised when `side` is not 'white' or 'black', or when
        `piece_positions` contains an invalid board coordinate.
    TypeError
        Raised when `piece_positions` is not a list of strings or when
        `side` is not a string.

    Examples
    --------
    >>> extract_pawn_positions(['a2', 'b2', 'c3', 'd5', 'e4'], 'white')
    ['a2', 'b2']

    >>> extract_pawn_positions(['a7', 'b6', 'c5', 'd4', 'e3'], 'black')
    ['a7', 'b6', 'c5']

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")