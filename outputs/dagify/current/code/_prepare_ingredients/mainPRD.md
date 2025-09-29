# _prepare_ingredients - Complete PRD Documentation

## Overview
PRDs for nodes in the '_prepare_ingredients' module.

## Table of Contents

- [validate_meal_plan](#validate_meal_plan)

- [validate_ingredient_compatibility](#validate_ingredient_compatibility)

- [parse_ingredients_from_plan](#parse_ingredients_from_plan)

- [parse_cooking_techniques](#parse_cooking_techniques)

- [determine_prep_methods](#determine_prep_methods)

- [apply_preparation_methods](#apply_preparation_methods)



---

## validate_meal_plan

### Description
Validates a meal plan to ensure it meets certain criteria.

### Conceptual Info

This shim node is responsible for validating a meal plan. It checks if the provided meal plan contains necessary information and meets certain criteria.

### Docstring

**Summary:** Validates a meal plan based on its content and structure.

**Parameters:**

- meal_plan (str): The meal plan to be validated. It should contain information about the meal name, ingredients, and cooking techniques.
**Returns:** str - A string indicating whether the meal plan is valid. It may contain additional information about the validation result.

**Raises:**

- ValueError: If the meal plan is empty or does not contain required information.
- TypeError: If the input meal plan is not a string.
**Examples:**

```python
>>> validate_meal_plan(meal_plan="{'meal_name': 'Grilled Chicken', 'ingredients': ['chicken', 'salt', 'pepper'], 'cooking_techniques': ['grilling']}")
'Meal plan is valid.'
```

```python
>>> validate_meal_plan(meal_plan="{'meal_name': '', 'ingredients': [], 'cooking_techniques': []}")
'Meal plan is invalid: Missing required information.'
```



---

## validate_ingredient_compatibility

### Description
Validates the compatibility of purchased ingredients with the meal plan requirements.

### Conceptual Info

This shim node validates whether the ingredients purchased are compatible with the meal plan requirements, ensuring that the necessary ingredients are available for cooking.

### Docstring

**Summary:** Validates the compatibility of purchased ingredients with the meal plan ingredients and cooking techniques.

**Parameters:**

- meal_plan (str): A string representing the meal plan containing the required ingredients and cooking techniques.
- purchased_ingredients (str): A string representing the list of ingredients purchased by the user.
**Returns:** str - A string indicating whether the purchased ingredients are compatible with the meal plan requirements.

**Raises:**

- ValueError: If the meal plan or purchased ingredients are not in the expected format.
- TypeError: If the input types are not as expected (e.g., not strings).
**Examples:**

```python
>>> validate_ingredient_compatibility(meal_plan='{"meal_name": "Grilled Chicken", "ingredients": ["chicken", "salt", "pepper"], "cooking_techniques": ["grilling"]}', purchased_ingredients='["chicken", "salt", "pepper"]')
"true"
```

```python
>>> validate_ingredient_compatibility(meal_plan='{"meal_name": "Pasta", "ingredients": ["pasta", "sauce", "cheese"], "cooking_techniques": ["boiling"]}', purchased_ingredients='["pasta", "sauce"]')
"false"
```



---

## parse_ingredients_from_plan

### Description
Parses a string representing ingredients from a meal plan into a list of individual ingredients

### Conceptual Info

This shim function is responsible for extracting individual ingredients from a string representation of ingredients in a meal plan, converting it into a structured list format for further processing

### Docstring

**Summary:** Parses a string of ingredients into a list of individual ingredients

**Parameters:**

- ingredients_str (str): A string containing the ingredients information, potentially comma-separated or in a list format
**Returns:** List[str] - A list of strings where each string represents an individual ingredient extracted from the input string

**Raises:**

- ValueError: If the input string is malformed or cannot be parsed into a list of ingredients
- TypeError: If the input is not a string
**Examples:**

```python
>>> ingredients_str = 'flour, sugar, eggs, milk'
>>> parse_ingredients_from_plan(ingredients_str=ingredients_str)
['flour', 'sugar', 'eggs', 'milk']
```

```python
>>> ingredients_str = 'flour
sugar
eggs
milk'
>>> parse_ingredients_from_plan(ingredients_str=ingredients_str)
['flour', 'sugar', 'eggs', 'milk']
```



---

## parse_cooking_techniques

### Description
Parses a string containing cooking techniques into a list of individual techniques.

### Conceptual Info

This shim node is responsible for parsing a string that contains cooking techniques and returning a list of individual techniques.

### Docstring

**Summary:** Parses a string of cooking techniques into a list of strings.

**Parameters:**

- techniques_str (str): A string containing one or more cooking techniques, potentially comma-separated or listed in some format.
**Returns:** List[str] - A list of individual cooking techniques extracted from the input string.

**Raises:**

- ValueError: If the input string is malformed or cannot be parsed into a list of techniques.
- TypeError: If the input is not a string.
**Examples:**

```python
>>> parse_cooking_techniques(techniques_str='roasting, sautéing, boiling')
['roasting', 'sautéing', 'boiling']
```

```python
>>> parse_cooking_techniques(techniques_str='grilling')
['grilling']
```



---

## determine_prep_methods

### Description
Determines the preparation methods for an ingredient based on the required cooking techniques.

### Conceptual Info

This shim function plays a crucial role in meal preparation by determining the appropriate preparation methods for ingredients based on the cooking techniques required for the meal.

### Docstring

**Summary:** Determines the preparation methods for an ingredient based on the cooking techniques.

**Parameters:**

- ingredient (str): The ingredient that needs to be prepared.
- cooking_techniques (str): Comma-separated list of cooking techniques required for the meal.
**Returns:** List[str] - List of preparation methods suitable for the ingredient given the cooking techniques.

**Raises:**

- ValueError: When the ingredient is empty or cooking techniques are not provided.
- TypeError: When the input types are incorrect, such as ingredient not being a string or cooking techniques not being a string.
**Examples:**

```python
>>> determine_prep_methods(ingredient='carrot', cooking_techniques='boiling,steaming')
>>> determine_prep_methods(ingredient='beef', cooking_techniques='grilling,roasting')
['peeling', 'chopping']
['marinating', 'slicing']
```



---

## apply_preparation_methods

### Description
Applies various preparation methods to an ingredient based on the provided cooking techniques and returns the prepared ingredient.

### Conceptual Info

This shim function applies preparation methods to ingredients based on the required cooking techniques, playing a crucial role in the meal preparation workflow.

### Docstring

**Summary:** Applies preparation methods to an ingredient based on the given cooking techniques.

**Parameters:**

- ingredient (str): The ingredient to be prepared.
- methods (str): A list of preparation methods to be applied to the ingredient.
**Returns:** str - The prepared ingredient after applying the specified preparation methods.

**Raises:**

- ValueError: If the ingredient is empty or if the preparation methods are not provided.
- TypeError: If the ingredient is not a string or if the methods are not a list of strings.
**Examples:**

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

