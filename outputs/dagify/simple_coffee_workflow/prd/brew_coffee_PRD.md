# brew_coffee PRD

## Description
Simulates heating a liquid (water, tea, or any beverage base) to its boiling point, measuring the duration taken and confirming readiness for downstream brewing or processing steps.


## Conceptual Info

The boil_any_liquid node models the physical process of heating a liquid to its boiling point, capturing key performance metrics such as time, temperature, and success status to inform subsequent brewing stages.

## Docstring

### Summary
Boil the specified liquid to its target boiling temperature and report readiness metrics.

### Parameters

- **target_temperature_celsius** (float): Desired boiling temperature for the liquid in degrees Celsius.

### Returns

dict: Dictionary containing boiled status, temperature, and boil time.

### Raises

- ValueError: Raised if the liquid fails to reach the target temperature within the allowed timeframe.

### Examples

```python
>>> result = boil_any_liquid(target_temperature_celsius=100.0)
>>> print(result['boiled'], result['temperature_celsius'], result['boil_time_seconds'])
True 100.0 45
```
