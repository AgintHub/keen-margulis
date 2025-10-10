# identify_ingredients PRD

## Description
Extracts and identifies ingredients from a given recipe.


## Conceptual Info

This shim function is designed to parse a given recipe and extract the list of ingredients required for it.

## Docstring

### Summary
Identifies and returns a list of ingredients from the provided recipe.

### Parameters

- **recipe** (str): The input recipe in string format from which ingredients will be extracted.

### Returns

list[str]: A list of ingredients required for the recipe.

### Raises

- ValueError: If the input recipe is empty or not in the expected format.
- TypeError: If the input recipe is not a string.

### Examples

```python
>>> recipe = 'To make a cake, you need: flour, sugar, eggs.'
>>> ingredients = identify_ingredients(recipe=recipe)
['flour', 'sugar', 'eggs']
```

```python
>>> recipe = 'Ingredients for salad: lettuce, tomatoes, cucumbers.'
>>> ingredients = identify_ingredients(recipe=recipe)
['lettuce', 'tomatoes', 'cucumbers']
```
