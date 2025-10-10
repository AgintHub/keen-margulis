# validate_sport_input PRD

## Description
Validates a sport name against a predefined list of supported sports and returns the standardized sport name.


## Conceptual Info

This shim ensures that only known sports are propagated through the system, preventing downstream errors and normalizing input for consistent processing.

## Docstring

### Summary
Validates the input sport name against a list of supported sports and returns the canonical name.

### Parameters

- **sport_name** (str): The sport name to validate. Must be a non-empty string.

### Returns

str: The validated sport name in lowercase, matching one of the supported sports.

### Raises

- TypeError: If sport_name is not of type str.
- ValueError: If sport_name is not found in the list of supported sports.

### Examples

```python
>>> result = validate_sport_input("soccer")
>>> print(result)
'soccer'
```

```python
>>> validate_sport_input("unknown_sport")
ValueError: "'unknown_sport' is not a supported sport name."
```
