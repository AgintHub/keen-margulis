# cook_meal PRD

## Description
Cook the meal according to the planned recipe.


## Conceptual Info

This node is responsible for cooking a meal based on the prepared ingredients and previously identified cooking techniques.

## Docstring

### Summary
Cooks a meal using the prepared ingredients and identified cooking techniques.

### Parameters

- **prepared_ingredients** (List[str]): List of ingredients that have been prepared for cooking.
- **cooking_techniques** (List[str]): List of cooking techniques required for the meal, derived from the meal plan.

### Returns

str: The name of the meal that has been cooked.

### Raises

- ValueError: If the prepared ingredients are not sufficient for cooking the meal.
- TypeError: If the cooking techniques are not provided or are of incorrect type.

### Examples

```python
>>> prepared_ingredients = ['chopped onions', 'minced garlic', 'sliced chicken']
>>> cooking_techniques = ['grilling', 'sauteing']
>>> cooked_meal = cook_meal(prepared_ingredients, cooking_techniques)
'Grilled Chicken'
```
