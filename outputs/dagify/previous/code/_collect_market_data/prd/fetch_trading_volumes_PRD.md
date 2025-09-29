# fetch_trading_volumes PRD

## Description
Fetches trading volumes from specified data sources and returns them as a list of integers.


## Conceptual Info

This shim node is responsible for retrieving trading volume data from various market data sources, playing a crucial role in the market data collection process.

## Docstring

### Summary
Fetches trading volumes from the specified data sources and returns them as a list of integers.

### Parameters

- **sources** (str): A string representing the data sources to fetch trading volumes from.

### Returns

List[int]: A list of integers representing the trading volumes retrieved from the specified sources.

### Raises

- ValueError: If the input sources string is invalid or empty.
- TypeError: If the input sources is not a string.

### Examples

```python
>>> fetch_trading_volumes(sources='NYSE, NASDAQ')
>>> # Returns a list of trading volumes for the specified exchanges
[1000, 2000, 3000]
```

```python
>>> fetch_trading_volumes(sources='LSE')
>>> # Returns a list of trading volumes for the London Stock Exchange
[500, 800, 1200]
```
