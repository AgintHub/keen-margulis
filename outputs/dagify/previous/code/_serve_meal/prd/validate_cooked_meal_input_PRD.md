# validate_cooked_meal_input PRD

## Description
Validates the input for a cooked meal to ensure it meets certain criteria.


## Conceptual Info

This shim node is responsible for validating the input related to a cooked meal, ensuring that it conforms to expected standards or formats.

## Docstring

### Summary
Validates the input for a cooked meal.

### Parameters

- **meal_name** (str): The name of the cooked meal to be validated.

### Returns

str: A validation message indicating whether the meal name is valid.

### Raises

- ValueError: If the meal name is empty or does not match expected patterns.
- TypeError: If the meal name is not a string.

### Examples

```python
>>> validate_cooked_meal_input(meal_name='Grilled Chicken')
'Valid meal name'
```

```python
>>> validate_cooked_meal_input(meal_name='')
ValueError: 'Meal name cannot be empty'
```
