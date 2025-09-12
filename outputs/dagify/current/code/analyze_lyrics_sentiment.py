from pydantic import BaseModel, Field
from typing import List


class GatherTaylorSwiftDataOutput(BaseModel):
    """Pydantic model for gather_taylor_swift_data node outputs."""
    album_names: List[str] = Field(..., description="List of Taylor Swift's album names")
    release_dates: List[str] = Field(..., description="List of release dates corresponding to the albums")
    song_lyrics: List[str] = Field(..., description="List of song lyrics from Taylor Swift's discography")
    chart_performance: List[int] = Field(..., description="List of chart performance metrics for Taylor Swift's songs")


class AnalyzeLyricsSentimentOutput(BaseModel):
    """Pydantic model for analyze_lyrics_sentiment node outputs."""
    sentiment_scores: List[float] = Field(..., description="List of sentiment scores for each song")
    average_sentiment: float = Field(..., description="Average sentiment score across all songs")


def analyze_lyrics_sentiment(gather_taylor_swift_data_input: GatherTaylorSwiftDataOutput, **kwargs) -> AnalyzeLyricsSentimentOutput:
    """
    Analyzes the sentiment of Taylor Swift's song lyrics.

    Parameters
    ----------
    song_lyrics : List[str]
        List of song lyrics from Taylor Swift's discography, obtained from
        the 'gather_taylor_swift_data' node.

    Returns
    -------
    {'sentiment_scores': List[float], 'average_sentiment': float}
        A dictionary containing a list of sentiment scores for each song and
        the average sentiment score across all songs.

    Raises
    ------
    ValueError
        If the input 'song_lyrics' is empty or not a list of strings.

    Examples
    --------
    >>> song_lyrics = ['I stay out too late, got nothing in my brain', 'I think
    I got a broken heart']
    >>> result = analyze_lyrics_sentiment(song_lyrics)
    >>> print(result)
    {'sentiment_scores': [0.2, -0.5], 'average_sentiment': -0.15}

    >>> song_lyrics = ['You took the time to memorize me, my fears, my hopes,
    and dreams']
    >>> result = analyze_lyrics_sentiment(song_lyrics)
    >>> print(result)
    {'sentiment_scores': [0.8], 'average_sentiment': 0.8}

    """
    return AnalyzeLyricsSentimentOutput(
        sentiment_scores=[],
        average_sentiment=0.0,
    )