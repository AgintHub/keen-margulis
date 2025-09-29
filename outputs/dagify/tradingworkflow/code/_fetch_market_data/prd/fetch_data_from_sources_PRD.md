# fetch_data_from_sources PRD

## Description
Fetches data from multiple sources and returns it in a structured format.


## Conceptual Info

This shim node is responsible for fetching data from multiple sources and returning it in a structured format that can be further processed downstream.

## Docstring

### Summary
Fetches data from the provided sources and returns it as a list of dictionaries.

### Parameters

- **sources** (str): A string representing the sources from which data should be fetched.

### Returns

List[dict]: A list of dictionaries containing the fetched data from various sources.

### Raises

- ValueError: If the input 'sources' is not a valid string or is empty.
- TypeError: If the input 'sources' is not of type string.

### Examples

```python
>>> sources = 'https://example.com/data1,https://example.com/data2'
>>> result = fetch_data_from_sources(sources=sources)
[{'source': 'https://example.com/data1', 'data': '...'}, {'source': 'https://example.com/data2', 'data': '...'}]
```

```python
>>> sources = 'https://example.com/data3'
>>> result = fetch_data_from_sources(sources=sources)
[{'source': 'https://example.com/data3', 'data': '...'}]
```
