# calculate_stock_metrics PRD

## Description
Compute important stock performance metrics.


## Conceptual Info

This node computes key stock performance metrics using preprocessed stock data.

## Docstring

### Summary
Calculates moving averages, Relative Strength Index (RSI), and volatility from preprocessed stock data.

### Parameters

- **cleaned_stock_data** (List[float]): Preprocessed stock price data from the 'process_stock_data' node.
- **normalized_volumes** (List[float]): Normalized trading volumes from the 'process_stock_data' node.

### Returns

Tuple[List[float], List[float], float]: A tuple containing moving averages, RSI values, and volatility measure.

### Raises

- ValueError: If cleaned_stock_data or normalized_volumes are empty or malformed.

### Examples

```python
>>> cleaned_data = [100.0, 101.0, 102.0, 103.0, 104.0]
>>> normalized_volumes = [0.5, 0.6, 0.7, 0.8, 0.9]
>>> moving_averages, rsi_values, volatility = calculate_stock_metrics(cleaned_data, normalized_volumes)
([101.0, 102.0], [0.2, 0.3], 0.015)
```

```python
>>> cleaned_data = [50.0, 51.0, 52.0, 53.0, 54.0]
>>> normalized_volumes = [0.1, 0.2, 0.3, 0.4, 0.5]
>>> moving_averages, rsi_values, volatility = calculate_stock_metrics(cleaned_data, normalized_volumes)
([51.0, 52.0], [0.1, 0.2], 0.020)
```
