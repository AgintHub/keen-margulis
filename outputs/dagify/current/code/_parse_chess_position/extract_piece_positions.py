from typing import List


def extract_piece_positions(board_section: str) -> List[str]:
    """
    Extract a list of piece positions from a FEN board section string.

    Parameters
    ----------
    board_section : str
        The board section of a FEN string (e.g.,
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR").

    Returns
    -------
    list[str]
        A list of strings, each formatted as "<square> <piece>", enumerating
        all pieces on the board from a8 to h1.

    Raises
    ------
    TypeError
        If board_section is not a string.
    ValueError
        If board_section does not contain exactly 8 ranks separated by
        slashes or contains invalid characters.

    Examples
    --------
    >>> extract_piece_positions('8/8/8/8/8/8/8/8')
    []

    >>> extract_piece_positions('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
    ["a8 r", "b8 n", "c8 b", "d8 q", "e8 k", "f8 b", "g8 n", "h8 r", "a7 p", "b7
    p", "c7 p", "d7 p", "e7 p", "f7 p", "g7 p", "h7 p", "a2 P", "b2 P", "c2 P",
    "d2 P", "e2 P", "f2 P", "g2 P", "h2 P", "a1 R", "b1 N", "c1 B", "d1 Q", "e1
    K", "f1 B", "g1 N", "h1 R"]

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")