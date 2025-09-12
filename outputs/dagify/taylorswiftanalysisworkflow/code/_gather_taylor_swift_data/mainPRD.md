# _gather_taylor_swift_data - Complete PRD Documentation

## Overview
PRDs for nodes in the '_gather_taylor_swift_data' module.

## Table of Contents

- [fetch_discography_metadata](#fetch_discography_metadata)

- [extract_album_names](#extract_album_names)

- [extract_release_dates](#extract_release_dates)

- [get_song_titles_from_albums](#get_song_titles_from_albums)

- [fetch_lyrics_batch](#fetch_lyrics_batch)

- [fetch_chart_performance_data](#fetch_chart_performance_data)

- [extract_chart_positions](#extract_chart_positions)

- [validate_data_completeness](#validate_data_completeness)



---

## fetch_discography_metadata

### Description
Retrieves a JSON dictionary of discography metadata for the specified artist from an external API or database.

### Conceptual Info

Shim to abstract external data fetching

### Docstring

**Summary:** Fetches discography metadata for a given artist.

**Parameters:**

- artist (str): Name of the artist to fetch metadata for.
**Returns:** str - JSON string representation of discography metadata.

**Raises:**

- ValueError: Raised if artist name is empty or None.
- RuntimeError: Raised if external API fails.
**Examples:**

```python
>>> metadata = fetch_discography_metadata(artist='Taylor Swift')
{'albums': [...], 'release_dates': [...], ...}
```



---

## extract_album_names

### Description
Extracts a list of album names from the JSON-formatted discography data.

### Conceptual Info

This shim parses raw discography metadata and extracts the album titles to support downstream data gathering steps.

### Docstring

**Summary:** Extract album names from a discography JSON string.

**Parameters:**

- discography_data (str): JSON-formatted string containing the discography data.
**Returns:** List[str] - A list of album names in the order they appear in the input.

**Raises:**

- ValueError: Raised when the input is not valid JSON or the expected 'albums' key is missing.
**Examples:**

```python
>>> discography_data_json = '{"albums": ["Fearless", "1989", "Red"]}'
>>> album_names = extract_album_names(discography_data_json)
>>> print(album_names)
['Fearless', '1989', 'Red']
```



---

## extract_release_dates

### Description
Extracts a list of release dates for each album from the provided discography metadata.

### Conceptual Info

This shim parses discography metadata to produce a chronological list of album release dates.

### Docstring

**Summary:** Extracts release dates for each album from the provided discography metadata JSON.

**Parameters:**

- discography_data (str): JSON string representing the discography metadata containing album names and release dates.
**Returns:** List[str] - A list of album release dates extracted from the input data.

**Raises:**

- ValueError: Raised when the input JSON is invalid or missing required fields.
**Examples:**

```python
>>> import json
>>> # Sample discography data
>>> sample_json = json.dumps({
...     "albums": [
...         {"name": "Album1", "release_date": "2020-01-01"},
...         {"name": "Album2", "release_date": "2021-01-01"}
...     ]
>>> })
>>> release_dates = extract_release_dates(sample_json)
>>> print(release_dates)
["2020-01-01", "2021-01-01"]
```



---

## get_song_titles_from_albums

### Description
Retrieves all song titles for the provided list of Taylor Swift album names.

### Conceptual Info

This shim encapsulates the logic needed to fetch song titles from a list of album names, delegating the heavy lifting to a reliable music metadata service. It isolates network calls, parsing, and error handling, enabling the rest of the pipeline to treat the operation as a pure function that returns a simple list of strings.

### Docstring

**Summary:** Retrieve a list of song titles for the given Taylor Swift album names.

**Parameters:**

- albums (str): A comma-separated string containing the names of the albums to query.
**Returns:** list[str] - A list of all song titles found in the specified albums.

**Raises:**

- ValueError: Raised when the `albums` string is empty or contains only whitespace.
- RuntimeError: Raised when the external metadata service fails or returns incomplete data.
**Examples:**

```python
>>> song_titles = get_song_titles_from_albums(albums='Red, 1989, Lover')
>>> print(song_titles)
['State of Grace', 'Red', 'I Knew You Were Trouble', ..., 'Lover', ...]
```



---

## fetch_lyrics_batch

### Description
Fetches lyrics for a batch of songs by a specified artist, returning a list of lyric strings.

### Conceptual Info

Provides a batched lyrics retrieval service that abstracts the complexity of querying external lyric databases or APIs.

### Docstring

**Summary:** Shim function to retrieve lyrics for multiple songs by a given artist.

**Parameters:**

- song_titles (List[str]): A list of song titles whose lyrics need to be fetched.
- artist (str): The name of the artist associated with the song titles.
**Returns:** List[str] - A list containing the lyrics for each requested song title, in the same order as the input list.

**Raises:**

- Exception: Raised if the lyrics cannot be fetched due to network issues, API rate limiting, or missing data for a requested title.
**Examples:**

```python
>>> song_list = ["Love Story", "Blank Space", "Shake It Off"]
>>> artist = "Taylor Swift"
>>> lyrics = fetch_lyrics_batch(song_titles=song_list, artist=artist)
>>> print(lyrics[0])
"We were both young when I first saw you..."
```



---

## fetch_chart_performance_data

### Description
Retrieve chart performance data for a specified artist and list of songs from an external chart service and return the data as a JSON string.

### Conceptual Info

- **Purpose**: Collect accurate, up‑to‑date chart rankings for a given artist’s songs.
- **Key Implementation Points**:
  1. **API Integration**: Use a RESTful chart API (e.g., Billboard, Spotify Charts) with proper authentication.
  2. **Data Normalization**: Parse and map raw API responses to a consistent JSON schema.
  3. **Error Handling & Retries**: Gracefully handle HTTP errors, missing data, and implement exponential back‑off for transient failures.

### Docstring

**Summary:** Retrieve chart performance data for a list of songs by a specific artist.

**Parameters:**

- artist (str): Name of the artist whose chart data is requested.
- songs (str): Comma‑separated list of song titles.
**Returns:** str - JSON string mapping each song title to its current chart position.

**Raises:**

- ValueError: Raised if the API request fails or returns an unexpected format.
**Examples:**

```python
>>> output = fetch_chart_performance_data(artist="Taylor Swift", songs="Love Story, Blank Space")
>>> print(output)
{"Love Story": 1, "Blank Space": 2}
```



---

## extract_chart_positions

### Description
Extracts an ordered list of integer chart positions from the provided chart_data string, preserving the original data order.

### Conceptual Info

Shim to convert raw chart metadata into a concrete sequence of numeric chart positions for downstream validation and analytics.

### Docstring

**Summary:** Parse a chart_data string to produce an ordered List[int] of chart positions.

**Parameters:**

- chart_data (STR): Raw chart data string containing numeric tokens separated by delimiters
**Returns:** LIST_INT - List of parsed integer chart positions in the same order as tokens found in chart_data

**Raises:**

- ValueError: Raised when a token cannot be parsed as an integer, or when input is not a string
**Examples:**

```python
>>> chart_data = '1, 4, 7, 9'
>>> positions = extract_chart_positions(chart_data=chart_data)
[1, 4, 7, 9]
```

```python
>>> chart_data = '2 5; 8'
>>> positions = extract_chart_positions(chart_data=chart_data)
[2, 5, 8]
```



---

## validate_data_completeness

### Description
Validates the completeness and consistency of album, date, lyric, and chart data lists.

### Conceptual Info

Ensures that all data extracted for Taylor Swift's discography is complete before downstream processing.

### Docstring

**Summary:** Validates that all provided data lists are non-empty and of matching length.

**Parameters:**

- albums (List[str]): List of album names.
- dates (List[str]): List of release dates corresponding to the albums.
- lyrics (List[str]): List of song lyrics.
- charts (List[int]): List of chart performance metrics.
**Returns:** str - A message indicating successful validation.

**Raises:**

- ValueError: If any input list is empty or the lists are of differing lengths.
**Examples:**

```python
>>> albums = ['Folklore', 'Evermore']
>>> dates = ['2020-07-24', '2021-12-10']
>>> lyrics = ['...', '...']
>>> charts = [5, 3]
>>> result = validate_data_completeness(albums=albums, dates=dates, lyrics=lyrics, charts=charts)
>>> print(result)
"Validation successful"
```

