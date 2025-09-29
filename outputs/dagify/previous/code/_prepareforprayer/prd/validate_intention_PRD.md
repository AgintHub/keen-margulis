# validate_intention PRD

## Description
Validates the given intention to ensure it's appropriate for prayer.


## Conceptual Info

This shim validates the prayer intention to ensure it's suitable for the prayer context.

## Docstring

### Summary
Validates the given prayer intention.

### Parameters

- **intention** (str): The prayer intention to be validated.

### Returns

str: The validated intention if it passes validation.

### Raises

- ValueError: If the intention is empty, too long, or contains inappropriate content.
- TypeError: If the input intention is not a string.

### Examples

```python
>>> validate_intention('world peace')
'world peace'
```

```python
>>> validate_intention('')
ValueError: Intention cannot be empty
```
