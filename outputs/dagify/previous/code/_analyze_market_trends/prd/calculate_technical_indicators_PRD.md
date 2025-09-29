# calculate_technical_indicators PRD

## Description
Calculates technical indicators based on given market prices and volumes.


## Conceptual Info

This shim node is responsible for computing technical indicators from market data, which are crucial for analyzing market trends.

## Docstring

### Summary
Calculates technical indicators from given market prices and volumes.

### Parameters

- **prices** (str): String representation of market prices, expected to be a list of floats.
- **volumes** (str): String representation of market volumes, expected to be a list of integers.

### Returns

List[float]: List of technical indicators calculated from the input prices and volumes.

### Raises

- ValueError: If the input strings cannot be parsed into lists of numbers.
- TypeError: If the input types are not strings or if the parsed lists contain non-numeric values.

### Examples

```python
>>> prices = '[1.0, 2.0, 3.0]'
>>> volumes = '[100, 200, 300]'
>>> calculate_technical_indicators(prices=prices, volumes=volumes)
[0.5, 1.0, 1.5]
```

```python
>>> prices = '[4.0, 5.0, 6.0]'
>>> volumes = '[400, 500, 600]'
>>> calculate_technical_indicators(prices=prices, volumes=volumes)
[2.0, 2.5, 3.0]
```
