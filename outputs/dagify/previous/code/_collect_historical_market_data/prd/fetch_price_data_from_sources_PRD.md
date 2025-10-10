# fetch_price_data_from_sources PRD

## Description
Fetches historical price data from specified data sources.


## Conceptual Info

This shim node is responsible for retrieving historical price data from various data sources identified by their names or identifiers.

## Docstring

### Summary
Fetches historical price data from the specified data sources and returns it as a list of dictionaries.

### Parameters

- **sources** (str): Comma-separated string of data source names or identifiers from which to fetch the price data.

### Returns

List[dict]: A list of dictionaries where each dictionary contains historical price data for a specific data source.

### Raises

- ValueError: If the input 'sources' is empty or not a string.
- TypeError: If the input 'sources' is not a string.

### Examples

```python
>>> fetch_price_data_from_sources(sources='yahoo,fmp,quandl')
[{'source': 'yahoo', 'data': [...]}, {'source': 'fmp', 'data': [...]}, {'source': 'quandl', 'data': [...]}]
```

```python
>>> fetch_price_data_from_sources(sources='alpha_vantage')
[{'source': 'alpha_vantage', 'data': [...]}]
```
