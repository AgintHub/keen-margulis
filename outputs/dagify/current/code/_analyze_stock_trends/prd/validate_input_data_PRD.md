# validate_input_data PRD

## Description
Validates input stock data and trading volumes for analysis.


## Conceptual Info

This shim node is responsible for validating the input stock data and trading volumes before they are used for trend analysis.

## Docstring

### Summary
Validates input stock data and trading volumes for correct format and content.

### Parameters

- **cleaned_data** (str): Preprocessed stock price data to be validated.
- **volumes** (str): Normalized trading volumes to be validated.

### Returns

str: Output indicating the validation result.

### Raises

- ValueError: If the input data or volumes are not in the expected format or range.
- TypeError: If the input types are not as expected.

### Examples

```python
>>> validate_input_data(cleaned_data='[1.0, 2.0, 3.0]', volumes='[100, 200, 300]')
'Input data is valid'
```

```python
>>> validate_input_data(cleaned_data='invalid_data', volumes='[100, 200, 300]')
ValueError: Invalid input data format
```
