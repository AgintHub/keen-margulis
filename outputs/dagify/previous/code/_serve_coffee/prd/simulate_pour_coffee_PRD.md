# simulate_pour_coffee PRD

## Description
Simulates the temperature of coffee after it is poured into a cup and returns the resulting temperature in degrees Celsius.


## Conceptual Info

This shim models the heat loss that occurs when coffee is poured from a pot into a cup, providing a realistic temperature for downstream nodes that handle serving or consuming the coffee.

## Docstring

### Summary
Simulates the temperature of coffee after pouring into a cup.

### Parameters

- **temperature_c** (float): The temperature of the coffee before pouring, expressed in degrees Celsius.

### Returns

float: The temperature of the coffee after pouring, in degrees Celsius.

### Raises

- ValueError: Raised when the input temperature is outside the physically realistic range of -10°C to 100°C.
- TypeError: Raised when the input temperature is not a float or int.

### Examples

```python
>>> simulate_pour_coffee(temperature_c=95.0)
90.0
```

```python
>>> simulate_pour_coffee(temperature_c=60.0)
58.0
```
