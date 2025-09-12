from ._gather_taylor_swift_data.fetch_discography_metadata import fetch_discography_metadata
from ._gather_taylor_swift_data.extract_album_names import extract_album_names
from ._gather_taylor_swift_data.extract_release_dates import extract_release_dates
from ._gather_taylor_swift_data.get_song_titles_from_albums import get_song_titles_from_albums
from ._gather_taylor_swift_data.fetch_lyrics_batch import fetch_lyrics_batch
from ._gather_taylor_swift_data.fetch_chart_performance_data import fetch_chart_performance_data
from ._gather_taylor_swift_data.extract_chart_positions import extract_chart_positions
from ._gather_taylor_swift_data.validate_data_completeness import validate_data_completeness

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
    discography_data: dict = fetch_discography_metadata(artist="Taylor Swift")
    album_names: List[str] = extract_album_names(discography_data=discography_data)
    release_dates: List[str] = extract_release_dates(discography_data=discography_data)
    
    song_list: List[str] = get_song_titles_from_albums(albums=album_names)
    song_lyrics: List[str] = fetch_lyrics_batch(song_titles=song_list, artist="Taylor Swift")
    
    chart_data: dict = fetch_chart_performance_data(artist="Taylor Swift", songs=song_list)
    chart_performance: List[int] = extract_chart_positions(chart_data=chart_data)
    
    validate_data_completeness(albums=album_names, dates=release_dates, lyrics=song_lyrics, charts=chart_performance)
    
    return GatherTaylorSwiftDataOutput(
        album_names=album_names,
        release_dates=release_dates,
        song_lyrics=song_lyrics,
        chart_performance=chart_performance
    )