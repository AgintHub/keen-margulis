# format_actionable_recommendations PRD

## Description
Formats the given recommendations into a list of actionable recommendations.


## Conceptual Info

This shim function is responsible for taking a string of recommendations and formatting them into a list of actionable steps, which can be used in a sports analysis report.

## Docstring

### Summary
Formats the input recommendations into a list of actionable recommendations.

### Parameters

- **recommendations** (str): A string containing recommendations that need to be formatted into actionable steps.

### Returns

List[str]: A list of strings where each string is an actionable recommendation.

### Raises

- ValueError: If the input recommendations are empty or not a string.
- TypeError: If the input is not of type string.

### Examples

```python
>>> format_actionable_recommendations('Improve team communication,Increase training sessions')
['Improve team communication', 'Increase training sessions']
```

```python
>>> format_actionable_recommendations('Enhance player fitness')
['Enhance player fitness']
```
