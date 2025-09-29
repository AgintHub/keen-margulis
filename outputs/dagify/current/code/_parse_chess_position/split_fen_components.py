from typing import List


def split_fen_components(fen: str) -> List[str]:
    """
    Splits a FEN string into its six components.

    Parameters
    ----------
    fen : str
        A validated FEN string containing exactly six fields separated by
        spaces.

    Returns
    -------
    LIST_STR
        A list of six strings representing the FEN components in the order:
        board, active color, castling rights, en passant target, half‑move
        clock, and full‑move number.

    Raises
    ------
    TypeError
        If the input is not a string.
    ValueError
        If the input string does not contain exactly six space‑separated
        parts.

    Examples
    --------
    >>> split_fen_components('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq
    - 0 1')
    ["rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR", "w", "KQkq", "-", "0", "1"]

    >>> split_fen_components('8/8/8/8/8/8/8/8 w - - 0 1')
    ["8/8/8/8/8/8/8/8", "w", "-", "-", "0", "1"]

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")