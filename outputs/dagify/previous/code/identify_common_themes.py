from ._identify_common_themes.validate_lyrics_input import validate_lyrics_input
from ._identify_common_themes.preprocess_lyrics_text import preprocess_lyrics_text
from ._identify_common_themes.extract_theme_keywords import extract_theme_keywords
from ._identify_common_themes.count_theme_occurrences import count_theme_occurrences
from ._identify_common_themes.sort_themes_by_frequency import sort_themes_by_frequency
from ._identify_common_themes.extract_frequencies_for_themes import extract_frequencies_for_themes

from pydantic import BaseModel, Field
from typing import List


class GatherTaylorSwiftDataOutput(BaseModel):
    """Pydantic model for gather_taylor_swift_data node outputs."""
    album_names: List[str] = Field(..., description="List of Taylor Swift's album names")
    release_dates: List[str] = Field(..., description="List of release dates corresponding to the albums")
    song_lyrics: List[str] = Field(..., description="List of song lyrics from Taylor Swift's discography")
    chart_performance: List[int] = Field(..., description="List of chart performance metrics for Taylor Swift's songs")


class IdentifyCommonThemesOutput(BaseModel):
    """Pydantic model for identify_common_themes node outputs."""
    themes: List[str] = Field(..., description="List of common themes found in the lyrics")
    theme_frequencies: List[int] = Field(..., description="Frequency of occurrence for each theme")


def identify_common_themes(gather_taylor_swift_data_input: GatherTaylorSwiftDataOutput, **kwargs) -> IdentifyCommonThemesOutput:
    """
    Identify common themes in Taylor Swift's lyrics by analyzing the collected
    song lyrics.

    Parameters
    ----------
    song_lyrics : List[str]
        List of song lyrics from Taylor Swift's discography, provided by the
        'gather_taylor_swift_data' node.

    Returns
    -------
    {'themes': List[str], 'theme_frequencies': List[int]}
        A dictionary containing a list of common themes and their
        corresponding frequencies.

    Raises
    ------
    ValueError
        If the input 'song_lyrics' is empty or not a list of strings.

    Examples
    --------
    >>> song_lyrics = ['Love is in the air', 'Heartbreak is hard', 'Love is
    sweet']
    >>> themes, theme_frequencies = identify_common_themes(song_lyrics)
    >>> print(themes)
    >>> print(theme_frequencies)
    ['love', 'heartbreak']
    [2, 1]

    """
    song_lyrics = gather_taylor_swift_data_input.song_lyrics
    
    validated_lyrics: List[str] = validate_lyrics_input(lyrics=song_lyrics)
    preprocessed_lyrics: List[str] = preprocess_lyrics_text(lyrics=validated_lyrics)
    theme_keywords: List[str] = extract_theme_keywords(lyrics=preprocessed_lyrics)
    theme_counts: dict = count_theme_occurrences(keywords=theme_keywords, lyrics=preprocessed_lyrics)
    sorted_themes: List[str] = sort_themes_by_frequency(theme_counts=theme_counts)
    frequencies: List[int] = extract_frequencies_for_themes(themes=sorted_themes, theme_counts=theme_counts)
    
    return IdentifyCommonThemesOutput(
        themes=sorted_themes,
        theme_frequencies=frequencies
    )