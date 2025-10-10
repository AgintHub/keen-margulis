# validate_input_lengths PRD

## Description
Validates that the input lists have the same length.


## Conceptual Info

This shim node validates that the input lists for evaluations and strategies have the same length, ensuring data consistency before further processing.

## Docstring

### Summary
Validates the lengths of input lists for evaluations and strategies.

### Parameters

- **evaluations** (str): String representation of a list of evaluations.
- **strategies** (str): String representation of a list of strategies.

### Returns

str: Output indicating whether the input lists have the same length.

### Raises

- ValueError: If the lengths of the input lists do not match.

### Examples

```python
>>> validate_input_lengths(evaluations='[1, 2, 3]', strategies='["a", "b", "c"]')
'Input lengths are valid'
```

```python
>>> validate_input_lengths(evaluations='[1, 2]', strategies='["a", "b", "c"]')
ValueError: 'Input lists have different lengths'
```
