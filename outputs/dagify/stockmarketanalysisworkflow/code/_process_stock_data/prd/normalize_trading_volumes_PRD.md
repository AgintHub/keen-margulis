# normalize_trading_volumes PRD

## Description
Normalizes trading volumes to a standard scale for further processing.


## Conceptual Info

This shim node is responsible for normalizing trading volumes, transforming raw volume data into a standardized format that can be used for analysis or further processing.

## Docstring

### Summary
Normalizes trading volumes from a string representation into a list of floats.

### Parameters

- **trading_volumes** (str): A string representation of trading volumes, expected to be a comma-separated list of integers or other valid numerical format.

### Returns

List[float]: A list of normalized trading volumes as floats, scaled appropriately for analysis.

### Raises

- ValueError: If the input string cannot be parsed into a list of numbers.
- TypeError: If the input is not a string or if the string contains non-numerical data that cannot be converted to float.

### Examples

```python
>>> normalize_trading_volumes(trading_volumes='100,200,300,400')
[0.1, 0.2, 0.3, 0.4]
```

```python
>>> normalize_trading_volumes(trading_volumes='500,600,700,800')
[0.5, 0.6, 0.7, 0.8]
```
