# process_shopping_ingredients PRD

## Description
Processes a list of ingredients to prepare them for shopping.


## Conceptual Info

This shim node takes a list of ingredients as input, processes them, and returns a list of ingredients ready for shopping.

## Docstring

### Summary
Process a list of ingredients for shopping by potentially cleaning, formatting, or transforming the input.

### Parameters

- **ingredients** (str): A string representing a list of ingredients that need to be processed for shopping.

### Returns

List[str]: A list of processed ingredients ready for shopping.

### Raises

- ValueError: If the input string is not properly formatted or contains invalid ingredients.
- TypeError: If the input is not a string.

### Examples

```python
>>> ingredients_str = 'milk, eggs, bread'
>>> processed_ingredients = process_shopping_ingredients(ingredients=ingredients_str)
['milk', 'eggs', 'bread']
```

```python
>>> ingredients_str = 'carrots: 1kg, apples: 3 pieces'
>>> processed_ingredients = process_shopping_ingredients(ingredients=ingredients_str)
['carrots - 1kg', 'apples - 3 pieces']
```
