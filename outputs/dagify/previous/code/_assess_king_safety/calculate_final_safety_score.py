def calculate_final_safety_score(castling_bonus: str, pawn_shield: str, threat_proximity: str, en_passant_threat: str) -> float:
    """
    Compute the final king safety score from individual safety component scores.

    Parameters
    ----------
    castling_bonus : float
        Bonus score for having castled. Non‑negative floating‑point value.
    pawn_shield : float
        Score reflecting the strength of the pawn shield around the king.
        Non‑negative floating‑point value.
    threat_proximity : float
        Score that increases with proximity of enemy pieces to the king.
        Non‑negative floating‑point value.
    en_passant_threat : float
        Score indicating threat from a potential en passant capture.
        Non‑negative floating‑point value.

    Returns
    -------
    float
        The weighted sum of the input scores, representing overall king
        safety.

    Raises
    ------
    TypeError
        If any argument is not of type float.
    ValueError
        If any argument is negative.

    Examples
    --------
    >>> calculate_final_safety_score(1.5, 2.0, 0.8, 0.3)
    4.6

    >>> calculate_final_safety_score(0.0, 1.2, 0.5, 0.0)
    1.7

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")