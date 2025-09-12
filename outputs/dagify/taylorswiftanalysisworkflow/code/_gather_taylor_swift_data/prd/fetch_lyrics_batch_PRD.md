# fetch_lyrics_batch PRD

## Description
Fetches lyrics for a batch of songs by a specified artist, returning a list of lyric strings.


## Conceptual Info

Provides a batched lyrics retrieval service that abstracts the complexity of querying external lyric databases or APIs.

## Docstring

### Summary
Shim function to retrieve lyrics for multiple songs by a given artist.

### Parameters

- **song_titles** (List[str]): A list of song titles whose lyrics need to be fetched.
- **artist** (str): The name of the artist associated with the song titles.

### Returns

List[str]: A list containing the lyrics for each requested song title, in the same order as the input list.

### Raises

- Exception: Raised if the lyrics cannot be fetched due to network issues, API rate limiting, or missing data for a requested title.

### Examples

```python
>>> song_list = ["Love Story", "Blank Space", "Shake It Off"]
>>> artist = "Taylor Swift"
>>> lyrics = fetch_lyrics_batch(song_titles=song_list, artist=artist)
>>> print(lyrics[0])
"We were both young when I first saw you..."
```
