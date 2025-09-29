# validate_market_data PRD

## Description
Validates the given market prices and volumes to ensure they are in the correct format and within acceptable ranges.


## Conceptual Info

This shim function is responsible for validating market data, specifically prices and volumes, to ensure they are correctly formatted and within acceptable ranges before further processing.

## Docstring

### Summary
Validates market prices and volumes to ensure they are in the correct format and within acceptable ranges.

### Parameters

- **prices** (str): A string representation of a list of market prices that needs to be validated.
- **volumes** (str): A string representation of a list of market volumes that needs to be validated.

### Returns

str: A success message if the validation is successful.

### Raises

- ValueError: If the input prices or volumes are not valid numbers or are out of range.
- TypeError: If the input prices or volumes are not strings representing lists of numbers.

### Examples

```python
>>> validate_market_data(prices='[1.2, 3.4, 5.6]', volumes='[100, 200, 300]')
'Market data is valid.'
```

```python
>>> validate_market_data(prices='[1.2, abc, 5.6]', volumes='[100, 200, 300]')
ValueError: Invalid price value 'abc' in prices.
```
