# fetch_song_data PRD

## Description
Collect basic metadata and lyrics for all Taylor Swift songs.


## Conceptual Info

Collect basic metadata and lyrics for all Taylor Swift songs.

## Docstring

### Summary
Fetches a list of all Taylor Swift songs along with their full lyrics and release years from a public API.

### Parameters

- **artist** (str): Name of the artist to query. Defaults to "Taylor Swift".

### Returns

dict: Dictionary containing three keys: `song_titles` (List[str]), `song_lyrics` (List[str]), and `release_years` (List[int]). The lists are aligned by index.

### Raises

- ValueError: If the API request fails or returns an unexpected status code.
- KeyError: If the API response is missing required fields (e.g., title, lyrics, or year).

### Examples

```python
>>> result = fetch_song_data()
>>> print(result['song_titles'][0])
"Love Story"
```

```python
>>> result = fetch_song_data(artist="Taylor Swift")
>>> print(len(result['song_titles']))
"<total number of Taylor Swift songs>"
```
