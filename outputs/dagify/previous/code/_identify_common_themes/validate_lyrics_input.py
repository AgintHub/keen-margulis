from typing import List


def validate_lyrics_input(lyrics: str) -> List[str]:
    """
    Validate and clean raw song lyrics.

    Parameters
    ----------
    lyrics : str
        Raw lyric string that may contain newlines, extraneous whitespace,
        or non‑ASCII characters.

    Returns
    -------
    List[str]
        A list of cleaned lyric lines ready for downstream processing.

    Raises
    ------
    ValueError
        Raised when the input string is empty or contains only whitespace.

    Examples
    --------
    >>> lyrics = "  Verse one\n\n Chorus   "
    >>> cleaned = validate_lyrics_input(lyrics)
    ['Verse one', 'Chorus']

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")