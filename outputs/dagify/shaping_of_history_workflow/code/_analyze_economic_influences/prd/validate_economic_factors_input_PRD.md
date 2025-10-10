# validate_economic_factors_input PRD

## Description
Validates a list of economic factor names, ensuring each is a non-empty alphabetic string and returns the cleaned list.


## Conceptual Info

This shim sanitizes the list of economic factors passed from the identify_key_factors node, ensuring that downstream analysis receives only valid, clean factor names.

## Docstring

### Summary
Validate and sanitize a list of economic factor names.

### Parameters

- **factors** (List[str]): List of raw economic factor names to validate.

### Returns

List[str]: A cleaned list of valid economic factor names.

### Raises

- TypeError: If `factors` is not a list or contains non-string elements.
- ValueError: If any factor is empty or contains non-alphabetic characters.

### Examples

```python
>>> validate_economic_factors_input(['inflation', 'gdp', 'taxation'])
['inflation', 'gdp', 'taxation']
```

```python
>>> validate_economic_factors_input(['inflation', '123', 'gdp'])
ValueError: Factor '123' contains non-alphabetic characters.
```
