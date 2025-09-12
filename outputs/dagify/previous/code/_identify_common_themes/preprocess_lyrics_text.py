from typing import List


def preprocess_lyrics_text(lyrics: str) -> List[str]:
    """
    Preprocesses raw song lyrics.

    Parameters
    ----------
    lyrics : List[str]
        A list of raw lyric strings to be cleaned.

    Returns
    -------
    List[str]
        List of cleaned, tokenized lyric strings.

    Raises
    ------
    ValueError
        Raised when the input list is empty or contains non-string elements.

    Examples
    --------
    >>> lyrics = ['Hello! This is a test.', 'Another line: with punctuation.']
    >>> preprocessed = preprocess_lyrics_text(lyrics=lyrics)
    >>> print(preprocessed)
    ['hello this is a test', 'another line with punctuation']

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")