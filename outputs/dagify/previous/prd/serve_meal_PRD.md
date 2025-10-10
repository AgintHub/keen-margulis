# serve_meal PRD

## Description
Present the cooked meal in an appealing manner.


## Conceptual Info

The serve_meal node is responsible for presenting the cooked meal in an appealing manner, taking the cooked meal name as input from its parent node, cook_meal.

## Docstring

### Summary
Serves the cooked meal by taking the cooked meal name as input and returning the served meal name.

### Parameters

- **cooked_meal** (str): The name of the cooked meal, received from the cook_meal node.

### Returns

str: The name of the served meal.

### Raises

- ValueError: If the cooked meal name is empty or not a string.

### Examples

```python
>>> serve_meal('Grilled Chicken')
'Grilled Chicken'
```

```python
>>> serve_meal('Vegetable Soup')
'Vegetable Soup'
```
