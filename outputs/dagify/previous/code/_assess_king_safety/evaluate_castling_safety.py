def evaluate_castling_safety(castling_rights: str, side_to_move: str) -> float:
    """
    Computes a castling safety bonus from castling rights and the side to move.

    Parameters
    ----------
    castling_rights : str
        A four‑character string representing castling rights in standard
        chess notation (e.g., 'KQkq', 'KQ', 'kq', or '--').
    side_to_move : str
        The side to move, either 'white' or 'black'.

    Returns
    -------
    float
        A non‑negative float bonus; higher values indicate safer castling
        opportunities.

    Raises
    ------
    ValueError
        Raised when `castling_rights` is not a 4‑character string or
        contains invalid characters.
    TypeError
        Raised when either `castling_rights` or `side_to_move` is not of
        type `str`.

    Examples
    --------
    >>> evaluate_castling_safety(castling_rights='KQkq', side_to_move='white')
    1.0

    >>> evaluate_castling_safety(castling_rights='kq', side_to_move='black')
    0.5

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")