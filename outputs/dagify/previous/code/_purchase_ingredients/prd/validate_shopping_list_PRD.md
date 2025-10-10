# validate_shopping_list PRD

## Description
Validates a given shopping list and returns a list of valid items.


## Conceptual Info

This shim node is responsible for validating a shopping list, ensuring it contains appropriate and valid items for purchase.

## Docstring

### Summary
Validates the input shopping list and returns a list of valid shopping items.

### Parameters

- **shopping_list** (str): The input shopping list as a string, expected to be a comma-separated list of ingredients.

### Returns

List[str]: A list of valid shopping items after validation.

### Raises

- ValueError: If the input shopping list is empty or contains invalid items.
- TypeError: If the input shopping list is not a string.

### Examples

```python
>>> validate_shopping_list(shopping_list='apples,bananas,oranges')
['apples', 'bananas', 'oranges']
```

```python
>>> validate_shopping_list(shopping_list='apples,,oranges')
['apples', 'oranges']
```
