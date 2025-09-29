# analyze_market_trends PRD

## Description
Analyze market trends using historical data and technical indicators


## Conceptual Info

This node analyzes market trends using historical data and technical indicators, producing trend indicators and directions.

## Docstring

### Summary
Analyze market trends using historical data and technical indicators.

### Parameters

- **market_prices** (List[float]): List of current market prices from fetch_market_data node.
- **market_volumes** (List[int]): List of current market volumes from fetch_market_data node.

### Returns

Tuple[List[float], List[str]]: A tuple containing a list of trend indicators and a list of trend directions.

### Raises

- ValueError: If market_prices or market_volumes are empty or malformed.

### Examples

```python
>>> market_prices = [100.0, 120.0, 110.0]
>>> market_volumes = [1000, 1200, 1100]
>>> trend_indicators, trend_directions = analyze_market_trends(market_prices, market_volumes)
([1.2, 0.9, 1.1], ['up', 'down', 'up'])
```
