# validate_chart_data PRD

## Description
Validates a string input by parsing it into a clean List[int] of chart positions suitable for downstream chart analysis.


## Conceptual Info

Data validation shim to sanitize and convert string input into numeric chart positions

## Docstring

### Summary
Validate and coerce a string representation of chart data into a List[int] for downstream chart analysis

### Parameters

- **data** (str): String encoding of chart positions to validate and parse into integers

### Returns

List[int]: Validated list of chart positions parsed from the input string

### Raises

- TypeError: If input data is not a string
- ValueError: If the string cannot be parsed into integers or contains invalid values

### Examples

```python
>>> result = validate_chart_data(data='1, 2, 3, 5')
>>> print(result)
[1, 2, 3, 5]
```

```python
>>> result = validate_chart_data(data='[7 4 10]')
>>> print(result)
[7, 4, 10]
```
