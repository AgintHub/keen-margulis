# measure_coffee PRD

## Description
Measure the coffee grounds


## Conceptual Info

The `measure_coffee` node calculates the required quantity of coffee grounds based on user-provided cup count and grounds type, ensuring the measurement is valid before the grounds are transferred to the coffee maker.

## Docstring

### Summary
Calculate and verify the amount of coffee grounds needed for a given number of cups.

### Parameters

- **desired_cup_count** (int): The target number of coffee cups to brew.
- **grounds_type** (str): The type of coffee grounds (e.g., 'medium grind', 'dark roast').

### Returns

dict: Dictionary containing `ground_amount_grams` (float), `desired_cup_count` (int), `grounds_type` (str), and `measurement_valid` (bool).

### Raises

- ValueError: If `desired_cup_count` is not a positive integer or `grounds_type` is not among the supported types.

### Examples

```python
>>> measure_coffee(3, 'medium grind')
{'ground_amount_grams': 18.0, 'desired_cup_count': 3, 'grounds_type': 'medium grind', 'measurement_valid': True}
```

```python
>>> measure_coffee(0, 'dark roast')
ValueError: desired_cup_count must be a positive integer.
```
