from pydantic import BaseModel, Field
from typing import List


class GatherTaylorSwiftDataOutput(BaseModel):
    """Pydantic model for gather_taylor_swift_data node outputs."""
    album_names: List[str] = Field(..., description="List of Taylor Swift's album names")
    release_dates: List[str] = Field(..., description="List of release dates corresponding to the albums")
    song_lyrics: List[str] = Field(..., description="List of song lyrics from Taylor Swift's discography")
    chart_performance: List[int] = Field(..., description="List of chart performance metrics for Taylor Swift's songs")


def gather_taylor_swift_data(general_input: str, **kwargs) -> GatherTaylorSwiftDataOutput:
    """
    Gathers data on Taylor Swift's discography, lyrics, and chart performance.

    Returns
    -------
    dict
        A dictionary containing lists of album names, release dates, song
        lyrics, and chart performance metrics.

    Raises
    ------
    DataCollectionError
        If there's an issue collecting data from the sources.
    DataFormatError
        If the collected data is not in the expected format.

    Examples
    --------
    >>> data = gather_taylor_swift_data()
    >>> print(data['album_names'])
    >>> print(data['release_dates'])
    >>> print(data['song_lyrics'])
    >>> print(data['chart_performance'])
    ['Taylor Swift', 'Fearless', ...]
    ['2006-10-24', '2008-11-11', ...]
    [' lyrics1 ', ' lyrics2 ', ...]
    [10, 20, ...]

    """
    return GatherTaylorSwiftDataOutput(
        album_names=[],
        release_dates=[],
        song_lyrics=[],
        chart_performance=[],
    )