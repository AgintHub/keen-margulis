# check_boiling_status PRD

## Description
Check whether the supplied temperature has reached or exceeded the boiling point.


## Conceptual Info

Determines whether a liquid has reached its boiling point based on its current temperature and the known boiling point for that liquid, providing a boolean result that drives subsequent brewing logic.

## Docstring

### Summary
Determine if a liquid has reached its boiling point.

### Parameters

- **temperature** (float): Current temperature of the liquid in degrees Celsius.
- **boiling_point** (float): Boiling point temperature of the liquid in degrees Celsius.

### Returns

bool: True if temperature is greater than or equal to boiling_point; otherwise False.

### Raises

- ValueError: Raised when temperature or boiling_point is negative.
- TypeError: Raised when either temperature or boiling_point is not a numeric type.

### Examples

```python
>>> check_boiling_status(temperature=100.0, boiling_point=100.0)
True
```

```python
>>> check_boiling_status(temperature=90.0, boiling_point=100.0)
False
```
