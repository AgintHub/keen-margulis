# check_ingredient_availability PRD

## Description
Checks the availability of ingredients in the given list.


## Conceptual Info

This shim function is designed to verify the availability of ingredients. It takes a list of ingredients as input and returns a list of ingredients that are available.

## Docstring

### Summary
Checks the availability of ingredients in the given list.

### Parameters

- **ingredients** (str): Comma-separated list of ingredients to check for availability.

### Returns

List[str]: List of available ingredients from the input list.

### Raises

- ValueError: When the input is not a valid list of ingredients.
- TypeError: When the input type is not str.

### Examples

```python
>>> available_ingredients = check_ingredient_availability(ingredients='flour,sugar,eggs')
>>> print(available_ingredients)
['flour', 'sugar']
```

```python
>>> available_ingredients = check_ingredient_availability(ingredients='milk,butter,salt')
>>> print(available_ingredients)
['milk', 'salt']
```
