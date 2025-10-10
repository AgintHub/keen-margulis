# _plan_meal - Complete PRD Documentation

## Overview
PRDs for nodes in the '_plan_meal' module.

## Table of Contents

- [parse_meal_requirements](#parse_meal_requirements)

- [select_recipe](#select_recipe)

- [extract_meal_name](#extract_meal_name)

- [identify_ingredients](#identify_ingredients)

- [determine_cooking_techniques](#determine_cooking_techniques)

- [format_ingredients_list](#format_ingredients_list)

- [format_cooking_techniques](#format_cooking_techniques)



---

## parse_meal_requirements

### Description
Parses meal requirements from a given input text into a structured dictionary format.

### Conceptual Info

This shim node is responsible for transforming unstructured input text into a structured dictionary containing meal requirements, which can then be used for further processing such as recipe selection.

### Docstring

**Summary:** Parses meal requirements from input text into a structured dictionary format.

**Parameters:**

- input_text (str): The input text containing meal requirements to be parsed
**Returns:** str - A JSON string representing the parsed meal requirements, expected to be a dictionary containing meal name, ingredients, and cooking techniques.

**Raises:**

- ValueError: When the input text is empty or does not contain valid meal requirements.
- TypeError: When the input is not a string.
**Examples:**

```python
>>> parse_meal_requirements(input_text='Prepare a vegan salad with avocado and tomatoes')
>>> # Expected output: A JSON string representing the parsed requirements
"{'meal_name': 'Vegan Salad', 'ingredients': ['avocado', 'tomatoes'], 'cooking_techniques': []}"
```

```python
>>> parse_meal_requirements(input_text='Cook chicken with olive oil and garlic')
>>> # Expected output: A JSON string representing the parsed requirements
"{'meal_name': 'Chicken Dish', 'ingredients': ['chicken', 'olive oil', 'garlic'], 'cooking_techniques': ['cooking']}"
```



---

## select_recipe

### Description
Selects a recipe based on the given meal requirements.

### Conceptual Info

This shim function is responsible for selecting a suitable recipe based on the parsed meal requirements. It acts as a bridge between meal requirement parsing and meal planning.

### Docstring

**Summary:** Selects a recipe based on the given meal requirements and returns it as a string.

**Parameters:**

- requirements (str): A string representation of the meal requirements dictionary.
**Returns:** str - A string representation of the selected recipe dictionary.

**Raises:**

- ValueError: If the input requirements string is not a valid representation of a dictionary.
- TypeError: If the input requirements is not a string.
**Examples:**

```python
>>> select_recipe(requirements='{"cuisine": "Italian", "diet": "Vegetarian"}')
'{"recipe_name": "Pasta Primavera", "ingredients": ["pasta", "vegetables"], "cooking_techniques": ["boiling", "sauteing"]}'
```

```python
>>> select_recipe(requirements='{"cuisine": "Mexican", "diet": "Non-Vegetarian"}')
'{"recipe_name": "Chicken Tacos", "ingredients": ["chicken", "tortillas", "cheese"], "cooking_techniques": ["grilling", "frying"]}'
```



---

## extract_meal_name

### Description
Extracts the meal name from a given recipe string.

### Conceptual Info

This shim function is designed to extract the meal name from a given recipe string, playing a crucial role in meal planning by identifying the name of the meal to be prepared.

### Docstring

**Summary:** Extracts the meal name from a recipe string.

**Parameters:**

- recipe (str): The recipe string containing the meal information.
**Returns:** str - The extracted meal name.

**Raises:**

- ValueError: If the recipe string is empty or does not contain a valid meal name.
- TypeError: If the input recipe is not of type string.
**Examples:**

```python
>>> extract_meal_name(recipe='Chicken Parmesan Recipe')
'Chicken Parmesan'
```

```python
>>> extract_meal_name(recipe='{ "meal_name": "Beef Stew" }')
'Beef Stew'
```



---

## identify_ingredients

### Description
Extracts and identifies ingredients from a given recipe.

### Conceptual Info

This shim function is designed to parse a given recipe and extract the list of ingredients required for it.

### Docstring

**Summary:** Identifies and returns a list of ingredients from the provided recipe.

**Parameters:**

- recipe (str): The input recipe in string format from which ingredients will be extracted.
**Returns:** list[str] - A list of ingredients required for the recipe.

**Raises:**

- ValueError: If the input recipe is empty or not in the expected format.
- TypeError: If the input recipe is not a string.
**Examples:**

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



---

## determine_cooking_techniques

### Description
This shim determines the cooking techniques required based on the input recipe.

### Conceptual Info

This shim analyzes a given recipe to identify the necessary cooking techniques, playing a crucial role in meal planning by providing essential cooking information.

### Docstring

**Summary:** Determines the cooking techniques required for a given recipe.

**Parameters:**

- recipe (str): A string representing the recipe to analyze.
**Returns:** list[str] - A list of strings representing the cooking techniques required.

**Raises:**

- ValueError: If the input recipe is empty or malformed.
- TypeError: If the input recipe is not a string.
**Examples:**

```python
>>> recipe = 'Grilled Chicken with Roasted Vegetables'
>>> cooking_techniques = determine_cooking_techniques(recipe)
>>> print(cooking_techniques)
['Grilling', 'Roasting']
```

```python
>>> recipe = 'Pan-Seared Salmon with Quinoa'
>>> cooking_techniques = determine_cooking_techniques(recipe)
>>> print(cooking_techniques)
['Pan-Sealing', 'Boiling']
```



---

## format_ingredients_list

### Description
Formats a list of ingredients into a human-readable string representation.

### Conceptual Info

This shim function is designed to take a list of ingredients as input and produce a formatted string that represents these ingredients in a human-readable format, likely for inclusion in a recipe or meal plan output.

### Docstring

**Summary:** Formats a list of ingredients into a human-readable string.

**Parameters:**

- ingredients (str): A string representing a list of ingredients. The exact format of this string is not specified, but it is expected to be parseable into a list of ingredients.
**Returns:** str - A formatted string representation of the ingredients list, suitable for display to the user.

**Raises:**

- ValueError: If the input string cannot be parsed into a list of ingredients.
- TypeError: If the input is not a string.
**Examples:**

```python
>>> ingredients_list = 'eggs, flour, sugar, milk'
>>> formatted_ingredients = format_ingredients_list(ingredients=ingredients_list)
'eggs\nflour\nsugar\nmilk'
```

```python
>>> ingredients_list = 'salt, pepper, garlic'
>>> formatted_ingredients = format_ingredients_list(ingredients=ingredients_list)
'salt\npepper\ngarlic'
```



---

## format_cooking_techniques

### Description
Formats a list of cooking techniques into a string representation.

### Conceptual Info

This shim node is responsible for taking a list or string of cooking techniques and formatting it into a human-readable string format.

### Docstring

**Summary:** Formats cooking techniques into a string.

**Parameters:**

- techniques (str): A list or comma-separated string of cooking techniques to be formatted.
**Returns:** str - A formatted string representation of the cooking techniques, potentially comma-separated or bulleted.

**Raises:**

- ValueError: If the input techniques are not in an expected format (e.g., not a list or comma-separated string).
- TypeError: If the input techniques are not of type string or list.
**Examples:**

```python
>>> format_cooking_techniques(techniques='grilling,roasting,boiling')
'grilling, roasting, boiling'
```

```python
>>> format_cooking_techniques(techniques=['grilling', 'roasting', 'boiling'])
'grilling, roasting, boiling'
```

