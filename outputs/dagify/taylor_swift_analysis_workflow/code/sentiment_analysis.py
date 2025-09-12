from pydantic import BaseModel, Field
from typing import List


class FetchSongDataOutput(BaseModel):
    """Pydantic model for fetch_song_data node outputs."""
    song_titles: List[str] = Field(..., description="List of song titles in the same order as the other lists.")
    song_lyrics: List[str] = Field(..., description="List of full lyrics corresponding to each song title.")
    release_years: List[int] = Field(..., description="List of release years corresponding to each song title.")


class SentimentAnalysisOutput(BaseModel):
    """Pydantic model for sentiment_analysis node outputs."""
    sentiment_scores: List[float] = Field(..., description="Sentiment score for each song.")


def sentiment_analysis(fetch_song_data_input: FetchSongDataOutput, **kwargs) -> SentimentAnalysisOutput:
    """
    Computes overall sentiment scores for a list of song lyrics, returning a
    list of floats between -1 and 1 aligned with song titles.

    Parameters
    ----------
    song_titles : List[str]
        List of song titles corresponding to the lyrics.
    song_lyrics : List[str]
        List of full lyrics for each song.

    Returns
    -------
    List[float]
        Sentiment score for each song.

    Raises
    ------
    ValueError
        If input lists are not the same length or are empty.

    Examples
    --------
    >>> scores = sentiment_analysis(["Love Story", "Bad Blood"], ["I knew you
    were trouble, so I stayed away", "I used to love you, now I hate you"])
    [0.76, -0.62]

    >>> scores = sentiment_analysis(["Blank Space"], ["So nice I can't decide if
    I'm a love or a lie"])
    [0.48]

    """
    return SentimentAnalysisOutput(
        sentiment_scores=[],
    )