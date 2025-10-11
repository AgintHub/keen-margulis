# _boil_water - Complete PRD Documentation

## Overview
PRDs for nodes in the '_boil_water' module.

## Table of Contents

- [extract_liquid_type](#extract_liquid_type)

- [extract_volume](#extract_volume)

- [validate_liquid_type](#validate_liquid_type)

- [get_boiling_point](#get_boiling_point)

- [get_heat_capacity](#get_heat_capacity)

- [simulate_heating_process](#simulate_heating_process)

- [check_boiling_status](#check_boiling_status)



---

## extract_liquid_type

### Description
Extracts the liquid type from a given input string, ignoring any volume or additional information.

### Conceptual Info

This shim encapsulates the logic for parsing a liquid type from arbitrary input strings, providing a standardized, validated output that other nodes can rely upon.

### Docstring

**Summary:** Extracts the liquid type from a general input string, returning a standardized lowercase string.

**Parameters:**

- general_input (str): The raw input string that may contain a liquid type followed by additional descriptors such as volume or units.
- kwargs (str): Additional keyword arguments in string form; currently unused but retained for API compatibility.
**Returns:** str - The liquid type extracted from the input, lowercased. Example: 'water', 'coffee', 'milk'.

**Raises:**

- ValueError: Raised when the liquid type cannot be determined from the input.
- TypeError: Raised when either `general_input` or `kwargs` is not a string.
**Examples:**

```python
>>> print(extract_liquid_type('Water 500ml', {}))
'water'
```

```python
>>> print(extract_liquid_type('Coffee 300ml', {}))
'coffee'
```



---

## extract_volume

### Description
Extracts a numeric volume value from the provided general input string and keyword arguments.

### Conceptual Info

The extract_volume shim parses textual or structured inputs to retrieve a numeric volume measure, enabling downstream processes to quantify liquid quantities accurately.

### Docstring

**Summary:** Extracts a numeric volume value from a string or keyword arguments.

**Parameters:**

- general_input (str): A string containing the volume information, e.g., '2L of water' or '1.5 liters'.
- kwargs (dict): Optional keyword arguments that may supply the unit or override default parsing behaviour (e.g., unit='liters').
**Returns:** float - The numeric volume value expressed in liters.

**Raises:**

- ValueError: Raised when no numeric volume can be extracted or when the unit is unsupported.
- TypeError: Raised when general_input is not a string or kwargs is not a dictionary.
**Examples:**

```python
>>> extract_volume('water 2L')
2.0
```

```python
>>> extract_volume('1.5 liters of water', unit='liters')
1.5
```



---

## validate_liquid_type

### Description
Validates whether a given liquid type is supported for boiling simulation.

### Conceptual Info

This shim ensures the boiling simulation receives only liquid types that have defined physical properties (boiling point and heat capacity). It serves as a gatekeeper before any thermodynamic calculations are performed.

### Docstring

**Summary:** Determines if the supplied liquid type is among the supported set for boiling simulation.

**Parameters:**

- liquid_type (str): Name of the liquid (e.g., 'water', 'coffee', 'milk').
**Returns:** bool - True if the liquid_type is supported, False otherwise.

**Raises:**

- TypeError: If liquid_type is not a string.
- ValueError: If liquid_type is an empty string or contains only whitespace.
**Examples:**

```python
>>> result = validate_liquid_type('water')
>>> print(result)
True
```

```python
>>> result = validate_liquid_type('coffee')
>>> print(result)
False
```

```python
>>> validate_liquid_type(123)
>>> print('This line will not be reached')
Traceback (most recent call last):\n  File "<stdin>", line 1, in <module>\nTypeError: liquid_type must be a string
```



---

## get_boiling_point

### Description
Returns the standard boiling point in degrees Celsius for a given liquid type.

### Conceptual Info

The get_boiling_point shim encapsulates the logic for retrieving a liquid’s standard boiling point, serving as a lookup utility that other nodes, such as boil_water, can depend on to perform temperature‑based calculations.

### Docstring

**Summary:** Return the standard boiling point of a liquid in degrees Celsius.

**Parameters:**

- liquid_type (str): The name of the liquid (e.g., 'water', 'ethanol').
**Returns:** float - The boiling point of the specified liquid in degrees Celsius.

**Raises:**

- ValueError: Raised when the supplied liquid_type is not supported.
- TypeError: Raised when liquid_type is not a string.
**Examples:**

```python
>>> get_boiling_point('water')
100.0
```

```python
>>> get_boiling_point('ethanol')
78.37
```



---

## get_heat_capacity

### Description
Retrieves the specific heat capacity (in J/(kg·K)) of a specified liquid at a standard temperature.

### Conceptual Info

This shim provides a lookup for the specific heat capacity of common brewing liquids, enabling downstream temperature simulations to use accurate thermal properties.

### Docstring

**Summary:** Return the specific heat capacity of a given liquid.

**Parameters:**

- liquid_type (str): Name of the liquid (e.g., 'water', 'ethanol').
**Returns:** float - Heat capacity of the liquid in J/(kg·K).

**Raises:**

- ValueError: Raised when the specified liquid type is not supported.
- TypeError: Raised when liquid_type is not a string.
**Examples:**

```python
>>> from get_heat_capacity import get_heat_capacity
>>> print(get_heat_capacity('water'))
4186.0
```

```python
>>> print(get_heat_capacity('ethanol'))
2420.0
```



---

## simulate_heating_process

### Description
Simulates the heating of a liquid until it reaches a target temperature and returns the simulation results as a JSON string.

### Conceptual Info

This shim encapsulates the physics of heating a liquid, modeling how the temperature rises over time given its volume and specific heat capacity. The simulation returns whether it converged, the final temperature reached, and the time taken, allowing downstream nodes to decide brewing readiness.

### Docstring

**Summary:** Simulate heating a liquid until it reaches a specified temperature.

**Parameters:**

- volume (str): String representation of the liquid volume in liters.
- target_temperature (str): String representation of the desired final temperature in degrees Celsius.
- heat_capacity (str): String representation of the specific heat capacity in J/(kg·K).
**Returns:** str - A JSON string containing three keys:
- 'converged' (bool): True if the simulation reached the target temperature within realistic limits.
- 'final_temperature' (float): The temperature achieved at the end of the simulation.
- 'time_seconds' (int): The number of seconds required to reach the target temperature.

**Raises:**

- ValueError: Raised when volume or target_temperature is negative or zero, or if heat_capacity is non‑positive.
- TypeError: Raised if any input is not a string that can be converted to a numeric value.
**Examples:**

```python
>>> simulate_heating_process(volume='0.5', target_temperature='100', heat_capacity='4184')
{'converged': True, 'final_temperature': 100.0, 'time_seconds': 300}
```

```python
>>> simulate_heating_process(volume='2', target_temperature='60', heat_capacity='4184')
{'converged': True, 'final_temperature': 60.0, 'time_seconds': 150}
```



---

## check_boiling_status

### Description
Check whether the supplied temperature has reached or exceeded the boiling point.

### Conceptual Info

Determines whether a liquid has reached its boiling point based on its current temperature and the known boiling point for that liquid, providing a boolean result that drives subsequent brewing logic.

### Docstring

**Summary:** Determine if a liquid has reached its boiling point.

**Parameters:**

- temperature (float): Current temperature of the liquid in degrees Celsius.
- boiling_point (float): Boiling point temperature of the liquid in degrees Celsius.
**Returns:** bool - True if temperature is greater than or equal to boiling_point; otherwise False.

**Raises:**

- ValueError: Raised when temperature or boiling_point is negative.
- TypeError: Raised when either temperature or boiling_point is not a numeric type.
**Examples:**

```python
>>> check_boiling_status(temperature=100.0, boiling_point=100.0)
True
```

```python
>>> check_boiling_status(temperature=90.0, boiling_point=100.0)
False
```

