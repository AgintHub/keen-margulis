# simulate_heating_process PRD

## Description
Simulates the heating of a liquid until it reaches a target temperature and returns the simulation results as a JSON string.


## Conceptual Info

This shim encapsulates the physics of heating a liquid, modeling how the temperature rises over time given its volume and specific heat capacity. The simulation returns whether it converged, the final temperature reached, and the time taken, allowing downstream nodes to decide brewing readiness.

## Docstring

### Summary
Simulate heating a liquid until it reaches a specified temperature.

### Parameters

- **volume** (str): String representation of the liquid volume in liters.
- **target_temperature** (str): String representation of the desired final temperature in degrees Celsius.
- **heat_capacity** (str): String representation of the specific heat capacity in J/(kg·K).

### Returns

str: A JSON string containing three keys:
- 'converged' (bool): True if the simulation reached the target temperature within realistic limits.
- 'final_temperature' (float): The temperature achieved at the end of the simulation.
- 'time_seconds' (int): The number of seconds required to reach the target temperature.

### Raises

- ValueError: Raised when volume or target_temperature is negative or zero, or if heat_capacity is non‑positive.
- TypeError: Raised if any input is not a string that can be converted to a numeric value.

### Examples

```python
>>> simulate_heating_process(volume='0.5', target_temperature='100', heat_capacity='4184')
{'converged': True, 'final_temperature': 100.0, 'time_seconds': 300}
```

```python
>>> simulate_heating_process(volume='2', target_temperature='60', heat_capacity='4184')
{'converged': True, 'final_temperature': 60.0, 'time_seconds': 150}
```
