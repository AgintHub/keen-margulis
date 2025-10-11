# brew_coffee PRD

## Description
Brew the coffee by pouring boiled water into a pre‑prepared coffee maker, starting the brewing cycle, and collecting timing, volume, and temperature metrics.


## Conceptual Info

The brew_coffee node simulates the physical act of brewing coffee. It takes the results of boiling water and preparing the coffee maker, pours the water into the machine, initiates the brew cycle, and measures key performance metrics such as start/end timestamps, duration, volume, success flag, and final temperature.

## Docstring

### Summary
Start the brewing process by combining boiled water with a prepared coffee maker and record brewing metrics.

### Parameters

- **boiled** (bool): Indicates whether the water has reached boiling point and is ready for brewing.
- **temperature_celsius** (float): Temperature of the water after boiling, in degrees Celsius.
- **boil_time_seconds** (int): Duration taken to bring the water to boiling temperature, in seconds.
- **coffee_grounds_amount_g** (float): Amount of coffee grounds added to the coffee maker's filter, in grams.
- **filter_prepared** (bool): Whether the filter is properly prepared and ready.
- **coffee_maker_status** (str): Current status of the coffee maker (e.g., 'ready', 'error').
- **desired_cup_count** (int): Number of cups that should be brewed based on the coffee grounds measurement.

### Returns

dict: Dictionary containing brewing timestamps, duration, volume, success flag, and final temperature.

### Raises

- ValueError: Raised if the water is not boiled, the filter is not prepared, the coffee maker status is not 'ready', or any input values are invalid.

### Examples

```python
>>> brew_coffee(
...     boiled=True,
...     temperature_celsius=95.0,
...     boil_time_seconds=120,
...     coffee_grounds_amount_g=18.0,
...     filter_prepared=True,
...     coffee_maker_status='ready',
...     desired_cup_count=2
>>> )
{'brew_start_timestamp': '2025-10-11T08:00:00Z', 'brew_end_timestamp': '2025-10-11T08:03:45Z', 'brew_duration_seconds': 225.0, 'brewed_volume_cups': 2, 'brewed_success': True, 'final_temperature_c': 88.5}
```

```python
>>> brew_coffee(
...     boiled=False,
...     temperature_celsius=0.0,
...     boil_time_seconds=0,
...     coffee_grounds_amount_g=18.0,
...     filter_prepared=True,
...     coffee_maker_status='ready',
...     desired_cup_count=2
>>> )
ValueError: Water must be boiled before brewing.
```
