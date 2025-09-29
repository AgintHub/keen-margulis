# gather_market_data PRD

## Description
Gather market data from various sources such as exchanges, APIs, or financial databases.


## Conceptual Info

This node is responsible for collecting current and historical market data from various financial sources.

## Docstring

### Summary
Gathers market data including current prices, historical prices, and trading volumes.

### Parameters

- **data_sources** (List[str]): List of financial data sources (e.g., exchanges, APIs, databases) to gather data from.
- **assets** (List[str]): List of assets (e.g., stocks, cryptocurrencies) for which to gather market data.

### Returns

Dict[str, List[float]]: A dictionary containing current prices, historical prices, and market volumes for the specified assets.

### Raises

- ConnectionError: If there's an issue connecting to any of the specified data sources.
- ValueError: If the list of assets or data sources is empty or invalid.

### Examples

```python
>>> gather_market_data(data_sources=['exchange1', 'api2'], assets=['BTC', 'ETH'])
{'current_prices': [35000.0, 2500.0], 'historical_prices': [[34000.0, 34500.0, 35000.0], [2400.0, 2450.0, 2500.0]], 'market_volumes': [1000.0, 500.0]}
```

```python
>>> gather_market_data(data_sources=['database3'], assets=['AAPL', 'GOOGL'])
{'current_prices': [150.0, 2800.0], 'historical_prices': [[145.0, 147.0, 150.0], [2750.0, 2780.0, 2800.0]], 'market_volumes': [2000.0, 300.0]}
```
