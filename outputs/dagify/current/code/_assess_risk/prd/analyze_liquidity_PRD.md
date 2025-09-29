# analyze_liquidity PRD

## Description
Analyzes market liquidity based on given volumes and prices.


## Conceptual Info

This shim analyzes market liquidity by processing the given market volumes and prices, providing liquidity metrics as output.

## Docstring

### Summary
Analyzes market liquidity based on the provided volumes and prices.

### Parameters

- **volumes** (str): Market volumes represented as a string, expected to be convertible to a list of integers.
- **prices** (str): Market prices represented as a string, expected to be convertible to a list of floats.

### Returns

List[float]: A list of liquidity metrics indicating the market's liquidity.

### Raises

- ValueError: If the input volumes or prices cannot be converted to their respective expected types.
- TypeError: If the input types are not strings.

### Examples

```python
>>> volumes_str = '100, 200, 300'
>>> prices_str = '10.5, 20.3, 30.7'
>>> analyze_liquidity(volumes=volumes_str, prices=prices_str)
[0.5, 0.6, 0.7]
```

```python
>>> volumes_str = '400, 500, 600'
>>> prices_str = '40.2, 50.1, 60.9'
>>> analyze_liquidity(volumes=volumes_str, prices=prices_str)
[0.8, 0.9, 1.0]
```
