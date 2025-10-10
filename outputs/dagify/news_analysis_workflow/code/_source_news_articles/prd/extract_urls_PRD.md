# extract_urls PRD

## Description
Extracts and returns a list of URLs found in the provided article data.


## Conceptual Info

The shim parses raw article data and isolates URLs for downstream processing.

## Docstring

### Summary
Parses the input article data string to extract all URLs and returns them as a list of strings.

### Parameters

- **data** (str): A JSON-formatted string representation of article data containing URLs.

### Returns

List[str]: A list of URL strings extracted from the input data.

### Raises

- ValueError: Raised when the input data does not contain any URLs.
- TypeError: Raised when the input data is not a string.

### Examples

```python
>>> urls = extract_urls(data='{"content": "Check https://example.com and http://test.com"}')
['https://example.com', 'http://test.com']
```

```python
>>> urls = extract_urls(data='{}')
[]
```
