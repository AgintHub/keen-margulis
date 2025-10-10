# analyze_price_trends PRD

## Description
Analyzes current and historical price data to identify trends and patterns.


## Conceptual Info

This shim analyzes price trends by comparing current and historical prices, identifying patterns and trends that could inform market analysis.

## Docstring

### Summary
Analyzes current and historical price data to identify market trends and patterns.

### Parameters

- **current_prices** (str): Current prices of the assets in a string format, expected to be a comma-separated list of float values.
- **historical_prices** (str): Historical price data for the assets over a specified period in a string format, expected to be a comma-separated list of float values.

### Returns

List[str]: List of identified price trends and patterns, such as 'bullish', 'bearish', or other trend indicators.

### Raises

- ValueError: If the input strings for current_prices or historical_prices are not properly formatted or contain invalid data.
- TypeError: If the input parameters are not strings.

### Examples

```python
>>> analyze_price_trends(current_prices='100.0,120.0,110.0', historical_prices='90.0,100.0,110.0,120.0,130.0')
>>> output = ['bullish']
['bullish']
```

```python
>>> analyze_price_trends(current_prices='80.0,70.0,60.0', historical_prices='100.0,90.0,80.0,70.0,60.0')
>>> output = ['bearish']
['bearish']
```
