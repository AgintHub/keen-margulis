# process_historical_volumes PRD

## Description
Processes historical volume data into a list of floats.


## Conceptual Info

This shim node is responsible for processing historical volume data, transforming it into a standardized format (list of floats) that can be used by downstream nodes in the pipeline.

## Docstring

### Summary
Processes historical volume data into a list of floats.

### Parameters

- **data** (str): Input string containing historical volume data that needs to be processed.

### Returns

List[float]: A list of floats representing the processed historical volumes.

### Raises

- ValueError: If the input data is malformed or cannot be converted to a list of floats.
- TypeError: If the input data is not a string.

### Examples

```python
>>> process_historical_volumes(data='{"volumes": [100.5, 200.3, 300.7]}')
[100.5, 200.3, 300.7]
```

```python
>>> process_historical_volumes(data='[150.2, 250.1, 350.9]')
[150.2, 250.1, 350.9]
```
