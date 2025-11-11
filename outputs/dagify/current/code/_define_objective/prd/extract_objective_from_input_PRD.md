# extract_objective_from_input PRD

## Description
Extracts the objective or task description from the given processed input string.


## Conceptual Info

This shim function is designed to take a processed input string, extract the objective or task description from it, and return it in a structured format.

## Docstring

### Summary
Extracts the objective from the given processed input string and returns it along with the processed input.

### Parameters

- **processed_input** (str): The input string that has been cleaned and normalized, from which the objective will be extracted.

### Returns

dict: A dictionary containing the extracted objective as 'output' and the processed input as 'processed_input'.

### Raises

- ValueError: If the processed input is empty or does not contain a valid objective.
- TypeError: If the processed input is not a string.

### Examples

```python
>>> extract_objective_from_input(processed_input='Define a task to improve customer satisfaction.')
{'output': 'Improve customer satisfaction', 'processed_input': 'Define a task to improve customer satisfaction.'}
```

```python
>>> extract_objective_from_input(processed_input='The objective is to reduce costs.')
{'output': 'Reduce costs', 'processed_input': 'The objective is to reduce costs.'}
```
