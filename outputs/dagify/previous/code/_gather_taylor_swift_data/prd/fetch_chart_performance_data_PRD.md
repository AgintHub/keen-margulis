# fetch_chart_performance_data PRD

## Description
Retrieve chart performance data for a specified artist and list of songs from an external chart service and return the data as a JSON string.


## Conceptual Info

- **Purpose**: Collect accurate, up‑to‑date chart rankings for a given artist’s songs.
- **Key Implementation Points**:
  1. **API Integration**: Use a RESTful chart API (e.g., Billboard, Spotify Charts) with proper authentication.
  2. **Data Normalization**: Parse and map raw API responses to a consistent JSON schema.
  3. **Error Handling & Retries**: Gracefully handle HTTP errors, missing data, and implement exponential back‑off for transient failures.

## Docstring

### Summary
Retrieve chart performance data for a list of songs by a specific artist.

### Parameters

- **artist** (str): Name of the artist whose chart data is requested.
- **songs** (str): Comma‑separated list of song titles.

### Returns

str: JSON string mapping each song title to its current chart position.

### Raises

- ValueError: Raised if the API request fails or returns an unexpected format.

### Examples

```python
>>> output = fetch_chart_performance_data(artist="Taylor Swift", songs="Love Story, Blank Space")
>>> print(output)
{"Love Story": 1, "Blank Space": 2}
```
