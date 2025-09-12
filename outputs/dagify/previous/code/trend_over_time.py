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


class TrendOverTimeOutput(BaseModel):
    """Pydantic model for trend_over_time node outputs."""
    years: List[int] = Field(..., description="Chronological list of years with songs.")
    avg_sentiment: List[float] = Field(..., description="Average sentiment for each year.")


def trend_over_time(fetch_song_data_input: FetchSongDataOutput, sentiment_analysis_input: SentimentAnalysisOutput, **kwargs) -> TrendOverTimeOutput:
    """
    Compute average sentiment per release year from parallel lists of years and
    sentiment scores.

    Parameters
    ----------
    release_years : List[int]
        List of release years for each song, aligned with sentiment_scores.
    sentiment_scores : List[float]
        Sentiment score for each song, ranging from -1 (very negative) to 1
        (very positive).

    Returns
    -------
    Tuple[List[int], List[float]]
        A tuple containing two parallel lists: - years: Chronological list
        of years with songs. - avg_sentiment: Average sentiment for each
        corresponding year.

    Raises
    ------
    ValueError
        If release_years and sentiment_scores are of different lengths.
    ValueError
        If either input list is empty.

    Examples
    --------
    >>> years, avg = trend_over_time([2015, 2015, 2016], [0.2, 0.5, -0.1])
    ([2015, 2016], [0.35, -0.1])

    >>> trend_over_time([2015, 2016], [0.3])
    Traceback (most recent call last):
      ...
    ValueError: release_years and sentiment_scores must have the same length.

    """
    return TrendOverTimeOutput(
        years=[],
        avg_sentiment=[],
    )