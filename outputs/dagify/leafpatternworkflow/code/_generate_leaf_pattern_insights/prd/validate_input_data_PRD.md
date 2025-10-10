# validate_input_data PRD

## Description
Validates the input data for vein patterns and colors to ensure they are in the correct format and contain valid information.


## Conceptual Info

This shim function is designed to validate the input data for leaf vein patterns and colors, ensuring that the data is correctly formatted and contains valid information before it is processed further in the system.

## Docstring

### Summary
Validates input lists of vein patterns and colors to ensure they are not empty and contain valid string entries.

### Parameters

- **vein_patterns** (str): A list of vein patterns as strings that need to be validated.
- **colors** (str): A list of colors as strings that need to be validated.

### Returns

str: A message indicating whether the input data is valid or not.

### Raises

- ValueError: If either vein_patterns or colors is empty or contains invalid entries.
- TypeError: If the input types for vein_patterns or colors are not as expected.

### Examples

```python
>>> validate_input_data(vein_patterns='["pattern1", "pattern2"]', colors='["red", "green"]')
'Input data is valid'
```

```python
>>> validate_input_data(vein_patterns='[]', colors='["red", "green"]')
ValueError: Input lists cannot be empty
```
