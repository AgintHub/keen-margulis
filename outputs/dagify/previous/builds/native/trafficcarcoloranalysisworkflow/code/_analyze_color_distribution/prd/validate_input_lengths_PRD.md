# validate_input_lengths PRD

## Description
Validates that the input lists for colors and scores have the same length.


## Conceptual Info

This shim node is responsible for validating that the input lists for colors and their corresponding confidence scores have the same length, ensuring data consistency before further processing.

## Docstring

### Summary
Validates the lengths of input lists 'colors' and 'scores' to ensure they are equal.

### Parameters

- **colors** (List[str]): List of detected vehicle colors.
- **scores** (List[float]): List of confidence scores corresponding to the detected vehicle colors.

### Returns

str: Output indicating whether the input lengths are valid. Returns 'valid' if lengths match, otherwise raises an exception.

### Raises

- ValueError: Raised when the lengths of 'colors' and 'scores' do not match.

### Examples

```python
>>> validate_input_lengths(colors=['red', 'blue', 'green'], scores=[0.8, 0.9, 0.7])
'valid'
```

```python
>>> validate_input_lengths(colors=['red', 'blue'], scores=[0.8, 0.9, 0.7])
ValueError: Input lists 'colors' and 'scores' must have the same length.
```
