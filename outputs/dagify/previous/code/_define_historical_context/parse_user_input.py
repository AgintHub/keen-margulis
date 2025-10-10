def parse_user_input(input_text: str) -> str:
    """
    Clean and normalize a raw user input string.

    Parameters
    ----------
    input_text : str
        Raw user input text to be parsed and cleaned.

    Returns
    -------
    str
        Normalized user input string ready for downstream processing.

    Raises
    ------
    ValueError
        Raised when the cleaned input string is empty.
    TypeError
        Raised when input_text is not of type str.

    Examples
    --------
    >>> parse_user_input('  Hello, World!  ')
    'hello world'

    >>> parse_user_input('  2021-05-10  ')
    '2021-05-10'

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")