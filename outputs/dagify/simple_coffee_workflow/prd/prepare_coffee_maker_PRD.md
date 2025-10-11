# prepare_coffee_maker PRD

## Description
Prepare the coffee maker


## Conceptual Info

Prepares the coffee maker by loading the measured coffee grounds into the filter, verifying filter readiness, and reporting the status of the coffee maker.

## Docstring

### Summary
Adds the specified amount of coffee grounds into the coffee maker's filter, validates the measurement, and reports the amount added, filter status, and overall maker status.

### Parameters

- **ground_amount_grams** (float): Amount of coffee grounds measured in grams (from measure_coffee).
- **desired_cup_count** (int): Number of coffee cups to be brewed (from measure_coffee).
- **grounds_type** (str): Type of coffee grounds used (e.g., medium grind, dark roast).
- **measurement_valid** (bool): Flag indicating whether the measurement was performed correctly.

### Returns

dict: Dictionary with keys `coffee_grounds_amount_g` (float), `filter_prepared` (bool), and `coffee_maker_status` (str).

### Raises

- ValueError: If `measurement_valid` is False or `ground_amount_grams` is non‑positive.

### Examples

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
