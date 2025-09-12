from pydantic import BaseModel, Field
from typing import List


class FetchSongDataOutput(BaseModel):
    """Pydantic model for fetch_song_data node outputs."""
    song_titles: List[str] = Field(..., description="List of song titles in the same order as the other lists.")
    song_lyrics: List[str] = Field(..., description="List of full lyrics corresponding to each song title.")
    release_years: List[int] = Field(..., description="List of release years corresponding to each song title.")


def fetch_song_data(general_input: str, **kwargs) -> FetchSongDataOutput:
    """
    Fetches a list of all Taylor Swift songs along with their full lyrics and
    release years from a public API.

    Parameters
    ----------
    artist : str
        Name of the artist to query. Defaults to "Taylor Swift".

    Returns
    -------
    dict
        Dictionary containing three keys: `song_titles` (List[str]),
        `song_lyrics` (List[str]), and `release_years` (List[int]). The
        lists are aligned by index.

    Raises
    ------
    ValueError
        If the API request fails or returns an unexpected status code.
    KeyError
        If the API response is missing required fields (e.g., title, lyrics,
        or year).

    Examples
    --------
    >>> result = fetch_song_data()
    >>> print(result['song_titles'][0])
    "Love Story"

    >>> result = fetch_song_data(artist="Taylor Swift")
    >>> print(len(result['song_titles']))
    "<total number of Taylor Swift songs>"

    """
    return FetchSongDataOutput(
        song_titles=[],
        song_lyrics=[],
        release_years=[],
    )