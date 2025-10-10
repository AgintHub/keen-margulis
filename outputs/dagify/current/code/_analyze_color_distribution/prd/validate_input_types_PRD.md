# validate_input_types PRD

## Description
Validates that the input colors and scores are of the correct type.


## Conceptual Info

This shim function is designed to validate the types of input parameters, specifically checking if the provided colors and scores are of the expected types.

## Docstring

### Summary
Validates the types of input colors and scores.

### Parameters

- **colors** (List[str]): List of detected vehicle colors.
- **scores** (List[float]): List of confidence scores corresponding to the detected vehicle colors.

### Returns

str: A message indicating whether the input types are valid.

### Raises

- TypeError: If the input colors are not a list of strings or if the scores are not a list of floats.

### Examples

```python
>>> colors = ['red', 'blue', 'green']
>>> scores = [0.8, 0.9, 0.7]
>>> validate_input_types(colors=colors, scores=scores)
'Input types are valid.'
```

```python
>>> colors = ['red', 1, 'green']
>>> scores = [0.8, 0.9, 0.7]
>>> validate_input_types(colors=colors, scores=scores)
TypeError: 'colors' must be a list of strings.
```
