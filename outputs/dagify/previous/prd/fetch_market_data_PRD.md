# fetch_market_data PRD

## Description
Retrieve current market data from various sources


## Conceptual Info

The fetch_market_data node retrieves current market data from various sources, providing essential information for downstream analysis and decision-making.

## Docstring

### Summary
Fetches current market data, including prices and volumes, from multiple sources.

### Returns

Tuple[List[float], List[int]]: A tuple containing a list of current market prices and a list of current market volumes.

### Raises

- ConnectionError: If there's a failure connecting to market data sources.
- DataParsingError: If there's an issue parsing the received market data.

### Examples

```python
>>> market_data = fetch_market_data()
([123.45, 67.89], [1000, 2000])
```

```python
>>> prices, volumes = fetch_market_data()
>>> print(f'Prices: {prices}')
>>> print(f'Volumes: {volumes}')
Prices: [123.45, 67.89]
Volumes: [1000, 2000]
```
