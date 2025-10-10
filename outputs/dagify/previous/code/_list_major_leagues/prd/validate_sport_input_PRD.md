# validate_sport_input PRD

## Description
Validates and normalizes the sport name input, ensuring it matches supported sports before further processing.


## Conceptual Info

This shim ensures that any sport name passed into the system is valid and in a consistent format, acting as a gatekeeper before downstream operations.

## Docstring

### Summary
Validate and normalize a sport name.

### Parameters

- **sport_name** (str): The sport name provided by the user, to be validated.

### Returns

str: The validated and canonical sport name.

### Raises

- ValueError: Raised when sport_name is empty or does not match any supported sport.
- TypeError: Raised when sport_name is not a string.

### Examples

```python
>>> validate_sport_input('soccer')
'soccer'
```

```python
>>> validate_sport_input('')
ValueError: Sport name must not be empty.
```
