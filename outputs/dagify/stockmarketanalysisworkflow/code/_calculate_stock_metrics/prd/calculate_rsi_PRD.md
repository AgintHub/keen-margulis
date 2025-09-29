# calculate_rsi PRD

## Description
Calculates Relative Strength Index (RSI) values based on given price data and trading volumes.


## Conceptual Info

This shim node is responsible for calculating the Relative Strength Index (RSI), a technical indicator used to measure the magnitude of recent price changes in order to determine overbought or oversold conditions.

## Docstring

### Summary
Calculates RSI values based on the provided price data and trading volumes.

### Parameters

- **price_data** (str): Serialized list of float values representing stock prices.
- **volumes** (str): Serialized list of float values representing trading volumes.

### Returns

List[float]: List of RSI values corresponding to the input price data.

### Raises

- ValueError: If the input price data or volumes are not valid serialized lists of floats.
- TypeError: If the input types are not strings or if deserialization fails.

### Examples

```python
>>> import json
>>> price_data = json.dumps([12.5, 13.2, 12.8, 13.5, 14.1])
>>> volumes = json.dumps([1000, 1200, 1100, 1300, 1400])
>>> rsi_values = calculate_rsi(price_data=price_data, volumes=volumes)
[0.45, 0.52, 0.48, 0.55, 0.60]
```

```python
>>> import json
>>> price_data = json.dumps([25.1, 24.8, 25.3, 24.9, 25.5])
>>> volumes = json.dumps([2000, 2100, 2200, 2300, 2400])
>>> rsi_values = calculate_rsi(price_data=price_data, volumes=volumes)
[0.58, 0.55, 0.60, 0.57, 0.62]
```
