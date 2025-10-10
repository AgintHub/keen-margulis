# fetch_articles_from_source PRD

## Description
Retrieves news article data for a specified source and returns it as a JSON-formatted string.


## Conceptual Info

This shim abstracts the logic for fetching and aggregating article metadata from a given news source. It isolates external API interactions and data extraction, providing a consistent JSON interface for downstream processing.

## Docstring

### Summary
Fetches news articles from a specified source and returns article metadata as a JSON string.

### Parameters

- **source** (str): Identifier of the news source to query (e.g., 'NYTimes', 'BBC'). Must be a non-empty string.

### Returns

str: JSON-formatted string containing a dictionary with keys: 'urls', 'titles', 'texts', and 'sources', each mapping to a list of strings.

### Raises

- ValueError: Raised when the `source` argument is an empty string or represents an unsupported news source.
- TypeError: Raised when the `source` argument is not of type `str`.

### Examples

```python
>>> result = fetch_articles_from_source('NYTimes')
"{\"urls\": [\"https://nytimes.com/article1\"], \"titles\": [\"Breaking News\"], \"texts\": [\"Full article text...\"], \"sources\": [\"NYTimes\"]}"
```

```python
>>> try:
...     fetch_articles_from_source('')
>>> except ValueError as e:
...     print(e)
"Source identifier must be a non-empty string."
```
