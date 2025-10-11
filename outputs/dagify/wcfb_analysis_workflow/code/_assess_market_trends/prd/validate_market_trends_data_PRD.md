# validate_market_trends_data PRD

## Description
Validates market trends data by converting input string to a list of floats.


## Conceptual Info

This shim node is responsible for validating and converting market trends data from a string format to a list of floats, which is then used for further analysis.

## Docstring

### Summary
Validates market trends data by parsing the input string and returning a list of floats.

### Parameters

- **data** (str): Input string containing market trends data, expected to be a comma-separated list of numbers.

### Returns

List[float]: A list of floats representing the validated market trends data.

### Raises

- ValueError: If the input string cannot be parsed into a list of floats.
- TypeError: If the input is not a string.

### Examples

```python
>>> validate_market_trends_data('1.2,3.4,5.6')
>>> validate_market_trends_data('7.8,9.0')
[1.2, 3.4, 5.6]
```

```python
>>> validate_market_trends_data('invalid,input')
ValueError: Invalid input format
```
