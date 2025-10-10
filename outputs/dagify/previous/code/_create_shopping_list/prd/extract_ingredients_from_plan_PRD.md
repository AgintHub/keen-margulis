# extract_ingredients_from_plan PRD

## Description
Extracts a list of ingredients from a given meal plan string.


## Conceptual Info

This shim function is responsible for parsing a meal plan string and extracting a list of ingredients required for the meal. It plays a crucial role in the meal planning pipeline by providing the necessary ingredients for further processing, such as creating a shopping list.

## Docstring

### Summary
Extracts ingredients from a meal plan string and returns them as a list of strings.

### Parameters

- **meal_plan** (str): A string representing the meal plan from which ingredients are to be extracted.

### Returns

List[str]: A list of strings representing the ingredients extracted from the meal plan.

### Raises

- ValueError: If the input meal plan is empty or malformed.
- TypeError: If the input meal plan is not a string.

### Examples

```python
>>> meal_plan = 'Grilled chicken with roasted vegetables: chicken breast, olive oil, salt, pepper, carrots, broccoli' 
>>> extract_ingredients_from_plan(meal_plan)
['chicken breast', 'olive oil', 'salt', 'pepper', 'carrots', 'broccoli']
```

```python
>>> meal_plan = 'Pasta with tomato sauce: pasta, tomatoes, garlic, olive oil, basil' 
>>> extract_ingredients_from_plan(meal_plan)
['pasta', 'tomatoes', 'garlic', 'olive oil', 'basil']
```
