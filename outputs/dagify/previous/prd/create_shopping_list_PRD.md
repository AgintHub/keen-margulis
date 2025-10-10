# create_shopping_list PRD

## Description
Generate a shopping list from the meal plan.


## Conceptual Info

This node generates a shopping list based on the ingredients required for the meal plan created by the 'plan_meal' node.

## Docstring

### Summary
Create a shopping list from the meal plan ingredients.

### Parameters

- **meal_plan** (dict): Meal plan details containing ingredients, meal name, and cooking techniques.

### Returns

List[str]: A list of ingredients to purchase for the meal.

### Raises

- KeyError: If 'ingredients' key is missing from the meal plan.
- TypeError: If the meal plan is not a dictionary or if ingredients is not a list.

### Examples

```python
>>> meal_plan = {'meal_name': 'Pasta', 'ingredients': ['pasta', 'sauce', 'cheese'], 'cooking_techniques': ['boiling', 'heating']}
>>> shopping_list = create_shopping_list(meal_plan)
>>> print(shopping_list)
['pasta', 'sauce', 'cheese']
```

```python
>>> meal_plan = {'meal_name': 'Salad', 'ingredients': ['lettuce', 'tomatoes', 'cucumber'], 'cooking_techniques': []}
>>> shopping_list = create_shopping_list(meal_plan)
>>> print(shopping_list)
['lettuce', 'tomatoes', 'cucumber']
```
