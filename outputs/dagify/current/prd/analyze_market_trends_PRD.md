# analyze_market_trends PRD

## Description
Use technical indicators and machine learning algorithms to analyze market trends.


## Conceptual Info

This node analyzes market trends using technical indicators and machine learning algorithms.

## Docstring

### Summary
Analyzes market data to identify trends and patterns.

### Parameters

- **current_prices** (List[float]): Current prices of relevant assets gathered from gather_market_data node.
- **historical_prices** (List[float]): Historical price data for relevant assets gathered from gather_market_data node.
- **market_volumes** (List[float]): Current trading volumes of relevant assets gathered from gather_market_data node.

### Returns

Tuple[List[float], List[str]]: A tuple containing trend indicators and pattern recognition results.

### Raises

- ValueError: If input data is inconsistent or missing.

### Examples

```python
>>> current_prices = [100.0, 120.0, 110.0]
>>> historical_prices = [90.0, 100.0, 110.0, 120.0, 130.0]
>>> market_volumes = [1000.0, 1200.0, 1100.0]
>>> result = analyze_market_trends(current_prices, historical_prices, market_volumes)
([0.5, 0.7, 0.3], ['uptrend', 'reversal'])
```
