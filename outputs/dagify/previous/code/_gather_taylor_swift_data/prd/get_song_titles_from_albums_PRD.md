# get_song_titles_from_albums PRD

## Description
Retrieves all song titles for the provided list of Taylor Swift album names.


## Conceptual Info

This shim encapsulates the logic needed to fetch song titles from a list of album names, delegating the heavy lifting to a reliable music metadata service. It isolates network calls, parsing, and error handling, enabling the rest of the pipeline to treat the operation as a pure function that returns a simple list of strings.

## Docstring

### Summary
Retrieve a list of song titles for the given Taylor Swift album names.

### Parameters

- **albums** (str): A comma-separated string containing the names of the albums to query.

### Returns

list[str]: A list of all song titles found in the specified albums.

### Raises

- ValueError: Raised when the `albums` string is empty or contains only whitespace.
- RuntimeError: Raised when the external metadata service fails or returns incomplete data.

### Examples

```python
>>> song_titles = get_song_titles_from_albums(albums='Red, 1989, Lover')
>>> print(song_titles)
['State of Grace', 'Red', 'I Knew You Were Trouble', ..., 'Lover', ...]
```
