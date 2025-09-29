# extract_meal_name PRD

## Description
Extracts the meal name from a given recipe string.


## Conceptual Info

This shim function is designed to extract the meal name from a given recipe string, playing a crucial role in meal planning by identifying the name of the meal to be prepared.

## Docstring

### Summary
Extracts the meal name from a recipe string.

### Parameters

- **recipe** (str): The recipe string containing the meal information.

### Returns

str: The extracted meal name.

### Raises

- ValueError: If the recipe string is empty or does not contain a valid meal name.
- TypeError: If the input recipe is not of type string.

### Examples

```python
>>> extract_meal_name(recipe='Chicken Parmesan Recipe')
'Chicken Parmesan'
```

```python
>>> extract_meal_name(recipe='{ "meal_name": "Beef Stew" }')
'Beef Stew'
```
