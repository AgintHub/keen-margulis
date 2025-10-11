# boil_water PRD

## Description
Boil water for the coffee


## Conceptual Info

The boil_water node simulates heating water to its boiling point, measuring how long the process takes and confirming readiness for brewing.

## Docstring

### Summary
Boils water to 100 °C, measures the boiling time, and indicates when it is ready for coffee brewing.

### Returns

Dict[str, Any]: A dictionary containing three keys:
- 'boiled' (bool): True if water has reached boiling point.
- 'temperature_celsius' (float): The final temperature in Celsius.
- 'boil_time_seconds' (int): Number of seconds elapsed during boiling.

### Raises

- ValueError: Raised if the boiling simulation fails due to invalid conditions (e.g., insufficient water).

### Examples

```python
>>> output = boil_water()
>>> print(output)
{'boiled': True, 'temperature_celsius': 100.0, 'boil_time_seconds': 120}
```
