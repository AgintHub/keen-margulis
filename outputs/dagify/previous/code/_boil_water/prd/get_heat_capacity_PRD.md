# get_heat_capacity PRD

## Description
Retrieves the specific heat capacity (in J/(kg·K)) of a specified liquid at a standard temperature.


## Conceptual Info

This shim provides a lookup for the specific heat capacity of common brewing liquids, enabling downstream temperature simulations to use accurate thermal properties.

## Docstring

### Summary
Return the specific heat capacity of a given liquid.

### Parameters

- **liquid_type** (str): Name of the liquid (e.g., 'water', 'ethanol').

### Returns

float: Heat capacity of the liquid in J/(kg·K).

### Raises

- ValueError: Raised when the specified liquid type is not supported.
- TypeError: Raised when liquid_type is not a string.

### Examples

```python
>>> from get_heat_capacity import get_heat_capacity
>>> print(get_heat_capacity('water'))
4186.0
```

```python
>>> print(get_heat_capacity('ethanol'))
2420.0
```
