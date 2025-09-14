# fetch_market_data PRD

## Description
Retrieve current market data, including prices and volumes.


## Conceptual Info

Fetches the latest market data, including prices and volumes, from reliable sources.

## Docstring

### Summary
Retrieve current market data, including prices and volumes, from reliable sources.

### Returns

Tuple[List[float], List[int]]: A tuple containing a list of current market prices and a list of current market volumes.

### Raises

- ConnectionError: If there's a failure connecting to the market data source.
- DataError: If the retrieved data is malformed or incomplete.

### Examples

```python
>>> market_data = fetch_market_data()
>>> prices, volumes = market_data['market_prices'], market_data['market_volumes']
{'market_prices': [12.5, 13.2, 11.8], 'market_volumes': [100, 200, 150]}
```
