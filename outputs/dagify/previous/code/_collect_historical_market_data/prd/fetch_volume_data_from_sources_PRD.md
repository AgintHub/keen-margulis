# fetch_volume_data_from_sources PRD

## Description
Fetches volume data from specified data sources and returns it as a list of dictionaries.


## Conceptual Info

This shim node is responsible for retrieving historical volume data from multiple data sources identified by their names or identifiers.

## Docstring

### Summary
Fetches volume data from specified data sources.

### Parameters

- **sources** (str): A string containing the names or identifiers of the data sources to fetch volume data from.

### Returns

List[dict]: A list of dictionaries where each dictionary contains the volume data fetched from a specific source.

### Raises

- ValueError: If the input 'sources' is not a valid string or if it's empty.
- TypeError: If the input 'sources' is not of type string.

### Examples

```python
>>> fetch_volume_data_from_sources('source1,source2')
[{'source': 'source1', 'volume': 1000}, {'source': 'source2', 'volume': 2000}]
```

```python
>>> fetch_volume_data_from_sources('invalid_source')
[]
```
