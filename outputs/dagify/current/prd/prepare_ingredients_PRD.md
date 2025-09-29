# prepare_ingredients PRD

## Description
Prepare the ingredients according to the meal plan.


## Conceptual Info

This node prepares the ingredients for cooking based on the meal plan and purchased ingredients.

## Docstring

### Summary
Prepare ingredients by washing, chopping, and measuring them according to the meal plan.

### Parameters

- **meal_plan** (dict): Meal plan containing the meal name, ingredients, and cooking techniques. Expected to be the output of the 'plan_meal' node.
- **purchased_ingredients** (List[str]): List of ingredients that have been purchased. Expected to be the output of the 'purchase_ingredients' node.

### Returns

List[str]: List of prepared ingredients.

### Raises

- ValueError: If the meal plan is invalid or if purchased ingredients do not match the meal plan.

### Examples

```python
>>> meal_plan = {'meal_name': 'Salad', 'ingredients': ['Lettuce', 'Tomatoes'], 'cooking_techniques': []}
>>> purchased_ingredients = ['Lettuce', 'Tomatoes']
>>> prepared_ingredients = prepare_ingredients(meal_plan, purchased_ingredients)
['Washed Lettuce', 'Chopped Tomatoes']
```

```python
>>> meal_plan = {'meal_name': 'Soup', 'ingredients': ['Carrots', 'Potatoes'], 'cooking_techniques': ['Boiling']}
>>> purchased_ingredients = ['Carrots', 'Potatoes']
>>> prepared_ingredients = prepare_ingredients(meal_plan, purchased_ingredients)
['Chopped Carrots', 'Peeled and Chopped Potatoes']
```
