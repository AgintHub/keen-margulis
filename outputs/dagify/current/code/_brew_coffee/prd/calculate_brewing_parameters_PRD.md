# calculate_brewing_parameters PRD

## Description
Calculates brewing parameters such as target brew temperature, brew duration, and filter flow rate from the input water temperature and coffee grounds amount.


## Conceptual Info

This shim computes the optimal brewing settings required for a coffee maker to produce a consistent cup of coffee, taking into account the initial water temperature and the amount of coffee grounds. It serves as a bridge between raw sensor inputs and the brewing execution logic.

## Docstring

### Summary
Compute brewing parameters for coffee based on water temperature and coffee grounds amount.

### Parameters

- **water_temp** (str): Water temperature in degrees Celsius represented as a string (e.g., "90").
- **coffee_amount** (str): Amount of coffee grounds in grams represented as a string (e.g., "20").

### Returns

str: A JSON-formatted string describing the brewing parameters. The dictionary contains keys such as `target_temperature_c`, `brew_time_seconds`, and `filter_flow_rate`.

### Raises

- ValueError: Raised when the string inputs cannot be converted to positive floats.
- TypeError: Raised when the inputs are not of type string.

### Examples

```python
>>> from calculate_brewing_parameters import calculate_brewing_parameters
>>> # Example 1: Typical brewing scenario
>>> params = calculate_brewing_parameters(water_temp="93", coffee_amount="18")
>>> print(params)
"{\"target_temperature_c\": 93, \"brew_time_seconds\": 240, \"filter_flow_rate\": \"medium\"}"
```

```python
>>> # Example 2: Error handling – non‑numeric input
>>> try:
...     calculate_brewing_parameters(water_temp="hot", coffee_amount="20")
>>> except ValueError as e:
...     print(e)
"Invalid numeric value for water_temp: 'hot'"
```
