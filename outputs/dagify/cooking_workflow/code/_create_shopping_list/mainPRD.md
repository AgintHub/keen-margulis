# _create_shopping_list - Complete PRD Documentation

## Overview
PRDs for nodes in the '_create_shopping_list' module.

## Table of Contents

- [validate_meal_plan_input](#validate_meal_plan_input)

- [extract_ingredients_from_plan](#extract_ingredients_from_plan)

- [process_shopping_ingredients](#process_shopping_ingredients)



---

## validate_meal_plan_input

### Description
Validates the meal plan input to ensure it meets the required format and structure for further processing.

### Conceptual Info

This shim node is responsible for validating the meal plan input, ensuring it conforms to the expected structure and format before it is used in subsequent processing steps.

### Docstring

**Summary:** Validates meal plan input to ensure it is correctly formatted and structured.

**Parameters:**

- meal_plan (str): The meal plan input to be validated, expected to be a string representation that needs to be verified against the required format.
**Returns:** str - The validated meal plan input, returned as a string in the required format for further processing.

**Raises:**

- ValueError: If the meal plan input is not in the correct format or fails validation checks.
- TypeError: If the input type is not as expected (i.e., not a string).
**Examples:**

```python
>>> from pydantic import BaseModel
>>> class PlanMealOutput(BaseModel):
...     meal_name: str
...     ingredients: str
...     cooking_techniques: str
>>> plan_meal_input = PlanMealOutput(meal_name='Grilled Chicken', ingredients='Chicken, Salt, Pepper', cooking_techniques='Grilling')
>>> validated_input = validate_meal_plan_input(meal_plan=plan_meal_input.json())
{'meal_name': 'Grilled Chicken', 'ingredients': 'Chicken, Salt, Pepper', 'cooking_techniques': 'Grilling'}
```

```python
>>> validate_meal_plan_input(meal_plan='Invalid input')
ValueError: Invalid meal plan input format
```



---

## extract_ingredients_from_plan

### Description
Extracts a list of ingredients from a given meal plan string.

### Conceptual Info

This shim function is responsible for parsing a meal plan string and extracting a list of ingredients required for the meal. It plays a crucial role in the meal planning pipeline by providing the necessary ingredients for further processing, such as creating a shopping list.

### Docstring

**Summary:** Extracts ingredients from a meal plan string and returns them as a list of strings.

**Parameters:**

- meal_plan (str): A string representing the meal plan from which ingredients are to be extracted.
**Returns:** List[str] - A list of strings representing the ingredients extracted from the meal plan.

**Raises:**

- ValueError: If the input meal plan is empty or malformed.
- TypeError: If the input meal plan is not a string.
**Examples:**

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



---

## process_shopping_ingredients

### Description
Processes a list of ingredients to prepare them for shopping.

### Conceptual Info

This shim node takes a list of ingredients as input, processes them, and returns a list of ingredients ready for shopping.

### Docstring

**Summary:** Process a list of ingredients for shopping by potentially cleaning, formatting, or transforming the input.

**Parameters:**

- ingredients (str): A string representing a list of ingredients that need to be processed for shopping.
**Returns:** List[str] - A list of processed ingredients ready for shopping.

**Raises:**

- ValueError: If the input string is not properly formatted or contains invalid ingredients.
- TypeError: If the input is not a string.
**Examples:**

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

