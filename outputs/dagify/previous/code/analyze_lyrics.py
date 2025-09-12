from pydantic import BaseModel, Field
from typing import List


class FetchSongDataOutput(BaseModel):
    """Pydantic model for fetch_song_data node outputs."""
    song_titles: List[str] = Field(..., description="List of song titles in the same order as the other lists.")
    song_lyrics: List[str] = Field(..., description="List of full lyrics corresponding to each song title.")
    release_years: List[int] = Field(..., description="List of release years corresponding to each song title.")


class AnalyzeLyricsOutput(BaseModel):
    """Pydantic model for analyze_lyrics node outputs."""
    unique_words: List[str] = Field(..., description="All distinct words found in the lyrics, ordered by descending frequency.")
    word_counts: List[int] = Field(..., description="Number of occurrences for each word, aligned with unique_words.")


def analyze_lyrics(fetch_song_data_input: FetchSongDataOutput, **kwargs) -> AnalyzeLyricsOutput:
    """
    Computes the frequency of every unique word across all song lyrics and
    returns the words sorted by decreasing count.

    Parameters
    ----------
    song_titles : List[str]
        Parallel list of song titles; provided for context but not used in
        frequency computation.
    song_lyrics : List[str]
        Parallel list of full lyrics corresponding to each song title.

    Returns
    -------
    Tuple[List[str], List[int]]
        A tuple containing the list of unique words sorted by descending
        frequency and a parallel list of their counts.

    Raises
    ------
    ValueError
        Raised if `song_lyrics` is empty or all entries are blank.
    TypeError
        Raised if inputs are not lists of strings.

    Examples
    --------
    >>> song_titles = ['A', 'B']
    >>> song_lyrics = ['Hello world hello', 'World of code']
    >>> unique, counts = analyze_lyrics(song_titles, song_lyrics)
    >>> print(unique)
    >>> print(counts)
    ['hello', 'world', 'of', 'code']
    [3, 2, 1, 1]

    >>> song_titles = ['Song']
    >>> song_lyrics = ['I love coding', 'I love coding', 'Coding is fun']
    >>> unique, counts = analyze_lyrics(song_titles, song_lyrics)
    >>> print(dict(zip(unique, counts)))
    {'i': 3, 'love': 2, 'coding': 3, 'is': 1, 'fun': 1}

    """
    return AnalyzeLyricsOutput(
        unique_words=[],
        word_counts=[],
    )