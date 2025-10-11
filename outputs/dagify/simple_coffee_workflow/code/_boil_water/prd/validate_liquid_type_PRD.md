# validate_liquid_type PRD

## Description
Validates whether a given liquid type is supported for boiling simulation.


## Conceptual Info

This shim ensures the boiling simulation receives only liquid types that have defined physical properties (boiling point and heat capacity). It serves as a gatekeeper before any thermodynamic calculations are performed.

## Docstring

### Summary
Determines if the supplied liquid type is among the supported set for boiling simulation.

### Parameters

- **liquid_type** (str): Name of the liquid (e.g., 'water', 'coffee', 'milk').

### Returns

bool: True if the liquid_type is supported, False otherwise.

### Raises

- TypeError: If liquid_type is not a string.
- ValueError: If liquid_type is an empty string or contains only whitespace.

### Examples

```python
>>> result = validate_liquid_type('water')
>>> print(result)
True
```

```python
>>> result = validate_liquid_type('coffee')
>>> print(result)
False
```

```python
>>> validate_liquid_type(123)
>>> print('This line will not be reached')
Traceback (most recent call last):\n  File "<stdin>", line 1, in <module>\nTypeError: liquid_type must be a string
```
