from typing import List


def preprocess_lyrics_text(lyrics: str) -> List[str]:
    """
    Preprocess a list of song lyrics for sentiment analysis.

    Parameters
    ----------
    lyrics : LIST_STR
        A list of raw lyric strings.

    Returns
    -------
    LIST_STR
        A list of cleaned lyric strings.

    Raises
    ------
    ValueError
        If `lyrics` is not a list of strings.

    Examples
    --------
    >>> cleaned = preprocess_lyrics_text(lyrics=["Hey!  ", "Good morning."])
    >>> print(cleaned)
    ['hey', 'good morning']

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")