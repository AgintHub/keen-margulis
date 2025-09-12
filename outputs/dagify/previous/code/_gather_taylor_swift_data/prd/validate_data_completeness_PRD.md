# validate_data_completeness PRD

## Description
Validates the completeness and consistency of album, date, lyric, and chart data lists.


## Conceptual Info

Ensures that all data extracted for Taylor Swift's discography is complete before downstream processing.

## Docstring

### Summary
Validates that all provided data lists are non-empty and of matching length.

### Parameters

- **albums** (List[str]): List of album names.
- **dates** (List[str]): List of release dates corresponding to the albums.
- **lyrics** (List[str]): List of song lyrics.
- **charts** (List[int]): List of chart performance metrics.

### Returns

str: A message indicating successful validation.

### Raises

- ValueError: If any input list is empty or the lists are of differing lengths.

### Examples

```python
>>> albums = ['Folklore', 'Evermore']
>>> dates = ['2020-07-24', '2021-12-10']
>>> lyrics = ['...', '...']
>>> charts = [5, 3]
>>> result = validate_data_completeness(albums=albums, dates=dates, lyrics=lyrics, charts=charts)
>>> print(result)
"Validation successful"
```
