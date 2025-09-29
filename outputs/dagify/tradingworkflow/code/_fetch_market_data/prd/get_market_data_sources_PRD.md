# get_market_data_sources PRD

## Description
Retrieves a list of URLs for market data sources.


## Conceptual Info

This shim function is responsible for providing a list of URLs that serve as sources for market data. It acts as a bridge to fetch the necessary data for further processing.

## Docstring

### Summary
Fetches and returns a list of URLs for market data sources.

### Returns

List[str]: A list of URLs where market data can be fetched.

### Raises

- RuntimeError: If there's an issue retrieving the market data sources.

### Examples

```python
>>> sources = get_market_data_sources()
['https://source1.com/data', 'https://source2.com/data']
```

```python
>>> print(get_market_data_sources())
['https://source1.com/data', 'https://source2.com/data']
```
