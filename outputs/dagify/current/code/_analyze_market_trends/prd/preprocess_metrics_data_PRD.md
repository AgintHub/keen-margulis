# preprocess_metrics_data PRD

## Description
Preprocesses raw market metric strings into a list of normalized floating-point values suitable for trend analysis.


## Conceptual Info

This shim converts raw market metric descriptions into numerical data for downstream analytical nodes.

## Docstring

### Summary
Converts a raw metrics string into a list of floats.

### Parameters

- **metrics** (str): Raw market metrics as a single string, e.g., "volume: 1000; price: 23.5".

### Returns

List[float]: A list of floating-point numbers extracted from the input metrics.

### Raises

- ValueError: Raised when no numeric values are found in the input.
- TypeError: Raised when metrics is not a string.

### Examples

```python
>>> preprocess_metrics_data('volume: 1000; price: 23.5')
[1000.0, 23.5]
```

```python
>>> preprocess_metrics_data('unparsable')
ValueError: No numeric metrics found in input string.
```
