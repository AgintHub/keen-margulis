# validate_cooking_techniques PRD

## Description
Validates the cooking techniques provided to ensure they are appropriate for meal preparation.


## Conceptual Info

This shim node is responsible for validating cooking techniques provided as input to ensure they are valid and appropriate for meal preparation.

## Docstring

### Summary
Validates cooking techniques to ensure they are appropriate for meal preparation.

### Parameters

- **cooking_techniques** (str): A string containing cooking techniques separated by commas.

### Returns

str: A message indicating whether the cooking techniques are valid.

### Raises

- ValueError: When the cooking techniques provided are invalid or not supported.
- TypeError: When the input type is not a string.

### Examples

```python
>>> validate_cooking_techniques(cooking_techniques='roasting,baking')
'Cooking techniques are valid.'
```

```python
>>> validate_cooking_techniques(cooking_techniques='invalid_technique')
'ValueError: Invalid cooking technique: invalid_technique'
```
