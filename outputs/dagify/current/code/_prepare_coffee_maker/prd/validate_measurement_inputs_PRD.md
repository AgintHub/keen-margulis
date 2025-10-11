# validate_measurement_inputs PRD

## Description
Checks that a measurement is flagged as valid and the ground amount is positive, returning a success message or raising an error.


## Conceptual Info

This shim validates the inputs from the coffee measuring step before allowing the coffee maker to proceed, ensuring that only correct and meaningful data is passed downstream.

## Docstring

### Summary
Validates measurement inputs for coffee preparation.

### Parameters

- **measurement_valid** (bool): True if the measurement was performed correctly, otherwise False.
- **ground_amount_grams** (float): Amount of coffee grounds measured in grams.

### Returns

str: A status message confirming that the inputs are valid.

### Raises

- ValueError: Raised when measurement_valid is False or ground_amount_grams is not a positive number.
- TypeError: Raised when measurement_valid is not a bool or ground_amount_grams is not a numeric type.

### Examples

```python
>>> result = validate_measurement_inputs(measurement_valid=True, ground_amount_grams=20.5)
>>> print(result)
Inputs are valid
```

```python
>>> validate_measurement_inputs(measurement_valid=False, ground_amount_grams=10)
ValueError: Measurement is marked invalid.
```
