# finalize_meal_name PRD

## Description
Finalizes the name of the cooked meal based on the cooked result.


## Conceptual Info

This shim function takes the cooked result from the cooking process and generates a final name for the meal, making it presentable and identifiable.

## Docstring

### Summary
Finalizes the name of the cooked meal based on the input cooked result.

### Parameters

- **cooked_result** (str): The result from the cooking process that needs to be finalized into a meal name.

### Returns

str: The finalized name of the cooked meal, ready for presentation.

### Raises

- ValueError: If the cooked result is empty or not a valid string.
- TypeError: If the input cooked result is not of type string.

### Examples

```python
>>> finalize_meal_name(cooked_result='Grilled chicken with spices')
'Spicy Grilled Chicken Delight'
```

```python
>>> finalize_meal_name(cooked_result='Vegetable stir-fry')
'Veggie Stir-Fry'
```
