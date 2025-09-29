# extract_market_volumes PRD

## Description
Extracts market volumes from validated market data.


## Conceptual Info

This shim node is responsible for extracting market volumes from validated market data, playing a crucial role in providing the necessary data for further processing in the market data pipeline.

## Docstring

### Summary
Extracts market volumes from the provided validated market data string.

### Parameters

- **data** (str): Validated market data in string format, expected to contain volume information.

### Returns

List[int]: A list of integers representing the current market volumes extracted from the input data.

### Raises

- ValueError: When the input data is malformed or does not contain valid volume information.
- TypeError: When the input data is not of type string.

### Examples

```python
>>> extract_market_volumes(data='{"market_volumes": [100, 200, 300]}')
[100, 200, 300]
```

```python
>>> extract_market_volumes(data='invalid_data')
ValueError: Invalid data format
```
