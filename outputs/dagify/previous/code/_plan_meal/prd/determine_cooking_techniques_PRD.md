# determine_cooking_techniques PRD

## Description
This shim determines the cooking techniques required based on the input recipe.


## Conceptual Info

This shim analyzes a given recipe to identify the necessary cooking techniques, playing a crucial role in meal planning by providing essential cooking information.

## Docstring

### Summary
Determines the cooking techniques required for a given recipe.

### Parameters

- **recipe** (str): A string representing the recipe to analyze.

### Returns

list[str]: A list of strings representing the cooking techniques required.

### Raises

- ValueError: If the input recipe is empty or malformed.
- TypeError: If the input recipe is not a string.

### Examples

```python
>>> recipe = 'Grilled Chicken with Roasted Vegetables'
>>> cooking_techniques = determine_cooking_techniques(recipe)
>>> print(cooking_techniques)
['Grilling', 'Roasting']
```

```python
>>> recipe = 'Pan-Seared Salmon with Quinoa'
>>> cooking_techniques = determine_cooking_techniques(recipe)
>>> print(cooking_techniques)
['Pan-Sealing', 'Boiling']
```
