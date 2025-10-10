# determine_rush_hour_timing PRD

## Description
Determines the rush hour schedule for a given location.


## Conceptual Info

This shim node is responsible for determining the rush hour schedule for a given location, which is crucial for capturing traffic images during peak hours.

## Docstring

### Summary
Returns a dictionary representing the rush hour schedule for a given location.

### Parameters

- **location** (str): The location for which the rush hour timing needs to be determined.

### Returns

str: A dictionary containing the rush hour schedule with 'start_time' and 'end_time' as keys.

### Raises

- ValueError: If the location is invalid or not supported.
- TypeError: If the input location is not a string.

### Examples

```python
>>> determine_rush_hour_timing(location='downtown')
{'start_time': '07:00', 'end_time': '09:00'}
```

```python
>>> determine_rush_hour_timing(location='suburban_area')
{'start_time': '08:00', 'end_time': '10:00'}
```
