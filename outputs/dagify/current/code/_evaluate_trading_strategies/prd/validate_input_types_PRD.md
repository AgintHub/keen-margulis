# validate_input_types PRD

## Description
Validate that the predictions list contains strings and the confidence list contains floats of equal length.


## Conceptual Info

This shim ensures the core data passed between market trend analysis and strategy evaluation nodes is correctly typed and structurally consistent, preventing downstream processing errors.

## Docstring

### Summary
Validate that the inputs `predictions` and `confidence` are lists of the expected types and have matching lengths.

### Parameters

- **predictions** (List[str]): A list of trend predictions, each element should be a string.
- **confidence** (List[float]): A list of confidence scores corresponding to each prediction, each element should be a float.

### Returns

str: A message confirming successful validation, e.g., `'Validation successful'`.

### Raises

- ValueError: Raised if the lengths of `predictions` and `confidence` differ.
- TypeError: Raised if any element of `predictions` is not a string or any element of `confidence` is not a float.

### Examples

```python
>>> output = validate_input_types(predictions=['trend1', 'trend2'], confidence=[0.9, 0.8])
'Validation successful'
```

```python
>>> output = validate_input_types(predictions=['trend1'], confidence=[0.9])
'Validation successful'
```
