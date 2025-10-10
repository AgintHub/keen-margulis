# extract_cooking_techniques PRD

## Description
Extracts cooking techniques from the provided input string.


## Conceptual Info

This shim node is responsible for extracting cooking techniques from a given input string, which is expected to contain information about how to cook a meal.

## Docstring

### Summary
Extracts a list of cooking techniques from the input string provided in kwargs.

### Parameters

- **kwargs** (str): Input string containing information about cooking techniques.

### Returns

List[str]: A list of cooking techniques extracted from the input string.

### Raises

- ValueError: If the input string is empty or does not contain valid cooking techniques.
- TypeError: If the input is not a string.

### Examples

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
