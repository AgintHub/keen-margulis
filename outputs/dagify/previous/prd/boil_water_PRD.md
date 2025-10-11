# boil_water PRD

## Description
Simulates heating a supplied liquid (water, milk, tea, etc.) to its boiling point, recording the temperature reached, the duration of heating, and whether the liquid is ready for use in downstream processes.


## Conceptual Info

The boil_liquid node is a core thermodynamic simulation step that transforms any input liquid into a ready‑to‑use state for brewing, cooking, or analytical processes. It abstracts the physics of heating while providing measurable metrics that downstream nodes can leverage for timing, quality control, and safety checks.

## Docstring

### Summary
Heats a liquid to its boiling point and returns the readiness status, final temperature, and heating duration.

### Parameters

- **liquid_type** (str): Name of the liquid to be boiled (e.g., "water", "milk", "tea").
- **volume** (float): Volume of the liquid in liters.

### Returns

dict: Dictionary containing `boiled` (bool), `temperature_celsius` (float), and `boil_time_seconds` (int).

### Raises

- ValueError: Raised if an unsupported liquid type is provided.
- RuntimeError: Raised if the heating simulation fails to converge within realistic limits.

### Examples

```python
>>> result = boil_liquid(liquid_type='water', volume=0.5)
>>> print(result)
{'boiled': True, 'temperature_celsius': 100.0, 'boil_time_seconds': 90}
```
