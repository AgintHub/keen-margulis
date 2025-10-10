# validate_inputs PRD

## Description
Validates the input trend indicators and directions to ensure they are of the correct type and format for further processing.


## Conceptual Info

This shim function is designed to validate the input trend indicators and directions provided to it, ensuring they meet the required format and type expectations before they are used in subsequent processing steps.

## Docstring

### Summary
Validates input trend indicators and directions.

### Parameters

- **trend_indicators** (List[float]): A list of float values representing trend indicators.
- **trend_directions** (List[str]): A list of string values representing trend directions (up, down, neutral).

### Returns

str: A success message if the inputs are valid.

### Raises

- ValueError: If the lengths of trend indicators and directions do not match, or if the trend directions contain invalid values.
- TypeError: If trend indicators are not a list of floats or if trend directions are not a list of strings.

### Examples

```python
>>> validate_inputs(trend_indicators=[0.5, 0.7, 0.3], trend_directions=['up', 'down', 'neutral'])
>>> print('Validation successful')
Validation successful
```

```python
>>> try:
...     validate_inputs(trend_indicators=[0.5, 'invalid', 0.3], trend_directions=['up', 'down', 'neutral'])
>>> except TypeError as e:
...     print(e)
Trend indicators must be a list of floats.
```
