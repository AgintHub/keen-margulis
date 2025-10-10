# _cook_meal - Complete PRD Documentation

## Overview
PRDs for nodes in the '_cook_meal' module.

## Table of Contents

- [extract_cooking_techniques](#extract_cooking_techniques)

- [validate_cooking_techniques](#validate_cooking_techniques)

- [validate_ingredients_sufficiency](#validate_ingredients_sufficiency)

- [create_cooking_plan](#create_cooking_plan)

- [execute_cooking_process](#execute_cooking_process)

- [finalize_meal_name](#finalize_meal_name)



---

## extract_cooking_techniques

### Description
Extracts cooking techniques from the provided input string.

### Conceptual Info

This shim node is responsible for extracting cooking techniques from a given input string, which is expected to contain information about how to cook a meal.

### Docstring

**Summary:** Extracts a list of cooking techniques from the input string provided in kwargs.

**Parameters:**

- kwargs (str): Input string containing information about cooking techniques.
**Returns:** List[str] - A list of cooking techniques extracted from the input string.

**Raises:**

- ValueError: If the input string is empty or does not contain valid cooking techniques.
- TypeError: If the input is not a string.
**Examples:**

```python
>>> extract_cooking_techniques(kwargs='Grill the chicken, then roast the vegetables.')
>>> # Expected output: ['Grill', 'roast']
['Grill', 'roast']
```

```python
>>> extract_cooking_techniques(kwargs='Boil water and then steam the broccoli.')
>>> # Expected output: ['Boil', 'steam']
['Boil', 'steam']
```



---

## validate_cooking_techniques

### Description
Validates the cooking techniques provided to ensure they are appropriate for meal preparation.

### Conceptual Info

This shim node is responsible for validating cooking techniques provided as input to ensure they are valid and appropriate for meal preparation.

### Docstring

**Summary:** Validates cooking techniques to ensure they are appropriate for meal preparation.

**Parameters:**

- cooking_techniques (str): A string containing cooking techniques separated by commas.
**Returns:** str - A message indicating whether the cooking techniques are valid.

**Raises:**

- ValueError: When the cooking techniques provided are invalid or not supported.
- TypeError: When the input type is not a string.
**Examples:**

```python
>>> validate_cooking_techniques(cooking_techniques='roasting,baking')
'Cooking techniques are valid.'
```

```python
>>> validate_cooking_techniques(cooking_techniques='invalid_technique')
'ValueError: Invalid cooking technique: invalid_technique'
```



---

## validate_ingredients_sufficiency

### Description
Validates if the prepared ingredients are sufficient for the given cooking techniques.

### Conceptual Info

This shim node validates the sufficiency of prepared ingredients based on the required cooking techniques, playing a crucial role in the meal preparation pipeline.

### Docstring

**Summary:** Validates the sufficiency of prepared ingredients for given cooking techniques and returns a validation result.

**Parameters:**

- prepared_ingredients (str): A string representing the list of prepared ingredients.
- cooking_techniques (str): A string representing the list of cooking techniques to be applied.
**Returns:** str - A string indicating whether the prepared ingredients are sufficient for the cooking techniques.

**Raises:**

- ValueError: If the input strings are not in the expected format or if the ingredients are insufficient.
- TypeError: If the input types are not strings.
**Examples:**

```python
>>> validate_ingredients_sufficiency(prepared_ingredients='["salt", "pepper", "oil"]', cooking_techniques='["frying", "seasoning"]')
'Ingredients are sufficient.'
```

```python
>>> validate_ingredients_sufficiency(prepared_ingredients='["salt"]', cooking_techniques='["frying", "boiling"]')
'Insufficient ingredients for the required cooking techniques.'
```



---

## create_cooking_plan

### Description
Creates a cooking plan based on prepared ingredients and cooking techniques.

### Conceptual Info

This shim generates a cooking plan by combining the prepared ingredients and selected cooking techniques, serving as a crucial step in the meal preparation process.

### Docstring

**Summary:** Creates a cooking plan by integrating prepared ingredients and cooking techniques into a structured plan.

**Parameters:**

- prepared_ingredients (str): A string representation of a list of prepared ingredients.
- cooking_techniques (str): A string representation of a list of cooking techniques to be applied.
**Returns:** str - A JSON-formatted string representing the cooking plan, including ingredient allocation and technique application sequence.

**Raises:**

- ValueError: If the prepared ingredients or cooking techniques are not in the expected format.
- TypeError: If the input types are not string representations of lists.
**Examples:**

```python
>>> create_cooking_plan(prepared_ingredients='["chicken", "rice", "vegetables"]', cooking_techniques='["grilling", "boiling"]')
"{'ingredients': ['chicken', 'rice', 'vegetables'], 'techniques': ['grilling', 'boiling'], 'plan': ['grill chicken', 'boil rice and vegetables']}"
```

```python
>>> create_cooking_plan(prepared_ingredients='["eggs", "milk", "flour"]', cooking_techniques='["whisking", "frying"]')
"{'ingredients': ['eggs', 'milk', 'flour'], 'techniques': ['whisking', 'frying'], 'plan': ['whisk eggs and milk', 'mix with flour and fry']}"
```



---

## execute_cooking_process

### Description
Executes the cooking process based on the provided cooking plan and returns the result.

### Conceptual Info

This shim node represents the execution of a cooking process based on a predefined cooking plan. It acts as a bridge between the planning stage and the actual cooking execution, encapsulating the complexity of cooking.

### Docstring

**Summary:** Executes the cooking process according to the provided cooking plan and returns the result as a string.

**Parameters:**

- cooking_plan (str): A string representation of the cooking plan that outlines the steps and ingredients needed for cooking.
**Returns:** str - The outcome of the cooking process, which could be a description of the cooked meal or any relevant status message.

**Raises:**

- ValueError: If the cooking plan is invalid or missing essential information.
- TypeError: If the input cooking plan is not of type string.
**Examples:**

```python
>>> cooking_plan = '{"recipe": "grilled chicken", "ingredients": ["chicken", "salt", "pepper"], "steps": ["marinate", "grill"]}'
>>> result = execute_cooking_process(cooking_plan=cooking_plan)
"Grilled chicken is ready."
```

```python
>>> cooking_plan = '{"recipe": "scrambled eggs", "ingredients": ["eggs", "salt", "butter"], "steps": ["crack eggs", "scramble"]}'
>>> result = execute_cooking_process(cooking_plan=cooking_plan)
"Scrambled eggs are ready."
```



---

## finalize_meal_name

### Description
Finalizes the name of the cooked meal based on the cooked result.

### Conceptual Info

This shim function takes the cooked result from the cooking process and generates a final name for the meal, making it presentable and identifiable.

### Docstring

**Summary:** Finalizes the name of the cooked meal based on the input cooked result.

**Parameters:**

- cooked_result (str): The result from the cooking process that needs to be finalized into a meal name.
**Returns:** str - The finalized name of the cooked meal, ready for presentation.

**Raises:**

- ValueError: If the cooked result is empty or not a valid string.
- TypeError: If the input cooked result is not of type string.
**Examples:**

```python
>>> finalize_meal_name(cooked_result='Grilled chicken with spices')
'Spicy Grilled Chicken Delight'
```

```python
>>> finalize_meal_name(cooked_result='Vegetable stir-fry')
'Veggie Stir-Fry'
```

