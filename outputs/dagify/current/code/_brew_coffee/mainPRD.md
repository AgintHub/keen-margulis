# _brew_coffee - Complete PRD Documentation

## Overview
PRDs for nodes in the '_brew_coffee' module.

## Table of Contents

- [validate_brewing_readiness](#validate_brewing_readiness)

- [get_current_timestamp](#get_current_timestamp)

- [calculate_brewing_parameters](#calculate_brewing_parameters)

- [execute_brewing_process](#execute_brewing_process)

- [calculate_duration_seconds](#calculate_duration_seconds)

- [measure_final_temperature](#measure_final_temperature)

- [calculate_brewed_volume](#calculate_brewed_volume)



---

## validate_brewing_readiness

### Description
Validate that boiled water and a ready coffee maker satisfy brewing prerequisites and return a status message.

### Conceptual Info

Ensures that the brewing process only starts when the water has reached boiling point and the coffee maker is prepared, providing clear feedback for downstream nodes.

### Docstring

**Summary:** Validate the readiness of the brewing setup before starting coffee production.

**Parameters:**

- water_status (BoilWaterOutput): Object containing boiled status, temperature, and boil time of the water.
- coffee_maker_status (PrepareCoffeeMakerOutput): Object containing coffee grounds amount, filter preparation flag, and overall maker status.
**Returns:** str - A human‑readable string indicating whether brewing can proceed or why it cannot.

**Raises:**

- ValueError: Raised when the water is not boiled, the filter is not prepared, or the coffee maker status is not 'ready'.
- TypeError: Raised when the provided arguments are not instances of BoilWaterOutput and PrepareCoffeeMakerOutput.
**Examples:**

```python
>>> from pydantic import BaseModel, Field
>>> class BoilWaterOutput(BaseModel):
...     boiled: bool
...     temperature_celsius: float
...     boil_time_seconds: int
>>> class PrepareCoffeeMakerOutput(BaseModel):
...     coffee_grounds_amount_g: float
...     filter_prepared: bool
...     coffee_maker_status: str
>>> water = BoilWaterOutput(boiled=True, temperature_celsius=100, boil_time_seconds=60)
>>> maker = PrepareCoffeeMakerOutput(coffee_grounds_amount_g=15.0, filter_prepared=True, coffee_maker_status='ready')
>>> print(validate_brewing_readiness(water_status=water, coffee_maker_status=maker))
'Ready to brew'
```

```python
>>> water_bad = BoilWaterOutput(boiled=False, temperature_celsius=90, boil_time_seconds=30)
>>> print(validate_brewing_readiness(water_status=water_bad, coffee_maker_status=maker))
ValueError: Water is not boiled or coffee maker not ready.
```



---

## get_current_timestamp

### Description
Returns the current UTC timestamp as an ISO 8601 string.

### Conceptual Info

Provides a consistent, timezone‑aware timestamp for use in workflow steps that require a point in time.

### Docstring

**Summary:** Return the current UTC time formatted as an ISO 8601 string.

**Returns:** str - ISO 8601 formatted string representing the current UTC timestamp.

**Raises:**

- TypeError: If arguments are passed to the function.
**Examples:**

```python
>>> timestamp = get_current_timestamp()
>>> print(timestamp)
"2025-10-11T12:34:56+00:00"
```

```python
>>> print(get_current_timestamp())
"2025-10-11T12:34:56+00:00"
```



---

## calculate_brewing_parameters

### Description
Calculates brewing parameters such as target brew temperature, brew duration, and filter flow rate from the input water temperature and coffee grounds amount.

### Conceptual Info

This shim computes the optimal brewing settings required for a coffee maker to produce a consistent cup of coffee, taking into account the initial water temperature and the amount of coffee grounds. It serves as a bridge between raw sensor inputs and the brewing execution logic.

### Docstring

**Summary:** Compute brewing parameters for coffee based on water temperature and coffee grounds amount.

**Parameters:**

- water_temp (str): Water temperature in degrees Celsius represented as a string (e.g., "90").
- coffee_amount (str): Amount of coffee grounds in grams represented as a string (e.g., "20").
**Returns:** str - A JSON-formatted string describing the brewing parameters. The dictionary contains keys such as `target_temperature_c`, `brew_time_seconds`, and `filter_flow_rate`.

**Raises:**

- ValueError: Raised when the string inputs cannot be converted to positive floats.
- TypeError: Raised when the inputs are not of type string.
**Examples:**

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



---

## execute_brewing_process

### Description
Executes the coffee brewing process and returns a boolean indicating success.

### Conceptual Info

The execute_brewing_process shim orchestrates the brewing step by validating water and coffee maker inputs, applying brewing parameters, and returning a success flag that determines downstream coffee output.

### Docstring

**Summary:** Executes the coffee brewing process for a given set of inputs and returns a boolean indicating whether the brewing was successful.

**Parameters:**

- water_input (str): A JSON‑encoded string containing boiled water information (temperature, boiled status, etc.).
- coffee_maker_input (str): A JSON‑encoded string containing coffee maker status and grounds amount.
- parameters (str): A JSON‑encoded string of brewing parameters such as brew time and coffee‑to‑water ratio.
**Returns:** bool - True if the brewing process completed successfully; otherwise False.

**Raises:**

- ValueError: Raised when any of the input JSON strings is missing required fields or contains invalid values.
- TypeError: Raised when any of the input parameters is not a string.
**Examples:**

```python
>>> water_input = '{"boiled": true, "temperature_celsius": 100}'
>>> coffee_maker_input = '{"coffee_grounds_amount_g": 20, "filter_prepared": true, "coffee_maker_status": "ready"}'
>>> parameters = '{"brew_time_seconds": 240}'
>>> success = execute_brewing_process(water_input, coffee_maker_input, parameters)
>>> print(success)
True
```

```python
>>> water_input = '{"boiled": false, "temperature_celsius": 85}'
>>> coffee_maker_input = '{"coffee_grounds_amount_g": 20, "filter_prepared": true, "coffee_maker_status": "ready"}'
>>> parameters = '{"brew_time_seconds": 240}'
>>> try:
...     execute_brewing_process(water_input, coffee_maker_input, parameters)
>>> except ValueError as e:
...     print(str(e))
"Boiled water required for brewing"
```



---

## calculate_duration_seconds

### Description
Calculates the elapsed duration in seconds between a start and end ISO 8601 timestamp.

### Conceptual Info

This shim provides precise timing by computing the number of seconds that elapse between a given start and end timestamp, enabling accurate duration tracking in the brewing workflow.

### Docstring

**Summary:** Computes the elapsed time in seconds between two ISO 8601 timestamps.

**Parameters:**

- start_time (str): The start timestamp in ISO 8601 format.
- end_time (str): The end timestamp in ISO 8601 format.
**Returns:** float - The duration in seconds between start_time and end_time.

**Raises:**

- ValueError: If end_time is earlier than start_time or if timestamps cannot be parsed.
- TypeError: If either start_time or end_time is not a string.
**Examples:**

```python
>>> duration = calculate_duration_seconds('2023-01-01T12:00:00Z', '2023-01-01T12:05:00Z')
>>> duration
300.0
```

```python
>>> calculate_duration_seconds('2023-01-01T12:05:00Z', '2023-01-01T12:00:00Z')
ValueError: End time must be after start time.
```



---

## measure_final_temperature

### Description
Calculates the final temperature of brewed coffee based on the success flag and the initial water temperature.

### Conceptual Info

The shim simulates the physical cooling of brewed coffee. It receives the brewing success status and the initial temperature of the boiled water, and returns a float representing the temperature of the coffee once brewing completes. The calculation is intentionally simple to allow future refinement.

### Docstring

**Summary:** Return the final temperature of brewed coffee based on whether the brewing process succeeded and the initial temperature of the boiled water.

**Parameters:**

- success (str): Indicates if the brewing process completed successfully. Expected values are the string literals "True" or "False".
- initial_temp (str): The temperature of the boiled water in degrees Celsius, provided as a numeric string.
**Returns:** float - The final temperature of the brewed coffee in degrees Celsius. If the brew was successful, the temperature is calculated as `float(initial_temp) - 15.0`. If unsuccessful, it defaults to `0.0`.

**Raises:**

- ValueError: Raised when `success` is not "True" or "False", or when `initial_temp` cannot be converted to a float.
- TypeError: Raised when `success` or `initial_temp` is not of type `str`.
**Examples:**

```python
>>> output = measure_final_temperature('True', '100')
>>> print(output)
85.0
```

```python
>>> output = measure_final_temperature('False', '90')
>>> print(output)
0.0
```



---

## calculate_brewed_volume

### Description
Calculates the number of coffee cups that can be brewed from a given amount of coffee grounds.

### Conceptual Info

The shim determines how many standard cups of coffee can be produced from a specified amount of coffee grounds, enabling downstream logic to anticipate volume and resource usage.

### Docstring

**Summary:** Returns the number of standard cups of coffee that can be brewed from the given coffee amount in grams.

**Parameters:**

- coffee_amount (str): String representation of the coffee grounds weight in grams.
**Returns:** int - Integer count of coffee cups that can be brewed.

**Raises:**

- ValueError: Raised when the coffee_amount cannot be converted to a positive numeric value.
- TypeError: Raised when coffee_amount is not a string.
**Examples:**

```python
>>> calculate_brewed_volume('7.5')
1
```

```python
>>> calculate_brewed_volume('15')
2
```

