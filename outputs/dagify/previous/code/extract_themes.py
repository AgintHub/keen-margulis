from pydantic import BaseModel, Field
from typing import List


class AnalyzeLyricsOutput(BaseModel):
    """Pydantic model for analyze_lyrics node outputs."""
    unique_words: List[str] = Field(..., description="All distinct words found in the lyrics, ordered by descending frequency.")
    word_counts: List[int] = Field(..., description="Number of occurrences for each word, aligned with unique_words.")


class ExtractThemesOutput(BaseModel):
    """Pydantic model for extract_themes node outputs."""
    themes: List[str] = Field(..., description="Top 5 thematic words in descending order of frequency.")
    theme_scores: List[float] = Field(..., description="Normalized frequency score for each theme (count / total word count).")


def extract_themes(analyze_lyrics_input: AnalyzeLyricsOutput, **kwargs) -> ExtractThemesOutput:
    """
    Selects the top five words by occurrence from lyric word statistics and
    returns them with their normalized frequency scores.

    Parameters
    ----------
    unique_words : List[str]
        List of unique words sorted by descending frequency.
    word_counts : List[int]
        Parallel list of counts corresponding to each word in
        `unique_words`.

    Returns
    -------
    Tuple[List[str], List[float]]
        A tuple containing the top 5 thematic words and a list of their
        normalized scores.

    Raises
    ------
    ValueError
        If `unique_words` and `word_counts` are empty or have mismatched
        lengths.
    ValueError
        If the total word count is zero (cannot compute normalized scores).

    Examples
    --------
    >>> unique_words = ['love', 'heart', 'night', 'dream', 'sky']
    >>> word_counts = [10, 8, 5, 2, 1]
    >>> themes, scores = extract_themes(unique_words, word_counts)
    >>> print(themes)
    >>> print(scores)
    ['love', 'heart', 'night', 'dream', 'sky']\n[0.38461538461538464,
    0.3076923076923077, 0.19230769230769232, 0.07692307692307693,
    0.038461538461538464]

    >>> unique_words = ['sun', 'rain']
    >>> word_counts = [10, 5]
    >>> themes, scores = extract_themes(unique_words, word_counts)
    >>> print(themes)
    >>> print(scores)
    ['sun', 'rain']\n[0.6666666666666666, 0.3333333333333333]

    """
    return ExtractThemesOutput(
        themes=[],
        theme_scores=[],
    )