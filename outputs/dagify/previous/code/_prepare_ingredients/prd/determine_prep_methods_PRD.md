# determine_prep_methods PRD

## Description
Determines the preparation methods for an ingredient based on the required cooking techniques.


## Conceptual Info

This shim function plays a crucial role in meal preparation by determining the appropriate preparation methods for ingredients based on the cooking techniques required for the meal.

## Docstring

### Summary
Determines the preparation methods for an ingredient based on the cooking techniques.

### Parameters

- **ingredient** (str): The ingredient that needs to be prepared.
- **cooking_techniques** (str): Comma-separated list of cooking techniques required for the meal.

### Returns

List[str]: List of preparation methods suitable for the ingredient given the cooking techniques.

### Raises

- ValueError: When the ingredient is empty or cooking techniques are not provided.
- TypeError: When the input types are incorrect, such as ingredient not being a string or cooking techniques not being a string.

### Examples

```python
>>> determine_prep_methods(ingredient='carrot', cooking_techniques='boiling,steaming')
>>> determine_prep_methods(ingredient='beef', cooking_techniques='grilling,roasting')
['peeling', 'chopping']
['marinating', 'slicing']
```
