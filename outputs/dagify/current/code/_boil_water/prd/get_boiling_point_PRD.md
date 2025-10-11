# get_boiling_point PRD

## Description
Returns the standard boiling point in degrees Celsius for a given liquid type.


## Conceptual Info

The get_boiling_point shim encapsulates the logic for retrieving a liquid’s standard boiling point, serving as a lookup utility that other nodes, such as boil_water, can depend on to perform temperature‑based calculations.

## Docstring

### Summary
Return the standard boiling point of a liquid in degrees Celsius.

### Parameters

- **liquid_type** (str): The name of the liquid (e.g., 'water', 'ethanol').

### Returns

float: The boiling point of the specified liquid in degrees Celsius.

### Raises

- ValueError: Raised when the supplied liquid_type is not supported.
- TypeError: Raised when liquid_type is not a string.

### Examples

```python
>>> get_boiling_point('water')
100.0
```

```python
>>> get_boiling_point('ethanol')
78.37
```
