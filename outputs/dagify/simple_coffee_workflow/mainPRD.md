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
Simulates heating a supplied liquid (water, milk, tea, etc.) to its boiling point, recording the temperature reached, the duration of heating, and whether the liquid is ready for use in downstream processes.

### Conceptual Info

The boil_liquid node is a core thermodynamic simulation step that transforms any input liquid into a ready‑to‑use state for brewing, cooking, or analytical processes. It abstracts the physics of heating while providing measurable metrics that downstream nodes can leverage for timing, quality control, and safety checks.

### Docstring

**Summary:** Heats a liquid to its boiling point and returns the readiness status, final temperature, and heating duration.

**Parameters:**

- liquid_type (str): Name of the liquid to be boiled (e.g., "water", "milk", "tea").
- volume (float): Volume of the liquid in liters.
**Returns:** dict - Dictionary containing `boiled` (bool), `temperature_celsius` (float), and `boil_time_seconds` (int).

**Raises:**

- ValueError: Raised if an unsupported liquid type is provided.
- RuntimeError: Raised if the heating simulation fails to converge within realistic limits.
**Examples:**

```python
>>> result = boil_liquid(liquid_type='water', volume=0.5)
>>> print(result)
{'boiled': True, 'temperature_celsius': 100.0, 'boil_time_seconds': 90}
```



---

## brew_coffee

### Description
Simulates heating a liquid (water, tea, or any beverage base) to its boiling point, measuring the duration taken and confirming readiness for downstream brewing or processing steps.

### Conceptual Info

The boil_any_liquid node models the physical process of heating a liquid to its boiling point, capturing key performance metrics such as time, temperature, and success status to inform subsequent brewing stages.

### Docstring

**Summary:** Boil the specified liquid to its target boiling temperature and report readiness metrics.

**Parameters:**

- target_temperature_celsius (float): Desired boiling temperature for the liquid in degrees Celsius.
**Returns:** dict - Dictionary containing boiled status, temperature, and boil time.

**Raises:**

- ValueError: Raised if the liquid fails to reach the target temperature within the allowed timeframe.
**Examples:**

```python
>>> result = boil_any_liquid(target_temperature_celsius=100.0)
>>> print(result['boiled'], result['temperature_celsius'], result['boil_time_seconds'])
True 100.0 45
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

