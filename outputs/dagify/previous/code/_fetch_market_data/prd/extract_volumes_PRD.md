# extract_volumes PRD

## Description
Extracts market volumes from parsed market data.


## Conceptual Info

This shim function is responsible for extracting market volumes from the parsed market data, playing a crucial role in processing financial data for further analysis.

## Docstring

### Summary
Extracts and returns market volumes as a list of integers from the given parsed market data.

### Parameters

- **parsed_data** (str): A string representation of parsed market data containing volume information.

### Returns

List[int]: A list of integers representing the extracted market volumes.

### Raises

- ValueError: If the parsed_data is not in the expected format or if volume extraction fails.
- TypeError: If the input parsed_data is not of type str.

### Examples

```python
>>> parsed_data = '{ "market_volumes": [100, 200, 300] }'
>>> volumes = extract_volumes(parsed_data=parsed_data)
>>> print(volumes)
[100, 200, 300]
```

```python
>>> parsed_data = 'Invalid data format'
>>> try:
...     volumes = extract_volumes(parsed_data=parsed_data)
>>> except ValueError as e:
...     print(e)
Invalid data format
```
