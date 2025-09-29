from typing import List


def count_pieces_by_type(pieces: str) -> List[int]:
    """
    Counts chess pieces by type.

    Parameters
    ----------
    pieces : List[str]
        A list of piece symbols (e.g., 'K', 'Q', 'R', 'B', 'N', 'P')
        representing the pieces of one side.

    Returns
    -------
    List[int]
        A list of six integers: [king_count, queen_count, rook_count,
        bishop_count, knight_count, pawn_count].

    Raises
    ------
    TypeError
        Raised if `pieces` is not a list.
    ValueError
        Raised if any element in `pieces` is not a valid chess piece symbol.

    Examples
    --------
    >>> count_pieces_by_type(['K', 'P', 'P', 'Q', 'R', 'B', 'N', 'P'])
    [1, 1, 1, 1, 1, 3]

    >>> count_pieces_by_type([])
    [0, 0, 0, 0, 0, 0]

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")