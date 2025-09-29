def parse_en_passant_square(en_passant_section: str) -> str:
    """
    Parse the en passant field of a FEN string and return the square or '-' if
    none.

    Parameters
    ----------
    en_passant_section : str
        The en passant section of a FEN string (fourth component). Expected
        to be either a two-character square notation like "e3" or a single
        hyphen '-' indicating no en passant square.

    Returns
    -------
    str
        The square notation of the en passant square, or '-' if no en
        passant move exists.

    Raises
    ------
    TypeError
        Raised if en_passant_section is not a string.
    ValueError
        Raised if en_passant_section is not a valid two-character square or
        '-'.

    Examples
    --------
    >>> parse_en_passant_square('e3')
    'e3'

    >>> parse_en_passant_square('-')
    '-'

    >>> parse_en_passant_square('z9')
    Traceback (most recent call last):
      ...
    ValueError: Invalid en passant square: z9

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")