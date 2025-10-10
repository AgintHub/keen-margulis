# validate_market_data PRD

## Description
Validates market data by checking prices and volumes for consistency and correctness.


## Conceptual Info

This shim node is responsible for validating market data, specifically checking if the provided prices and volumes are consistent and correct.

## Docstring

### Summary
Validates market data by checking the consistency and correctness of prices and volumes.

### Parameters

- **prices** (List[float]): List of current market prices to be validated.
- **volumes** (List[int]): List of current market volumes to be validated.

### Returns

str: Output indicating whether the market data is valid or not.

### Raises

- ValueError: When the lengths of prices and volumes lists do not match.
- TypeError: When prices or volumes contain invalid data types.

### Examples

```python
>>> validate_market_data(prices=[10.5, 20.8, 30.1], volumes=[100, 200, 300])
'Market data is valid'
```

```python
>>> validate_market_data(prices=[10.5, 'invalid', 30.1], volumes=[100, 200, 300])
TypeError: Prices must be a list of floats.
```
