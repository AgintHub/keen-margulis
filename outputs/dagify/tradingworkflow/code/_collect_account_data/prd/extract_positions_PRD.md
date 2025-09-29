# extract_positions PRD

## Description
Extracts and processes position data from raw account information.


## Conceptual Info

This shim function is responsible for extracting position data from raw account information and returning it in a processed format.

## Docstring

### Summary
Extracts position data from raw account data and returns it as a string.

### Parameters

- **data** (str): Raw account data containing position information.

### Returns

str: Processed positions data as a string, potentially representing a list or other structured data.

### Raises

- ValueError: If the input raw account data is malformed or missing required information.
- TypeError: If the input data type is not a string.

### Examples

```python
>>> raw_data = '{"positions": [{"symbol": "AAPL", "quantity": 100}, {"symbol": "GOOG", "quantity": 50}]}'
>>> processed_positions = extract_positions(data=raw_data)
'AAPL: 100, GOOG: 50'
```

```python
>>> raw_data = '{"positions": [{"symbol": "MSFT", "quantity": 200}]}'
>>> processed_positions = extract_positions(data=raw_data)
'MSFT: 200'
```
