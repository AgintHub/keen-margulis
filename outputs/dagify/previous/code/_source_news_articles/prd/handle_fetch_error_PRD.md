# handle_fetch_error PRD

## Description
Handles errors during article fetching and returns a standardized error message.


## Conceptual Info

This shim provides a consistent way to handle and report failures that occur while attempting to fetch news articles from various sources, ensuring that downstream processes receive a clear, structured error description.

## Docstring

### Summary
Creates a standardized error message for failed article fetch attempts.

### Parameters

- **error** (Exception): The exception raised during the fetch operation.
- **source** (str): The name of the news source from which the fetch failed.

### Returns

str: A user‑friendly string summarizing the error and the source.

### Raises

- ValueError: If `source` is not a non‑empty string.
- TypeError: If `error` is not an exception instance.

### Examples

```python
>>> error = ValueError('Network unreachable')
>>> msg = handle_fetch_error(error=error, source='BBC')
>>> print(msg)
'Failed to fetch from BBC: Network unreachable'
```

```python
>>> error = Exception('Timeout')
>>> msg = handle_fetch_error(error=error, source='Reuters')
>>> print(msg)
'Failed to fetch from Reuters: Timeout'
```
