# extract_album_names PRD

## Description
Extracts a list of album names from the JSON-formatted discography data.


## Conceptual Info

This shim parses raw discography metadata and extracts the album titles to support downstream data gathering steps.

## Docstring

### Summary
Extract album names from a discography JSON string.

### Parameters

- **discography_data** (str): JSON-formatted string containing the discography data.

### Returns

List[str]: A list of album names in the order they appear in the input.

### Raises

- ValueError: Raised when the input is not valid JSON or the expected 'albums' key is missing.

### Examples

```python
>>> discography_data_json = '{"albums": ["Fearless", "1989", "Red"]}'
>>> album_names = extract_album_names(discography_data_json)
>>> print(album_names)
['Fearless', '1989', 'Red']
```
