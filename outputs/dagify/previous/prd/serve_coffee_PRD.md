# serve_coffee PRD

## Description
Serve the coffee


## Conceptual Info

This node takes the results of the brewing process, verifies that brewing succeeded, converts the brewed volume from cups to milliliters, and simulates pouring the coffee into a cup while preserving its temperature.

## Docstring

### Summary
Serve freshly brewed coffee into a cup based on brewing results.

### Parameters

- **brew_start_timestamp** (str): ISO 8601 timestamp when brewing started.
- **brew_end_timestamp** (str): ISO 8601 timestamp when brewing completed.
- **brew_duration_seconds** (float): Total duration of the brewing process in seconds.
- **brewed_volume_cups** (int): Number of cups of coffee brewed.
- **brewed_success** (bool): Indicates whether the brewing process completed successfully.
- **final_temperature_c** (float): Final temperature of the brewed coffee in degrees Celsius.

### Returns

dict: A dictionary with keys:
  - served (bool): Whether the coffee was served.
  - temperature_c (float): Served coffee temperature.
  - volume_ml (int): Served coffee volume in milliliters.

### Raises

- ValueError: Raised if `brewed_success` is False, indicating the coffee cannot be served.

### Examples

```python
>>> serve_coffee(
...     brew_start_timestamp="2025-10-11T10:00:00Z",
...     brew_end_timestamp="2025-10-11T10:03:30Z",
...     brew_duration_seconds=210.0,
...     brewed_volume_cups=2,
...     brewed_success=True,
...     final_temperature_c=90.0)
{
  'served': True,
  'temperature_c': 90.0,
  'volume_ml': 480
}
```

```python
>>> serve_coffee(
...     brew_start_timestamp="2025-10-11T10:10:00Z",
...     brew_end_timestamp="2025-10-11T10:12:00Z",
...     brew_duration_seconds=120.0,
...     brewed_volume_cups=1,
...     brewed_success=False,
...     final_temperature_c=85.0)
ValueError: Brewed coffee is not successful; cannot serve.
```
