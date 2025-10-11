# validate_brewing_readiness PRD

## Description
Validate that boiled water and a ready coffee maker satisfy brewing prerequisites and return a status message.


## Conceptual Info

Ensures that the brewing process only starts when the water has reached boiling point and the coffee maker is prepared, providing clear feedback for downstream nodes.

## Docstring

### Summary
Validate the readiness of the brewing setup before starting coffee production.

### Parameters

- **water_status** (BoilWaterOutput): Object containing boiled status, temperature, and boil time of the water.
- **coffee_maker_status** (PrepareCoffeeMakerOutput): Object containing coffee grounds amount, filter preparation flag, and overall maker status.

### Returns

str: A human‑readable string indicating whether brewing can proceed or why it cannot.

### Raises

- ValueError: Raised when the water is not boiled, the filter is not prepared, or the coffee maker status is not 'ready'.
- TypeError: Raised when the provided arguments are not instances of BoilWaterOutput and PrepareCoffeeMakerOutput.

### Examples

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
