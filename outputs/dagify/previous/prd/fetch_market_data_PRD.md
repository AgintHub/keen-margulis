# fetch_market_data PRD

## Description
Fetch market data from reliable sources.


## Conceptual Info

The fetch_market_data node is responsible for retrieving current market data, including prices and volumes, from reliable sources. This data is crucial for downstream nodes that analyze market trends and assess risk.

## Docstring

### Summary
Fetches current market data including prices and volumes.

### Returns

Tuple[List[float], List[int]]: A tuple containing a list of current market prices as floats and a list of current market volumes as integers.

### Raises

- ConnectionError: If there's a failure in connecting to the market data source.
- DataError: If the retrieved data is malformed or incomplete.

### Examples

```python
>>> fetch_market_data()
([12.5, 15.2, 10.8], [100, 200, 50])
```

```python
>>> prices, volumes = fetch_market_data()
prices: [12.5, 15.2, 10.8]
volumes: [100, 200, 50]
```
