# _serve_coffee - Complete PRD Documentation

## Overview
PRDs for nodes in the '_serve_coffee' module.

## Table of Contents

- [verify_brewing_success](#verify_brewing_success)

- [convert_cups_to_ml](#convert_cups_to_ml)

- [simulate_pour_coffee](#simulate_pour_coffee)



---

## verify_brewing_success

### Description
Verifies whether the brewing process was successful and returns a status string.

### Conceptual Info

This shim checks the brewing success flag and provides a human‑readable status message, allowing downstream nodes to act accordingly.

### Docstring

**Summary:** Check brewing success and return a status message.

**Parameters:**

- brewed_success (bool): Boolean indicating if the brewing process completed successfully.
**Returns:** str - A message: 'Brewing succeeded' when brewed_success is True, otherwise 'Brewing failed'.

**Raises:**

- ValueError: If brewed_success is None.
- TypeError: If brewed_success is not a boolean.
**Examples:**

```python
>>> verify_brewing_success(brewed_success=True)
'Brewing succeeded'
```

```python
>>> verify_brewing_success(brewed_success=False)
'Brewing failed'
```



---

## convert_cups_to_ml

### Description
Converts a given volume in cups to its equivalent in milliliters.

### Conceptual Info

This shim provides a standardized conversion from cups to milliliters, enabling the coffee brewing system to express volumes in metric units for consistency.

### Docstring

**Summary:** Converts a volume measurement from cups to milliliters using the standard conversion factor of 236.588 ml per cup.

**Parameters:**

- volume_cups (int): The number of cups to be converted; must be a non‑negative integer.
**Returns:** int - The equivalent volume in milliliters, rounded to the nearest integer.

**Raises:**

- ValueError: Raised if `volume_cups` is negative.
- TypeError: Raised if `volume_cups` is not an integer.
**Examples:**

```python
>>> convert_cups_to_ml(2)
473
```

```python
>>> convert_cups_to_ml(0)
0
```



---

## simulate_pour_coffee

### Description
Simulates the temperature of coffee after it is poured into a cup and returns the resulting temperature in degrees Celsius.

### Conceptual Info

This shim models the heat loss that occurs when coffee is poured from a pot into a cup, providing a realistic temperature for downstream nodes that handle serving or consuming the coffee.

### Docstring

**Summary:** Simulates the temperature of coffee after pouring into a cup.

**Parameters:**

- temperature_c (float): The temperature of the coffee before pouring, expressed in degrees Celsius.
**Returns:** float - The temperature of the coffee after pouring, in degrees Celsius.

**Raises:**

- ValueError: Raised when the input temperature is outside the physically realistic range of -10°C to 100°C.
- TypeError: Raised when the input temperature is not a float or int.
**Examples:**

```python
>>> simulate_pour_coffee(temperature_c=95.0)
90.0
```

```python
>>> simulate_pour_coffee(temperature_c=60.0)
58.0
```

