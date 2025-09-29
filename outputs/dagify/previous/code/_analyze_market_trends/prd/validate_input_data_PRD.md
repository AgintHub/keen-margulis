# validate_input_data PRD

## Description
Validates the input data for market trend analysis by checking prices, volumes, and other metrics.


## Conceptual Info

This shim node is responsible for validating the input data used in market trend analysis, ensuring that prices, volumes, and other metrics are properly formatted and contain valid values.

## Docstring

### Summary
Validates input data for market trend analysis by checking prices, volumes, and other metrics for correct format and valid values.

### Parameters

- **prices** (str): List of historical prices to be validated.
- **volumes** (str): List of historical volumes to be validated.
- **metrics** (str): List of other relevant historical metrics to be validated.

### Returns

str: Output indicating whether the input data is valid or not.

### Raises

- ValueError: When input data contains invalid or inconsistent values.
- TypeError: When input types are not as expected (e.g., not lists or containing non-numeric values).

### Examples

```python
>>> validate_input_data(prices='[1.0, 2.0, 3.0]', volumes='[10, 20, 30]', metrics='["metric1", "metric2"]')
>>> validate_input_data(prices='[1.0, 2.0, 3.0]', volumes='[10, 20, 30]', metrics='["metric1", "metric2"]')
'Input data is valid'
```

```python
>>> validate_input_data(prices='[1.0, abc, 3.0]', volumes='[10, 20, 30]', metrics='["metric1", "metric2"]')
ValueError: Invalid price value 'abc'
```
