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
    return IdentifyCommonThemesOutput(
        themes=[],
        theme_frequencies=[],
    )