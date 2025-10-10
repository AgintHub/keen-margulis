# validate_inputs PRD

## Description
Validates that the sport is a non‑empty string and leagues is a non‑empty list of strings, returning a boolean result


## Conceptual Info

The validate_inputs shim is a guard that ensures downstream processing only occurs when the sport name and list of leagues are properly specified, preventing errors in later data‑fetching stages.

## Docstring

### Summary
Return a boolean indicating whether the provided sport and leagues are valid.

### Parameters

- **sport** (str): The name of the sport; must be a non‑empty string.
- **leagues** (LIST_STR): A list of league names; must contain at least one non‑empty string.

### Returns

bool: True if both `sport` and `leagues` are valid, otherwise False.

### Raises

- ValueError: Raised when `sport` is an empty string or `leagues` is empty or contains non‑string elements.
- TypeError: Raised when `sport` is not a string or `leagues` is not a list.

### Examples

```python
>>> validate_inputs('soccer', ['Premier League', 'La Liga'])
True
```

```python
>>> validate_inputs('', ['Premier League'])
False
```
