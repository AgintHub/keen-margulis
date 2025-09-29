# apply_preparation_methods PRD

## Description
Applies various preparation methods to an ingredient based on the provided cooking techniques and returns the prepared ingredient.


## Conceptual Info

This shim function applies preparation methods to ingredients based on the required cooking techniques, playing a crucial role in the meal preparation workflow.

## Docstring

### Summary
Applies preparation methods to an ingredient based on the given cooking techniques.

### Parameters

- **ingredient** (str): The ingredient to be prepared.
- **methods** (str): A list of preparation methods to be applied to the ingredient.

### Returns

str: The prepared ingredient after applying the specified preparation methods.

### Raises

- ValueError: If the ingredient is empty or if the preparation methods are not provided.
- TypeError: If the ingredient is not a string or if the methods are not a list of strings.

### Examples

```python
>>> apply_preparation_methods(ingredient='carrot', methods='chop,peel')
>>> apply_preparation_methods(ingredient='onion', methods='dice')
>>> apply_preparation_methods(ingredient='potato', methods='peel,boil')
['chopped and peeled carrot', 'diced onion', 'peeled and boiled potato']
```

```python
>>> apply_preparation_methods(ingredient='', methods='chop')
ValueError: Ingredient cannot be empty
```
