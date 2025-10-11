# convert_cups_to_ml PRD

## Description
Converts a given volume in cups to its equivalent in milliliters.


## Conceptual Info

This shim provides a standardized conversion from cups to milliliters, enabling the coffee brewing system to express volumes in metric units for consistency.

## Docstring

### Summary
Converts a volume measurement from cups to milliliters using the standard conversion factor of 236.588 ml per cup.

### Parameters

- **volume_cups** (int): The number of cups to be converted; must be a non‑negative integer.

### Returns

int: The equivalent volume in milliliters, rounded to the nearest integer.

### Raises

- ValueError: Raised if `volume_cups` is negative.
- TypeError: Raised if `volume_cups` is not an integer.

### Examples

```python
>>> convert_cups_to_ml(2)
473
```

```python
>>> convert_cups_to_ml(0)
0
```
