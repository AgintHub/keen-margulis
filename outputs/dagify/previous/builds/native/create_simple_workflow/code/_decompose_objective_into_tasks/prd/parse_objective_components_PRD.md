# parse_objective_components PRD

## Description
Parses a workflow objective string into a list of its constituent components.


## Conceptual Info

This shim takes a validated workflow objective string and splits it into individual, actionable components that can later be used to generate tasks.

## Docstring

### Summary
Parses the provided objective string into a list of its constituent components.

### Parameters

- **objective** (str): A validated workflow objective string to be parsed.

### Returns

List[str]: A list of strings, each representing an actionable component of the objective.

### Raises

- ValueError: Raised when the objective string cannot be parsed into any component.
- TypeError: Raised when the provided objective is not of type str.

### Examples

```python
>>> parsed = parse_objective_components('Build a web app that allows users to upload photos and share them with friends')
>>> print(parsed)
['Build a web app', 'allow users to upload photos', 'share them with friends']
```

```python
>>> parsed = parse_objective_components('Create a financial model to forecast quarterly earnings')
>>> print(parsed)
['Create a financial model', 'forecast quarterly earnings']
```
