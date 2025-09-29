# validate_market_data PRD

## Description
Validates market data by checking the consistency and correctness of the provided prices and volumes.


## Conceptual Info

This shim node is responsible for validating market data, ensuring that the provided prices and volumes are consistent and correct before further processing.

## Docstring

### Summary
Validates market data by checking the consistency and correctness of the provided prices and volumes.

### Parameters

- **prices** (str): A string representation of a list of market prices.
- **volumes** (str): A string representation of a list of market volumes.

### Returns

str: A dictionary containing the validation result, including information about the validity of the market data.

### Raises

- ValueError: If the input prices or volumes are not valid (e.g., not numeric, negative, or mismatched lengths).
- TypeError: If the input types are incorrect (e.g., not strings representing lists).

### Examples

```python
>>> validate_market_data(prices='[10.5, 20.3, 30.7]', volumes='[100, 200, 300]')
{'valid': True, 'message': 'Market data is valid'}
```

```python
>>> validate_market_data(prices='[10.5, 20.3]', volumes='[100, 200, 300]')
{'valid': False, 'message': 'Mismatch in prices and volumes lengths'}
```
