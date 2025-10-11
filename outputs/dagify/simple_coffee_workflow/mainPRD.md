# simple_coffee_workflow - Complete PRD Documentation

## Overview
PRDs for nodes in the 'simple_coffee_workflow' module.

## Table of Contents

- [boil_water](#boil_water)

- [brew_coffee](#brew_coffee)

- [measure_coffee](#measure_coffee)

- [prepare_coffee_maker](#prepare_coffee_maker)

- [serve_coffee](#serve_coffee)



---

## boil_water

### Description
Boil water for the coffee

### Conceptual Info

The boil_water node simulates heating water to its boiling point, measuring how long the process takes and confirming readiness for brewing.

### Docstring

**Summary:** Boils water to 100 °C, measures the boiling time, and indicates when it is ready for coffee brewing.

**Returns:** Dict[str, Any] - A dictionary containing three keys:
- 'boiled' (bool): True if water has reached boiling point.
- 'temperature_celsius' (float): The final temperature in Celsius.
- 'boil_time_seconds' (int): Number of seconds elapsed during boiling.

**Raises:**

- ValueError: Raised if the boiling simulation fails due to invalid conditions (e.g., insufficient water).
**Examples:**

```python
>>> output = boil_water()
>>> print(output)
{'boiled': True, 'temperature_celsius': 100.0, 'boil_time_seconds': 120}
```



---

## brew_coffee

### Description
Brew the coffee by pouring boiled water into a pre‑prepared coffee maker, starting the brewing cycle, and collecting timing, volume, and temperature metrics.

### Conceptual Info

The brew_coffee node simulates the physical act of brewing coffee. It takes the results of boiling water and preparing the coffee maker, pours the water into the machine, initiates the brew cycle, and measures key performance metrics such as start/end timestamps, duration, volume, success flag, and final temperature.

### Docstring

**Summary:** Start the brewing process by combining boiled water with a prepared coffee maker and record brewing metrics.

**Parameters:**

- boiled (bool): Indicates whether the water has reached boiling point and is ready for brewing.
- temperature_celsius (float): Temperature of the water after boiling, in degrees Celsius.
- boil_time_seconds (int): Duration taken to bring the water to boiling temperature, in seconds.
- coffee_grounds_amount_g (float): Amount of coffee grounds added to the coffee maker's filter, in grams.
- filter_prepared (bool): Whether the filter is properly prepared and ready.
- coffee_maker_status (str): Current status of the coffee maker (e.g., 'ready', 'error').
- desired_cup_count (int): Number of cups that should be brewed based on the coffee grounds measurement.
**Returns:** dict - Dictionary containing brewing timestamps, duration, volume, success flag, and final temperature.

**Raises:**

- ValueError: Raised if the water is not boiled, the filter is not prepared, the coffee maker status is not 'ready', or any input values are invalid.
**Examples:**

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



---

## measure_coffee

### Description
Measure the coffee grounds

### Conceptual Info

The `measure_coffee` node calculates the required quantity of coffee grounds based on user-provided cup count and grounds type, ensuring the measurement is valid before the grounds are transferred to the coffee maker.

### Docstring

**Summary:** Calculate and verify the amount of coffee grounds needed for a given number of cups.

**Parameters:**

- desired_cup_count (int): The target number of coffee cups to brew.
- grounds_type (str): The type of coffee grounds (e.g., 'medium grind', 'dark roast').
**Returns:** dict - Dictionary containing `ground_amount_grams` (float), `desired_cup_count` (int), `grounds_type` (str), and `measurement_valid` (bool).

**Raises:**

- ValueError: If `desired_cup_count` is not a positive integer or `grounds_type` is not among the supported types.
**Examples:**

```python
>>> measure_coffee(3, 'medium grind')
{'ground_amount_grams': 18.0, 'desired_cup_count': 3, 'grounds_type': 'medium grind', 'measurement_valid': True}
```

```python
>>> measure_coffee(0, 'dark roast')
ValueError: desired_cup_count must be a positive integer.
```



---

## prepare_coffee_maker

### Description
Prepare the coffee maker

### Conceptual Info

Prepares the coffee maker by loading the measured coffee grounds into the filter, verifying filter readiness, and reporting the status of the coffee maker.

### Docstring

**Summary:** Adds the specified amount of coffee grounds into the coffee maker's filter, validates the measurement, and reports the amount added, filter status, and overall maker status.

**Parameters:**

- ground_amount_grams (float): Amount of coffee grounds measured in grams (from measure_coffee).
- desired_cup_count (int): Number of coffee cups to be brewed (from measure_coffee).
- grounds_type (str): Type of coffee grounds used (e.g., medium grind, dark roast).
- measurement_valid (bool): Flag indicating whether the measurement was performed correctly.
**Returns:** dict - Dictionary with keys `coffee_grounds_amount_g` (float), `filter_prepared` (bool), and `coffee_maker_status` (str).

**Raises:**

- ValueError: If `measurement_valid` is False or `ground_amount_grams` is non‑positive.
**Examples:**

```python
>>> result = prepare_coffee_maker(
...     ground_amount_grams=15.0,
...     desired_cup_count=2,
...     grounds_type='medium',
...     measurement_valid=True)
>>> print(result)
{'coffee_grounds_amount_g': 15.0, 'filter_prepared': True, 'coffee_maker_status': 'ready'}
```

```python
>>> try:
...     prepare_coffee_maker(
...         ground_amount_grams=15.0,
...         desired_cup_count=2,
...         grounds_type='medium',
...         measurement_valid=False)
>>> except ValueError as e:
...     print(e)
Invalid measurement: measurement_valid is False
```



---

## serve_coffee

### Description
Serve the coffee

### Conceptual Info

This node takes the results of the brewing process, verifies that brewing succeeded, converts the brewed volume from cups to milliliters, and simulates pouring the coffee into a cup while preserving its temperature.

### Docstring

**Summary:** Serve freshly brewed coffee into a cup based on brewing results.

**Parameters:**

- brew_start_timestamp (str): ISO 8601 timestamp when brewing started.
- brew_end_timestamp (str): ISO 8601 timestamp when brewing completed.
- brew_duration_seconds (float): Total duration of the brewing process in seconds.
- brewed_volume_cups (int): Number of cups of coffee brewed.
- brewed_success (bool): Indicates whether the brewing process completed successfully.
- final_temperature_c (float): Final temperature of the brewed coffee in degrees Celsius.
**Returns:** dict - A dictionary with keys:
  - served (bool): Whether the coffee was served.
  - temperature_c (float): Served coffee temperature.
  - volume_ml (int): Served coffee volume in milliliters.

**Raises:**

- ValueError: Raised if `brewed_success` is False, indicating the coffee cannot be served.
**Examples:**

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

