# fetch_discography_metadata PRD

## Description
Retrieves a JSON dictionary of discography metadata for the specified artist from an external API or database.


## Conceptual Info

Shim to abstract external data fetching

## Docstring

### Summary
Fetches discography metadata for a given artist.

### Parameters

- **artist** (str): Name of the artist to fetch metadata for.

### Returns

str: JSON string representation of discography metadata.

### Raises

- ValueError: Raised if artist name is empty or None.
- RuntimeError: Raised if external API fails.

### Examples

```python
>>> metadata = fetch_discography_metadata(artist='Taylor Swift')
{'albums': [...], 'release_dates': [...], ...}
```
